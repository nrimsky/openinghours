import json
import openai
import certifi
from prompt import start_prompt

certifi.where()

with open("key.txt", "r") as keyfile:
    key = keyfile.read()

openai.api_key = key


def get_gpt_response(full_prompt, model="code-davinci-002"):
    completions = openai.Completion.create(
        engine=model,
        prompt=full_prompt,
        max_tokens=1024,
        n=1,
        temperature=0,
        stop="}",
    )
    message = completions["choices"][0]["text"]
    message = message.strip()
    if message[-1] != "}":
        message += "}"
    return message.strip()


def get_opening_times_json(input_sentence):
    full_prompt = start_prompt + f"INPUT: {input_sentence}\nOUTPUT:\n"
    text = get_gpt_response(full_prompt)

    try:
        return json.loads(text)
    except Exception as e:
        if "INSUFFICIENT" not in text.upper():
            print("Failed to parse response", text, e)
        return {}


if __name__ == "__main__":
    print(get_opening_times_json("Mon Fri dawn to dusk"))
