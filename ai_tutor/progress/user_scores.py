import uuid
from graphdb.neo4j_setup import run_cypher

def record_user_score(user_name: str, quiz_id: str, score: int, total: int):
    user_id = str(uuid.uuid4())

    run_cypher("""
        MERGE (u:User {name:$name})
        ON CREATE SET u.id=$id, u.joined_at=datetime()
    """, {"name": user_name, "id": user_id})

    attempt_id = str(uuid.uuid4())
    run_cypher("""
        MATCH (u:User {name:$name}), (q:Quiz {id:$quiz_id})
        CREATE (u)-[:TOOK]->(:Attempt {id:$aid, score:$score, total:$total, created_at:datetime()})-[:OF]->(q)
    """, {"name": user_name, "quiz_id": quiz_id, "aid": attempt_id, "score": score, "total": total})
