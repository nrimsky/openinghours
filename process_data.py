from openai_api import get_opening_times_json
import os
import json
import random

PATH = "data"
OUT_PATH = "output"


def process_data():
    for file in os.listdir("data"):
        full_path = os.path.join(PATH, file)
        output_path = os.path.join(OUT_PATH, file)
        print(f"Reading {file}")
        tot = 0
        with open(full_path, "r") as jsonfile:
            data = json.loads(jsonfile.read())
            random.shuffle(data)
            data = data[:15]
            with open(output_path, "w") as outfile:
                outfile.write("{" + f'"name": "{file}", "data": [')
                for item in data:
                    oh = item.get("opening_hours", "").strip()
                    if len(oh) < 1:
                        continue
                    completion = get_opening_times_json(oh)
                    if completion:
                        print("Processed", oh)
                        tot += 1
                        completion = json.dumps(str(f'"{completion}"'))
                        outfile.write('{"prompt":"' + oh + '", "completion":"' + completion[3:-3] + '"},')
                outfile.write("]}")
        print(f"Output written to {output_path}", f"{tot} opening hours processed")


if __name__ == "__main__":
    process_data()
