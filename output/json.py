from output.base_output import BaseOutput


class JsonOutput(BaseOutput):
    def show(self):
        print(self.roadmap.model_dump_json(indent=2))
