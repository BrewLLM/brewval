# Evaluate prompts for LLM applications

In the era of multiple Large Language Model providers and models which differ in capabilities, 
speed, and costs where is a need to evaluate prompts on different providers and models to 
choose the most suitable combination for given task.

## Example

```python
from typing import Dict
from brewval.model import Prompt, Label
from brewval.eval import Evaluator

from langchain.llms import OpenAI, BaseLLM

prompt = Prompt("""
Description: Feelings of disappointment, grief, hopelessness, disinterest, and dampened mood.
Emotion: sadness
Description: muscles become tense, your heart rate and respiration increase, and your mind becomes more alert, priming your body to either run from the danger or stand and fight
Emotion: fear
Description: {description}
Emotion: {result}""")

labels = [
    Label('fear', {'description': 'heart rate and respiration increase'}),
    Label('surprise', {'description': 'quite brief and is characterized by a physiological startle response following something unexpected'}),
    Label('anger', {'description': 'Characterized by feelings of hostility, agitation, frustration, and antagonism towards others.'})
]

models: Dict[str, BaseLLM] = {
    'OpenAI[davinci-003]': OpenAI(model_name='text-davinci-003'),
    'OpenAI[davinci-002]': OpenAI(model_name='text-davinci-002'),
    'OpenAI[ada-001]': OpenAI(model_name='text-ada-001')
}

evaluator = Evaluator(models)

results = evaluator.evaluate(prompt, labels)
for result in results:
    print(f'Model {result.model_name} accuracy: {result.accuracy * 100}%')
```
Outputs
```text
Model OpenAI[davinci-003] accuracy: 100.0%
Model OpenAI[davinci-002] accuracy: 33.3%
Model OpenAI[ada-001] accuracy: 0.0%
```

## Setup

Install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

```commandline
poetry install
```
```commandline
export OPENAI_API_KEY="your key"
```

## Evaluation

Command line, using data from CSV files:

```commandline
poetry run python3 -m brewval.cli -p examples/weather-umbrella/prompts.csv -l examples/weather-umbrella/labels.csv
```

Jupyter Notebook (docs/examples/evaluation.ipynb):

```commandline
poetry run jupyter notebook
```