from abc import abstractmethod, ABC

from generation_contract.roadmap_models import Roadmap


class BaseOutput(ABC):
    def __init__(self, roadmap: Roadmap):
        self.roadmap = roadmap

    @abstractmethod
    def show(self):
        pass
