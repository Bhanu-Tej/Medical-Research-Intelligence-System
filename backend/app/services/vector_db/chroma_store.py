import chromadb


class ChromaVectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="medical_research"
        )
    
    def add_documents(
        self,
        chunks,
        embeddings,
        source
    ):

        existing_count = self.collection.count()

        ids = [
            f"id_{existing_count + i}"
            for i in range(len(chunks))
        ]

        metadatas = [
            {
                "source": source
            }
            for _ in chunks
        ]

        self.collection.add(
            documents=chunks,
            embeddings=embeddings.tolist(),
            ids=ids,
            metadatas=metadatas
        )

    def get_all_documents(self):

        results = self.collection.get()

        return results

    def reset_database(self):

        self.client.delete_collection(
            name="medical_research"
        )

        self.collection = self.client.get_or_create_collection(
            name="medical_research"
        )

    def get_stats(self):

        results = self.collection.get()

        metadatas = results.get(
            "metadatas",
            []
        )

        unique_sources = list(
            set(
                [
                    meta["source"]
                    for meta in metadatas
                ]
            )
        )

        return {
            "total_chunks": self.collection.count(),
            "documents": unique_sources,
            "total_documents": len(unique_sources)
        }

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        if self.collection.count() == 0:

            return []

        results = self.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k
        )

        documents = results["documents"][0]

        metadatas = results["metadatas"][0]

        combined_results = []

        for doc, meta in zip(
            documents,
            metadatas
        ):

            combined_results.append({
                "content": doc,
                "source": meta["source"]
            })

        return combined_results