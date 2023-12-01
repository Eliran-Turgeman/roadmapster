from abc import ABC, abstractmethod
from generation_contract.roadmap_models import Roadmap


class BaseRoadmapGenerator(ABC):
    @abstractmethod
    def generate(self, roadmap_topic: str) -> Roadmap:
        """
        Given a topic, will generate a roadmap in JSON format.
        :param roadmap_topic: topic to generate a roadmap for
        :return: object of type Roadmap
        """
        pass
