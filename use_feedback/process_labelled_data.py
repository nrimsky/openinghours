import json


def main(original_data, labelled_data):
    seen_prompts = set()
    correct = []
    incorrect = []
    with open(labelled_data, "r") as jsonfile:
        data = json.loads(jsonfile.read())
        for item in data:
            if item["Prompt"] in seen_prompts:
                continue
            yes = int(item["# Yes"])
            no = int(item["# No"])
            if yes > no:
                seen_prompts.add(item["Prompt"])
                correct.append((item["Prompt"], item["Completion"]))
            elif no > yes:
                seen_prompts.add(item["Prompt"])
                incorrect.append(item["Prompt"])

    with open("correct_outputs.json", "w") as jsonfile:
        data = [{"prompt": p, "completion": c} for p, c in correct]
        json.dump(data, jsonfile)

    with open("mistakes.json", "w") as jsonfile:
        data = [{"prompt": p, "completion": ""} for p in incorrect]
        json.dump(data, jsonfile)

    with open(original_data, "r") as jsonfile:
        prompts = []
        orig_data = json.loads(jsonfile.read())
        for item in orig_data:
            opening_hours = item["opening_hours"]
            if opening_hours not in seen_prompts and len(opening_hours.strip()) != 0:
                prompts.append(item["opening_hours"])
                seen_prompts.add(item["opening_hours"])

    with open("remaining.json", "w") as jsonfile:
        data = [{"prompt": p, "completion": ""} for p in prompts]
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main("../generate_data/data/T4L-data-export-2023-01-29.json", "labelled.json")
