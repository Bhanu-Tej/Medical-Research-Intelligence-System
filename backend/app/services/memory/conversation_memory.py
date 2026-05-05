conversation_store = {}


def add_message(
    session_id,
    role,
    content
):

    if session_id not in conversation_store:

        conversation_store[session_id] = []

    conversation_store[session_id].append({
        "role": role,
        "content": content
    })


def get_conversation(
    session_id
):

    return conversation_store.get(
        session_id,
        []
    )


def clear_conversation(
    session_id
):

    if session_id in conversation_store:

        del conversation_store[session_id]