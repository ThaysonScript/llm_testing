from langchain_core.vectorstores import InMemoryVectorStore
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from src.embeddings.embedding import Embedding


class VectorStore:
    def __init__(self, batch_size=4, threads=4):
        self.batch_size = batch_size
        self.threads = threads
        self.document_ids = list()
        self.vector_store = self.get_vector_store_embedding(Embedding.get_embedding_instance())


    def get_vector_store_embedding(self, embeddings):
        return InMemoryVectorStore(embeddings)


    # Função para processar um lote e armazenar no vector store
    def process_batch(start_idx):
        batch = all_splits[start_idx: start_idx + self.batch_size]
        return self.vector_store.add_documents(documents=batch)


    def generate_threads(self):
        # Cria um pool de threads para paralelizar a execução
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = {executor.submit(process_batch, i): i for i in range(0, len(all_splits), batch_size)}

            for future in tqdm(as_completed(futures), total=len(futures), desc="Processando lotes em paralelo"):
                document_ids.append(future.result())  # Armazena os IDs processados

        print("✅ Processamento concluído com paralelismo!")