from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from model import llm_model

# Literal - Validation – Prevents invalid inputs. avoids someone passing "Google" instead of "websearch"
# Field - Metadata – Provides additional context about the data being validated.
# ... - you must provide datasource when creating a RouteQuery object.
class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "websearch"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore.",
    )

llm = llm_model

structured_llm_router = llm.with_structured_output(RouteQuery)

system = """You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
Use the vectorstore for questions on these topics. For all else, use web-search."""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router

# the final message the llm sees

# System: You are an expert at routing a user question to a vectorstore or web search.
# The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
# Use the vectorstore for questions on these topics. For all else, use web-search.

# Human: What are the latest prompt engineering techniques?

# [Hidden instruction from LangChain]: Respond in JSON matching this schema:
# {
#   "datasource": "vectorstore" | "websearch"
# }
