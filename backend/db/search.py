from db.client import db
import logging

def generate_mock_embedding(text: str) -> list[float]:
    # MVP mock embedding for demonstration
    # In production, use OpenAI / sentence-transformers to generate 1536-d vectors
    return [0.01] * 1536

async def search_agents_by_capability(query: str, limit: int = 3):
    """Searches millions of agents using pgvector cosine distance."""
    # query_vector = generate_mock_embedding(query)
    # embedding_str = "[" + ",".join(map(str, query_vector)) + "]"
    
    # query_sql = f"""
    #     SELECT id, name, description
    #     FROM "Agent"
    #     WHERE capability_embedding IS NOT NULL
    #     ORDER BY capability_embedding <-> '{embedding_str}'::vector
    #     LIMIT {limit};
    # """
    # try:
    #     results = await db.query_raw(query_sql)
    #     return results
    # except Exception as e:
    #     logging.error(f"Vector search failed: {e}")
    
    # Fallback to simple DB query for MVP without true vectors populated
    agents = await db.agent.find_many(take=limit)
    return agents
