import re
from typing import Dict, List


class Label:

    # TODO: Would make sense to add max expected tokens to save money

    def __init__(self, result: str, parameters: Dict[str, str]):
        self.result = result
        self.parameters = parameters

    def result_matches(self, result: str) -> bool:
        return self.result == result.strip()


class Prompt:

    def __init__(self, template: str):
        assert template.endswith('{result}')
        self.template = template

    def get_prompt_from_label(self, label: Label) -> str:
        template = self.template.removesuffix('{result}').strip()
        placeholders = re.findall(r'(?<=\{)\w+(?=\})', template)
        for placeholder in placeholders:
            value = label.parameters[placeholder]
            template = template.replace('{' + placeholder + '}', value)
        return template


class EvaluationResult:

    def __init__(self, model_name: str, accuracy: float):
        self.accuracy = accuracy
        self.model_name = model_name
