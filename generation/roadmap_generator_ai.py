import json

from pydantic import ValidationError

from generation.base_roadmap_generator import BaseRoadmapGenerator
from generation.gpt_utility import GPTUtility
from generation.prompt import PROMPT, TOPIC_PLACEHOLDER
from generation_contract.roadmap_models import Roadmap


class RoadmapGenerator(BaseRoadmapGenerator):
    def generate(self, roadmap_topic: str) -> Roadmap:
        """
        Generates a roadmap objects given the gpt prompt result.
        Given a malformed response, returns an empty roadmap object.
        :param roadmap_topic: topic to generate a roadmap for
        :return: Roadmap object
        """
        roadmap_json = json.loads(GPTUtility.prompt(msg=PROMPT.replace(TOPIC_PLACEHOLDER, roadmap_topic)))
        try:
            return Roadmap(**roadmap_json)
        except ValidationError as e:
            print(f'failed to serialize invalid roadmap, error={e}')

        return Roadmap(nodes=[])
