import json
from openai_api import get_opening_times_json
from datetime import datetime
import os

def read_data(json_path):
    with open(json_path, "r") as jf:
        data = json.load(jf)
        return list(set([d["opening_hours"].strip() for d in data if len(d["opening_hours"].strip()) != 0]))
    

def eval(data):
    ans = {}
    for i, d in enumerate(data):
        try:
            r = get_opening_times_json(d)
            print(i)
            ans[d] = r 
        except Exception as e:
            print(f"An exception occurred: {e}, Input: {d}")
    with open(os.path.join("outputs", f'output-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json'), "w") as outfile:
        json.dump(ans, outfile)
    return ans


if __name__ == "__main__":
    data = read_data("Toilet-2023-03-02.json") # len = 560
    eval(data=data[:100])
    eval(data=data[100:200])
    eval(data=data[200:300])
    eval(data=data[300:400])
    eval(data=data[400:500])
    eval(data=data[500:])