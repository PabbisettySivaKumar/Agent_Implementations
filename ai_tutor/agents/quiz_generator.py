import json, uuid
from agents.tutor_agents import get_llm
from agents.knowledge_agents import semantic_search_resource
from graphdb.neo4j_setup import run_cypher

QUIZ_PROMPT = """
You are a tutor. Based on the study material below, create {n} quiz questions.
Output only a valid JSON array. Each element should have:
"question", "options" (list), "answer".

Study material:
{context}
"""

def generate_quiz(topic: str, n: int = 5):
    llm = get_llm()
    context = semantic_search_resource(topic, top_k=8)
    prompt = QUIZ_PROMPT.format(n=n, context=context)
    raw = llm(prompt)

    try:
        start, end = raw.index("["), raw.rfind("]") + 1
        questions = json.loads(raw[start:end])
    except Exception:
        questions = []

    quiz_id = str(uuid.uuid4())
    run_cypher("MERGE (q:Quiz {id:$id}) SET q.topic=$topic, q.raw=$raw", {"id": quiz_id, "topic": topic, "raw": raw})
    return quiz_id, questions
