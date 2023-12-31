from typing import List

from pydantic import BaseModel, model_validator

from generation.roadmap_models import RoadmapNode


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
