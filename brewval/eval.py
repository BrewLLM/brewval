from typing import List, Dict

from brewval.model import Prompt, Label, EvaluationResult

from langchain.llms import OpenAI, BaseLLM

DEFAULT_MODELS: Dict[str, BaseLLM] = {
    'OpenAI[davinci-003]': OpenAI(model_name='text-davinci-003'),
    # 'OpenAI[davinci-002]': OpenAI(model_name='text-davinci-002'),
    # 'OpenAI[curie-001]': OpenAI(model_name='text-curie-001'),
    # 'OpenAI[babbage-001]': OpenAI(model_name='text-babbage-001'),
    'OpenAI[ada-001]': OpenAI(model_name='text-ada-001'),

}


class Evaluator:

    def __init__(self, models=None):
        if models is None:
            models = DEFAULT_MODELS
        self.models = models

    def evaluate(self, prompt: Prompt, labels: List[Label]) -> List[EvaluationResult]:
        results: List[EvaluationResult] = []
        for model in self.models.keys():
            match_count: int = 0
            for label in labels:
                prompt_text = prompt.get_prompt_from_label(label)
                output = self.models[model].generate([prompt_text])
                result = output.generations[0][0].text
                matches = label.result_matches(result)
                if matches:
                    match_count += 1
            results.append(EvaluationResult(model, match_count / len(labels)))

        return results

