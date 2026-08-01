import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters

import db.users.crud as user_crud
import db.agents.crud as agent_crud
import db.sessions.crud as session_crud
import db.messages.crud as message_crud
from db.client import db
from core.pipeline.runner import run_agent_pipeline

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db_user = await user_crud.get_or_create_user(str(user.id), user.username or "Unknown")
    await update.message.reply_text(f"Hello {db_user.username}! Use /store to view available agents.")

async def store(update: Update, context: ContextTypes.DEFAULT_TYPE):
    agents = await agent_crud.get_active_agents()
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
        
        db_user = await user_crud.get_or_create_user(user_id, query.from_user.username or "Unknown")
        
        session = await session_crud.switch_user_agent(db_user.id, agent_id)
        agent = await db.agent.find_unique(where={"id": agent_id})
        
        await query.edit_message_text(text=f"Switched to agent: {agent.name}\n{agent.description}")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    text = update.message.text
    
    db_user = await user_crud.get_or_create_user(user_id, update.effective_user.username or "Unknown")
    
    session = await db.session.find_first(
        where={"user_id": db_user.id, "isActive": True},
        include={"agent": True}
    )
    
    if not session:
        await update.message.reply_text("Please select an agent first using /store.")
        return
        
    await message_crud.save_message(session.id, "user", text)
    
    response_text = await run_agent_pipeline(
        system_prompt=session.agent.system_prompt,
        user_text=text
    )
    
    await message_crud.save_message(session.id, "assistant", response_text)
    await update.message.reply_text(response_text)
    
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    db_user = await user_crud.get_or_create_user(user_id, update.effective_user.username or "Unknown")
    
    session = await db.session.find_first(
        where={"user_id": db_user.id, "isActive": True},
        include={"agent": True}
    )
    
    if not session:
        await update.message.reply_text("Please select an agent first using /store.")
        return
        
    voice_file = await update.message.voice.get_file()
    file_path = f"{user_id}_voice.ogg"
    await voice_file.download_to_drive(file_path)
    
    await update.message.reply_text("Processing voice...")
    
    response_text = await run_agent_pipeline(
        system_prompt=session.agent.system_prompt,
        user_audio_path=file_path
    )
    
    await update.message.reply_text(response_text)
    
    if os.path.exists(file_path):
        os.remove(file_path)

async def start_telegram_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token or token == "your_telegram_bot_token_here":
        logger.error("TELEGRAM_BOT_TOKEN is not set in .env. Bot cannot start.")
        return
        
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("store", store))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))

    logger.info("Telegram polling initialized.")
    await application.run_polling()
