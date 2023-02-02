from typing import Dict


class Prompt:

    def __init__(self, template: str):
        self.template = template

    def get_prompt(self, inputs: Dict[str, str]) -> str:

        # TODO: Replace inputs and remove result placeholders
        return self.template




class Label:

    def __init__(self, result: str, parameters: Dict[str, str]):
        self.result = result
        self.parameters = parameters
