# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str