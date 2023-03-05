from flask import Flask, request
from openai_api import get_opening_times_json_codex

app = Flask(__name__)

@app.route('/', methods=['POST'])
def my_api():
    data = request.get_json()
    opening_hours = data["opening_hours"]
    parsed = get_opening_times_json_codex(opening_hours)
    return parsed

if __name__ == '__main__':
    app.run()