from typing import List, TypedDict

# This GraphState class acts as the central data structure that flows through 
# every node in our graph workflow.
# documents  - contains all the retrieved documents from both local and web sources.

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """

    question: str
    generation: str
    web_search: bool
    documents: List[str]