import argparse
import csv
from typing import List

from brewval.model import Prompt, Label
from brewval.eval import Evaluator

parser = argparse.ArgumentParser(description='Evaluate prompts')
parser.add_argument('-l', '--labels')
parser.add_argument('-p', '--prompts')
args = parser.parse_args()


def parse_prompts(csv_file: str) -> List[Prompt]:
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        return [Prompt(row['prompt']) for row in reader]


def parse_labels(csv_file: str) -> List[Label]:
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        return [Label(row['result'], row) for row in reader]


prompts = parse_prompts(args.prompts)
labels = parse_labels(args.labels)
print(f'Loaded {len(prompts)} prompts and {len(labels)} labels. Evaluating...')

evaluator = Evaluator()

for prompt in prompts:
    results = evaluator.evaluate(prompt, labels)
    for result in results:
        print(f'Model {result.model_name} accuracy: {result.accuracy * 100}%')
