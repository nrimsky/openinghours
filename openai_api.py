import json
import openai
import certifi

certifi.where()

with open("key.txt", "r") as keyfile:
    key = keyfile.read()

openai.api_key = key


def generate_text(prompt, model="text-davinci-003"):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()


def get_opening_times_json(input_sentence):

    prompt = """

We want to be an API that turns unstructured natural language opening hours text into a structured valid JSON format with keys of days of the weeks, values of hours intervals using an HH:MM format. Here are some examples: 

"Open weekdays noon to 4 pm, and 8 pm to midnight, and closed on weekends" should return
{
    "Monday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Tuesday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Wednesday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Thursday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Friday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Saturday": [],
    "Sunday": []
}

"The store is open from 9am to 5pm on weekdays and from 10am to 2pm on weekends." should return
{
    "Monday": [["09:00", "17:00"]],
    "Tuesday": [["09:00", "17:00"]],
    "Wednesday": [["09:00", "17:00"]],
    "Thursday": [["09:00", "17:00"]],
    "Friday": [["09:00", "17:00"]],
    "Saturday": [["10:00", "14:00"]],
    "Sunday": [["10:00", "14:00"]]
}

"Open on wed 11-2 and fri-sun 9-6:30" should return
{
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [["11:00", "14:00"]],
    "Thursday": [],
    "Friday": [["09:00", "18:30"]],
    "Saturday": [["09:00", "18:30"]],
    "Sunday": [["09:00", "18:00"]]
}

"May-October: 10:00-18:00, November-April: 9.00-17:00" should use the latest opening and earliest closing and return
{
    "Monday": [["10:00", "17:00"]],
    "Tuesday": [["10:00", "17:00"]],
    "Wednesday": [["10:00", "17:00"]],
    "Thursday": [["10:00", "17:00"]],
    "Friday": [["10:00", "17:00"]],
    "Saturday": [["10:00", "17:00"]],
    "Sunday": [["10:00", "17:00"]]
}

"Open 9-11am and 2-7pm" should return
{
    "Monday": [["09:00", "11:00"], ["14:00", "19:00"]],
    "Tuesday": [["09:00", "11:00"], ["14:00", "19:00"]],
    "Wednesday": [["09:00", "11:00"], ["14:00", "19:00"]],
    "Thursday": [["09:00", "11:00"], ["14:00", "19:00"]],
    "Friday": [["09:00", "11:00"], ["14:00", "19:00"]],
    "Saturday":[["09:00", "11:00"], ["14:00", "19:00"]],
    "Sunday": [["09:00", "11:00"], ["14:00", "19:00"]]
}

Now convert the input below into the valid JSON format:

"""

    full_prompt = prompt + input_sentence

    text = generate_text(full_prompt)

    try:
        return json.loads(text)
    except Exception as e:
        print('Failed to parse response as json', text, e)

    return None


if __name__ == "__main__":
    print(get_opening_times_json("Monday to Friday Midday to 2.30pm, 6pm to 10.30pm, Saturday: 6pm to 11pm, Sunday: 12pm to 10.30pm"))