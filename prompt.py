start_prompt = """

We want to be an API that turns unstructured natural language opening hours text into a structured valid JSON format with keys of days of the weeks, values of hours intervals using an HH:MM format. 
If there are different opening times for different times of year, use the latest opening and earliest closing times found.
If the description is vague, use realistic looking opening hours given the information.
If there is no information given that could be used to parse opening hours, return "INSUFFICIENT INFORMATION".

Here are some examples: 

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

"Open same times as museum" should return
INSUFFICIENT INFORMATION

"Mon Wed Every day from 8am 10am then 4pm 9pm, Thur - Sun closed" should return
{
    "Monday": [["08:00", "10:00"], ["16:00", "21:00"]], 
    "Tuesday":  [["08:00", "10:00"], ["16:00", "21:00"]], 
    "Wednesday":  [["08:00", "10:00"], ["16:00", "21:00"]], 
    "Thursday": [], 
    "Friday": [], 
    "Saturday": [], 
    "Sunday": []
}

Now convert the input below into the valid JSON format:

"""