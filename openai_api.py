import json
import openai
import certifi
from prompt import start_prompt

certifi.where()

with open("key.txt", "r") as keyfile:
    key = keyfile.read()

openai.api_key = key


def get_gpt_response(full_prompt, model="gpt-3.5-turbo"):
    completions = openai.ChatCompletion.create(
        model=model,
        messages =[{"role": "user", "content": full_prompt}],
        max_tokens=1024,
        n=1,
        temperature=0,
    )

    message = completions["choices"][0]["message"]["content"]
    return message.strip()


def get_opening_times_json(input_sentence):

    full_prompt = start_prompt + input_sentence

    text = get_gpt_response(full_prompt)

    try:
        return json.loads(text)
    except Exception as e:
        if "INSUFFICIENT" not in text.upper():
            print('Failed to parse response', text, e)
        return {}


if __name__ == "__main__":
    print(get_opening_times_json("Mon Sat 1-3pm Sun closed"))