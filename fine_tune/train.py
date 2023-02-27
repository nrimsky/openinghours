"""
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>

You can use your file for fine-tuning:
> openai api fine_tunes.create -t "train_prepared.jsonl"

After you’ve fine-tuned a model, remember that your prompt has to end with the indicator string ` -- JSON format:` for the model to start generating completions, rather than continuing with the prompt. Make sure to include `stop=["]}"]` so that the generated texts ends at the expected place.
Once your model starts training, it'll approximately take 3.95 minutes to train a `curie` model, and less for `ada` and `babbage`. Queue will approximately take half an hour per job ahead of you.


openai api fine_tunes.create -t "train_prepared.jsonl" -m curie

[2023-02-27 22:26:57] Created fine-tune: ft-R7uXcYe7SLoiccKHa4bujmMZ
[2023-02-27 22:34:15] Fine-tune costs $0.17
[2023-02-27 22:34:15] Fine-tune enqueued. Queue number: 0
[2023-02-27 22:34:17] Fine-tune started
[2023-02-27 22:35:41] Completed epoch 1/4
[2023-02-27 22:36:03] Completed epoch 2/4
[2023-02-27 22:36:24] Completed epoch 3/4
[2023-02-27 22:36:46] Completed epoch 4/4
[2023-02-27 22:37:09] Uploaded model: curie:ft-personal-2023-02-27-22-37-09
[2023-02-27 22:37:10] Uploaded result file: file-LKQfRKbvXB75ruW5LlSaAOR6
[2023-02-27 22:37:10] Fine-tune succeeded

Job complete! Status: succeeded 🎉
Try out your fine-tuned model:

openai api completions.create -m curie:ft-personal-2023-02-27-22-37-09 -p <YOUR_PROMPT>
"""

import json
import openai
import certifi
import sys 

sys.path.append("..")
from generate_data.openai_api import get_opening_times_json

certifi.where()

with open("../key.txt", "r") as keyfile:
    key = keyfile.read()

openai.api_key = key


def process_to_jsonl():
    with open("trainingset.json", "r") as jf:
        d = json.load(jf)
        with open("file2.JSONL", "w") as lfile:
            for l in d:
                p = l["prompt"]
                c = l["completion"]
                lfile.write(f'\\"prompt": "{p}", "completion": "{c}"\\ \n')


def use_fine_tuned_model(opening_hours):
    prompt = f"{opening_hours} -- JSON format:"
    completion = openai.Completion.create(
        model="curie:ft-personal-2023-02-27-22-37-09", prompt=prompt, max_tokens=200
    )["choices"][0]["text"]
    return completion


if __name__ == "__main__":
    TEST_CASE = "Monday - Wed 8am to 12pm and 4pm  6pm, Closed Saturday, Sunday 8am to 9pm"
    print("FINETUNED")
    print(use_fine_tuned_model(TEST_CASE))
    print("BASE")
    print(get_opening_times_json(TEST_CASE))
