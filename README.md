# Natural Language Opening Hours Parsing

## About

- Using OpenAI's GPT3 API to parse natural language opening hours into a structured JSON format
- Use prompt engineering with some examples to produce initial training set (`generate_data`)
- Get humans to weed out correct and incorrect generations, and handwrite correct answers for some incorrect ones using https://github.com/nrimsky/Feedbackr (`use_feedback`)
- Use the final dataset to fine-tune GPT3 using https://beta.openai.com/docs/guides/fine-tuning (`fine_tune`)

## Application

- My first usage for this parser will be to add an open now filter to the Toilets4London app :D
- Am therefore using data from https://github.com/toilets4london/Toilets4LondonAPI to validate and train the parser

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