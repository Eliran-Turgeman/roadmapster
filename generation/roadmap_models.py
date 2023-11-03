from pydantic import BaseModel, model_validator
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


class Roadmap(BaseModel):
    nodes: List[RoadmapNode]

    @model_validator(mode='after')
    def check_node_prerequisites_exist_in_node_ids(self) -> 'Roadmap':
        all_node_ids = [node.id for node in self.nodes]
        for node in self.nodes:
            for prerequisite in node.prerequisites:
                if prerequisite not in all_node_ids:
                    raise ValueError(f'prerequisite {prerequisite} does not exist in the roadmap')
        return self
