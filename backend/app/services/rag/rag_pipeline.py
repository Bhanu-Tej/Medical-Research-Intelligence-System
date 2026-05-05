import ollama

from app.services.memory.conversation_memory import (
    get_conversation
)


def generate_rag_response(
    session_id,
    query,
    retrieved_chunks
):

    context = "\n\n".join(
        [
            chunk["content"]
            for chunk in retrieved_chunks
        ]
    )

    conversation_history = get_conversation(
        session_id
    )

    history_text = ""

    for message in conversation_history:

        history_text += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    prompt = f"""
You are a medical research assistant.

STRICT RULES:
- Answer ONLY using provided context.
- Use conversation history for follow-up understanding.
- Do NOT hallucinate.
- If answer not found,
  say:
  "I could not find enough medical evidence."

Conversation History:
{history_text}

Medical Context:
{context}

Question:
{query}
"""

    response = ollama.chat(

        model="llama3:8b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]