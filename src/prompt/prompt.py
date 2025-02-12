from langchain import hub
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from IPython.display import Image, display

from src.prompt.state import State

class Prompt:
    def __init__(self):
        # Define prompt for question-answering
        self.prompt = hub.pull("rlm/rag-prompt")


    def flow_percurse(self):
        display(Image(graph.get_graph().draw_mermaid_png()))


    # Define application steps
    def retrieve(self, state: State):
        retrieved_docs = vector_store.similarity_search(state["question"])
        return {"context": retrieved_docs}


    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = prompt.invoke({"question": state["question"], "context": docs_content})
        response = new_obj.deep_seek_llm.invoke(messages)
        return {"answer": response.content}


    def compile_test(self, question) -> TypedDict:
        # Compile application and test
        graph = StateGraph(State).add_sequence([Prompt.retrieve, Prompt.generate]).add_edge(START, "retrieve").compile()
        return graph.invoke('question': question)