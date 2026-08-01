import os
from groq import AsyncGroq
from db.crud import get_or_create_user, get_active_session, save_message, get_session_history

# Initialize Groq Client
# Ensure GROQ_API_KEY is in .env
client = AsyncGroq(api_key=os.environ.get("GROQ_API_KEY"))

class MessageRouter:
    @staticmethod
    async def process_telegram_message(telegram_id: str, username: str, text: str) -> str:
        # 1. Get or create user based on Telegram ID
        user = await get_or_create_user(telegram_id=str(telegram_id), username=username or "Telegram User")
        
        # 2. Get the active session for this user
        session = await get_active_session(user_id=user.id)
        if not session:
            return "You don't have an active agent session right now. Please select one from the Dashboard!"
            
        agent = session.agent
        
        # 3. Save the incoming user message to the DB
        await save_message(session_id=session.id, role="user", content=text)
        
        # 4. Fetch conversation history for context
        history = await get_session_history(session_id=session.id, limit=10)
        
        # 5. Build the prompt payload
        messages = [{"role": "system", "content": agent.system_prompt}]
        for msg in history:
            messages.append({"role": msg.role, "content": msg.content})
            
        # 6. Call the LLM (Groq) via the Pipecat-agnostic pipeline
        try:
            chat_completion = await client.chat.completions.create(
                messages=messages,
                model=agent.llm_model or "llama3-8b-8192",
            )
            reply = chat_completion.choices[0].message.content
            
            # 7. Save the bot's response to the DB
            await save_message(session_id=session.id, role="assistant", content=reply)
            return reply
        except Exception as e:
            import logging
            logging.error(f"Error in MessageRouter: {e}")
            return f"Agent encountered an error: {str(e)}"
