start_prompt = """

This is an API that turns unstructured natural language opening hours text into a structured valid JSON format with keys of days of the weeks, values of hours intervals using an HH:MM format. 
If there are different opening times for different times of year, we use the latest opening and earliest closing times found.
If the description is vague, e.g. using terms such as dawn and dusk, we use the most realistic looking HH:MM opening hours given the information.
If there is no information given that could be used to parse opening hours, we return "INSUFFICIENT INFORMATION".
IMPORTANT: "Mon Sat 1-3pm Sun closed" (missing a dash) should be interpreted as "Monday TO Saturday 1 to 3pm, Sunday closed"

Examples of input/output pairs: 
INPUT: "Open weekdays noon to 4 pm, and 8 pm to midnight, and closed on weekends"
OUTPUT:
{
    "Monday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Tuesday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Wednesday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Thursday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Friday": [["12:00", "16:00"], ["20:00", "24:00"]],
    "Saturday": [],
    "Sunday": []
}
INPUT: "Open on wed 11-2 and fri sun 9-6:30"
OUTPUT:
{
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [["11:00", "14:00"]],
    "Thursday": [],
    "Friday": [["09:00", "18:30"]],
    "Saturday": [["09:00", "18:30"]],
    "Sunday": [["09:00", "18:00"]]
}
INPUT: "May-October: 10:00-18:00, November-April: 9.00-17:00"
OUTPUT:
{
    "Monday": [["10:00", "17:00"]],
    "Tuesday": [["10:00", "17:00"]],
    "Wednesday": [["10:00", "17:00"]],
    "Thursday": [["10:00", "17:00"]],
    "Friday": [["10:00", "17:00"]],
    "Saturday": [["10:00", "17:00"]],
    "Sunday": [["10:00", "17:00"]]
}
INPUT: "Open 9-11am and 2-dusk"
OUTPUT:
{
    "Monday": [["09:00", "11:00"], ["14:00", "18:00"]],
    "Tuesday": [["09:00", "11:00"], ["14:00", "18:00"]],
    "Wednesday": [["09:00", "11:00"], ["14:00", "18:00"]],
    "Thursday": [["09:00", "11:00"], ["14:00", "18:00"]],
    "Friday": [["09:00", "11:00"], ["14:00", "18:00"]],
    "Saturday":[["09:00", "11:00"], ["14:00", "18:00"]],
    "Sunday": [["09:00", "11:00"], ["14:00", "18:00"]]
}
INPUT: "Open same times as museum"
OUTPUT:
INSUFFICIENT INFORMATION
INPUT: "Mon Wed Every day from 8:15am 10am then 4pm 9pm, Thur - Sun closed"
OUTPUT:
{
    "Monday": [["08:15", "10:00"], ["16:00", "21:00"]], 
    "Tuesday":  [["08:15", "10:00"], ["16:00", "21:00"]], 
    "Wednesday":  [["08:15", "10:00"], ["16:00", "21:00"]], 
    "Thursday": [], 
    "Friday": [], 
    "Saturday": [], 
    "Sunday": []
}
INPUT: "May-Sept mon sat 1-8pm sun closed; Other times mon sat 1-6:30pm except sun"
OUTPUT:
{
    "Monday": [["13:00", "18:30"]], 
    "Tuesday":  [["13:00", "18:30"]], 
    "Wednesday":  [["13:00", "18:30"]], 
    "Thursday": [["13:00", "18:30"]], 
    "Friday": [["13:00", "18:30"]], 
    "Saturday": [["13:00", "18:30"]], 
    "Sunday": []
}
"""
