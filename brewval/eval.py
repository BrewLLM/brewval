from typing import List, Dict

from brewval.model import Prompt, Label

from langchain.llms import OpenAI, BaseLLM

MODELS: Dict[str, BaseLLM] = {
    'OpenAi[davinci-003]': OpenAI(model_name='text-davinci-003'),
    'OpenAi[davinci-002]': OpenAI(model_name='text-davinci-002'),
    'OpenAi[curie-001]': OpenAI(model_name='text-curie-001'),
    'OpenAi[babbage-001]': OpenAI(model_name='text-babbage-001'),
    'OpenAi[ada-001]': OpenAI(model_name='text-ada-001')
}


class Evaluator:

    def evaluate(self, prompt: Prompt, labels: List[Label]) -> None:
        for model in MODELS.keys():
            print(f'Evaluating PROMPT:\n{prompt.template}\nMODEL: {model}')
