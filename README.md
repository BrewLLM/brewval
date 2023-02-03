# brewval

## Setup

 - Install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
 - `poetry install`
 - `export OPENAI_API_KEY="your key"`

## Evaluation

```commandline
poetry run python3 -m brewval.cli -p examples/weather-umbrella/prompts.csv -l examples/weather-umbrella/labels.csv
```