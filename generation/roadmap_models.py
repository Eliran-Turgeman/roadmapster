from pydantic import BaseModel
from typing import List, Literal


class RoadmapResource(BaseModel):
    name: str
    url: str


class RoadmapNode(BaseModel):
    id: str
    title: str
    description: str
    resources: List[RoadmapResource]
    status: Literal["optional", "required"]
    prerequisites: List[str]
