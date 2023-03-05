import json
import openai
import certifi
from prompt import MESSAGES, CODEX_PROMPT
from dotenv import load_dotenv
import os

certifi.where()
load_dotenv()

openai.api_key = os.environ.get("OPENAI_KEY")

def get_gpt_response_chat(full_prompt, model="gpt-3.5-turbo"):
    completions = openai.ChatCompletion.create(
        model=model,
        messages=full_prompt,
        max_tokens=1024,
        n=1,
        temperature=0,
    )

    message = completions["choices"][-1]["message"]["content"]
    return message.strip()

def get_gpt_response_codex(full_prompt, model="code-davinci-002"):
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


def get_opening_times_json_chat(input_sentence):
    full_prompt = [m for m in MESSAGES]
    full_prompt.append({"role": "user", "content": input_sentence})
    text = get_gpt_response_chat(full_prompt)

    try:
        return json.loads(text)
    except Exception as e:
        if "INSUFFICIENT" not in text.upper():
            print("Failed to parse response", text, e)
        return {}

def get_opening_times_json_codex(input_sentence):
    full_prompt = CODEX_PROMPT + f"INPUT: {input_sentence}\nOUTPUT:\n"
    text = get_gpt_response_codex(full_prompt)

    try:
        return json.loads(text)
    except Exception as e:
        if "INSUFFICIENT" not in text.upper():
            print("Failed to parse response", text, e)
        return {}

if __name__ == "__main__":
    print(get_opening_times_json_chat("Hours: 9am-8pm Days open: Mon, Tue, Wed, Thur, Fri, Sat"))
    print(get_opening_times_json_codex("Hours: 9am-8pm Days open: Mon, Tue, Wed, Thur, Fri, Sat"))
