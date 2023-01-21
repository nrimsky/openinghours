
import os
import json
import openai

with open("key.txt", "r") as keyfile:
    key = keyfile.read()

openai.api_key = key

def generate_text(prompt, model = "text-davinci-003"):
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

    print(input_sentence)

    prompt = """

We want to be an API that turns natural language opening hours text into JSON with keys of days of the week, and values of an array of opening and closing times in HH:MM format. This will be used as data for an open now filter feature in an app. 

For example,

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

For another example, "The store is open from 9am to 5pm on weekdays and from 10am to 2pm on weekends." should return

{
    "Monday": [["09:00", "17:00"]],
    "Tuesday": [["09:00", "17:00"]],
    "Wednesday": [["09:00", "17:00"]],
    "Thursday": [["09:00", "17:00"]],
    "Friday": [["09:00", "17:00"]],
    "Saturday": [["10:00", "14:00"]],
    "Sunday": [["10:00", "14:00"]]
}

And another example, "Open on wed 11-2 and fri-sun 9-6:30" should return

{
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [["11:00", "14:00"]],
    "Thursday": [],
    "Friday": [["09:00", "18:30"]],
    "Saturday": [["09:00", "18:30"]],
    "Sunday": [["09:00", "18:00"]]
}

If it is unclear which set of opening hours to apply, for example if the input is "May-October: 10:00-18:00, November-April: 9.00-17:00", default to the hours when the facility is definitely open (latest open and earliest close):

{
    "Monday": [["10:00", "17:00"]],
    "Tuesday": [["10:00", "17:00"]],
    "Wednesday": [["10:00", "17:00"]],
    "Thursday": [["10:00", "17:00"]],
    "Friday": [["10:00", "17:00"]],
    "Saturday": [["10:00", "17:00"]],
    "Sunday": [["10:00", "17:00"]]
}

Now convert the sentence below into valid JSON:

"""

    full_prompt = prompt + input_sentence

    text = generate_text(full_prompt)

    try:
        return json.loads(text)
    except:
        print('Failed to parse response as json', text)
    
    return None
    

print(get_opening_times_json("1st April - 31st October: 9:00-18:00, 1st November - 31st March: 9.00-17:00"))


