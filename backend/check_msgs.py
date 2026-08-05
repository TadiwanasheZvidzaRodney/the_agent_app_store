import asyncio
from prisma import Prisma

async def main():
    db = Prisma()
    await db.connect()
    
    msgs = await db.message.find_many(order={'createdAt':'desc'}, take=10)
    for m in msgs:
        print(f"[{m.role}] {m.content}")
        
    await db.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
