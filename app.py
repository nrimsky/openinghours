from flask import Flask, request, render_template
from openai_api import get_opening_times_json_codex

app = Flask(__name__)

@app.route('/', methods=['POST'])
def my_api():
    data = request.get_json()
    opening_hours = data["opening_hours"]
    try:
        parsed = get_opening_times_json_codex(opening_hours)
    except Exception as e:
        print(e)
        return {}
    return parsed

@app.route('/demo.html')
def demo():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run()