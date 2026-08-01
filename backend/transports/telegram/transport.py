import os
import certifi

# Fix for Windows SSL Certificate Verification Error
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["SSL_CERT_DIR"] = certifi.where()

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters

from db.crud import get_or_create_user, get_active_agents, switch_user_agent
from db.client import db
from core.router import MessageRouter

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db_user = await get_or_create_user(str(user.id), user.username or "Unknown")
    await update.message.reply_text(f"Hello {db_user.username}! Use /store to view available agents.")

async def store(update: Update, context: ContextTypes.DEFAULT_TYPE):
    agents = await get_active_agents()
    if not agents:
        await update.message.reply_text("No active agents found in the store.")
        return
        
    keyboard = []
    for agent in agents:
        keyboard.append([InlineKeyboardButton(agent.name, callback_data=f"switch_{agent.id}")])
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select an agent:", reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data.startswith("switch_"):
        agent_id = query.data.split("_")[1]
        user_id = str(query.from_user.id)
        
        db_user = await get_or_create_user(user_id, query.from_user.username or "Unknown")
        
        session = await switch_user_agent(db_user.id, agent_id)
        agent = await db.agent.find_unique(where={"id": agent_id})
        
        await query.edit_message_text(text=f"Switched to agent: {agent.name}\n{agent.description}")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    text = update.message.text
    
    response_text = await MessageRouter.process_telegram_message(
        telegram_id=user_id,
        username=update.effective_user.username,
        text=text
    )
    
    await update.message.reply_text(response_text)
    
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Voice messages are currently being upgraded to the new unified pipeline. Please send text for now.")

async def start_telegram_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token or token == "your_telegram_bot_token_here":
        logger.error("TELEGRAM_BOT_TOKEN is not set in .env. Bot cannot start.")
        return
        
    from telegram.request import HTTPXRequest
    # Disable SSL verification for local dev to bypass Windows cert/proxy issues
    request = HTTPXRequest(httpx_kwargs={"verify": False})
    application = ApplicationBuilder().token(token).request(request).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("store", store))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))

    logger.info("Telegram polling initialized.")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
