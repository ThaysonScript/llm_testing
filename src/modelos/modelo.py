from langchain_groq import ChatGroq

class Modelo:
    def __init__(self):
        self.models = {
            'google_gemma': 'gemma2-9b-it',
            'meta_llama': 'llama-3.3-70b-versatile',
            'deep_seek': 'deepseek-r1-distill-qwen-32b'
        }

        self.google_llm = ChatGroq(model=self.models['google_gemma'])
        self.meta_llm = ChatGroq(model=self.models['meta_llama'])
        self.deep_seek_llm = ChatGroq(model=self.models['deep_seek'])

    def imprimir_llms_carregadas(self):
        print(f'GOOGLE_LLM: {self.google_llm}\n')
        print(f'META_LLM: {self.meta_llm}\n')
        print(f'DEEP_SEEK_LLM: {self.deep_seek_llm}\n')