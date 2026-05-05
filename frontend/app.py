import streamlit as st
import requests


BACKEND_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Medical Research Intelligence System",
    layout="wide"
)


st.title("🩺 Medical Research Intelligence System")

st.markdown(
    "AI-powered Medical RAG Assistant using FastAPI, ChromaDB, Ollama and Llama 3"
)


# SESSION ID

session_id = st.text_input(
    "Session ID",
    value="bhanu"
)


st.divider()


# PDF UPLOAD SECTION

st.header("📄 Upload Medical Research Papers")

uploaded_files = st.file_uploader(
    "Upload one or more PDFs",
    type=["pdf"],
    accept_multiple_files=True
)


if st.button("Upload PDFs"):

    if uploaded_files:

        for uploaded_file in uploaded_files:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/upload-pdf",
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    f"✅ {result['message']}"
                )

            else:

                st.error(
                    f"❌ Failed to upload {uploaded_file.name}"
                )

    else:

        st.warning("Please upload at least one PDF")


st.divider()


# QUESTION SECTION

st.header("💬 Ask Medical Questions")

question = st.text_area(
    "Enter your medical research question"
)


if st.button("Ask Question"):

    if question:

        payload = {
            "session_id": session_id,
            "question": question
        }

        response = requests.post(
            f"{BACKEND_URL}/ask-question",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("🧠 AI Answer")

            st.write(result["answer"])

            st.subheader("📚 Sources")

            for idx, source in enumerate(result["sources"]):

                with st.expander(
                    f"Source {idx + 1} — {source['source']}"
                ):

                    st.write(source["content"])

        else:

            st.error("Error generating response")

    else:

        st.warning("Please enter a question")


st.divider()


# DATABASE STATS

st.header("📊 Database Statistics")

if st.button("Load Database Stats"):

    response = requests.get(
        f"{BACKEND_URL}/database-stats"
    )

    if response.status_code == 200:

        stats = response.json()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Documents",
                stats["total_documents"]
            )

        with col2:
            st.metric(
                "Total Chunks",
                stats["total_chunks"]
            )

        st.subheader("Indexed Documents")

        for doc in stats["documents"]:
            st.write(f"• {doc}")


st.divider()


# RESET DATABASE

st.header("⚠️ Reset Vector Database")

if st.button("Reset Database"):

    response = requests.delete(
        f"{BACKEND_URL}/reset-database"
    )

    if response.status_code == 200:

        st.success("✅ Database reset successful")

    else:

        st.error("❌ Failed to reset database")