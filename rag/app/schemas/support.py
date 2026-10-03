from typing import List
from pydantic import BaseModel, Field


class SupportRequest(BaseModel):
    question: str = Field(..., description="The user's support question")


class SupportResponse(BaseModel):
    answer: str = Field(..., description="The grounded answer from the knowledge base")
    sources: List[str] = Field(
        default_factory=list, description="List of KB article IDs cited"
    )
