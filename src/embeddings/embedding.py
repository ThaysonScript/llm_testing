from langchain_huggingface import HuggingFaceEmbeddings

class Embedding:
    def __init__(self):
        pass


    def get_embedding_instance(self, model='sentence-transformers/all-mpnet-base-v2'):
        return HuggingFaceEmbeddings(model_name=model)
