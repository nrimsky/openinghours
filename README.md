# Natural Language Opening Hours Parsing

## About

- Using OpenAI's `gpt-3.5-turbo` or `code-davinci-002` APIs to parse natural language opening hours into a structured JSON format
- See `prompt.py` for prompts being used
- Also includes a basic flask API that can be run locally with `gunicorn app:app` (see `test.py` for an example request)

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then add your OpenAI API key to a file called `.env` in the root directory of the project

## Credits

Original OpenAI API call code, idea to use GPT3, and original prompt engineering by https://github.com/neilkakkar