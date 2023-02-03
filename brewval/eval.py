from typing import List, Dict

from brewval.model import Prompt, Label

from langchain.llms import OpenAI, BaseLLM

MODELS: Dict[str, BaseLLM] = {
    'OpenAI[davinci-003]': OpenAI(model_name='text-davinci-003'),
    # 'OpenAI[davinci-002]': OpenAI(model_name='text-davinci-002'),
    # 'OpenAI[curie-001]': OpenAI(model_name='text-curie-001'),
    # 'OpenAI[babbage-001]': OpenAI(model_name='text-babbage-001'),
    'OpenAI[ada-001]': OpenAI(model_name='text-ada-001')
}


class Evaluator:

    def evaluate(self, prompt: Prompt, labels: List[Label]) -> None:
        for model in MODELS.keys():
            print(f'Evaluating PROMPT:\n-----\n{prompt.template}\n-----\nMODEL: {model}')
            match_count: int = 0
            for label in labels:
                prompt_text = prompt.get_prompt_from_label(label)
                output = MODELS[model].generate([prompt_text])
                result = output.generations[0][0].text
                matches = label.result_matches(result)
                print(f'Predicted result "{result}" matches expected "{label.result}": {matches}')
                if matches:
                    match_count += 1
            print(f'Model {model} precision: {100.0 * match_count / len(labels)}%')

