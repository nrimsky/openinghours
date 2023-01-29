# Natural Language Opening Hours Parsing

## About

- Using OpenAI's GPT3 API to parse natural language opening hours into a structured JSON format
- First attempt simply involved using a good prompt with some examples
- Currently working on generating a training dataset to finetune GPT3 via https://beta.openai.com/docs/guides/fine-tuning
- Am working on a UI project (https://github.com/nrimsky/Feedbackr) to make it easier to collect accurate training data for this


## Usage instructions

1. Create a virtual environment
```
python -m venv env
```

2. Activate the virtual environment
```
source env/bin/activate
```

3. Install the requirements
```
pip install -r requirements.txt
```

4. Get your API key from OpenAI and create a `key.txt` file in the root directory with that API key

5. Run the application
```
python server.py
```

## Application

- My first usage for this parser will be to add an open now filter to the Toilets4London app :D
- Am therefore using data from https://github.com/toilets4london/Toilets4LondonAPI to validate the parser (see `data/`)

## Example output

```json
{
  "name": "test_data.json",
  "data": [
    {
      "prompt": "9am-8pm weekdays, 8:30am-5pm weekends",
      "completion": "{'Monday': [['09:00', '20:00']], 'Tuesday': [['09:00', '20:00']], 'Wednesday': [['09:00', '20:00']], 'Thursday': [['09:00', '20:00']], 'Friday': [['09:00', '20:00']], 'Saturday': [['08:30', '17:00']], 'Sunday': [['08:30', '17:00']]}"
    }
  ]
}
```

## Credits

- Original OpenAI API call code, idea to use GPT3, and prompt engineering by https://github.com/neilkakkar