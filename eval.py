import json
from openai_api import get_opening_times_json
from datetime import datetime

def read_data(json_path):
    with open(json_path, "r") as jf:
        data = json.load(jf)
        return list(set([d["opening_hours"].strip() for d in data if len(d["opening_hours"].strip()) != 0]))
    

def eval(data, n=3):
    ans = {}
    for d in data[:n]:
        r = get_opening_times_json(d)
        ans[d] = r 
    with open(f'output-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json', "w") as outfile:
        json.dump(ans, outfile)
    return ans

        


if __name__ == "__main__":
    eval(read_data("Toilet-2023-03-02.json"))