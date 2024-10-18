import re

# Define time conversion function
def time_to_minutes(time):
    period = time[-2:].upper()
    hours, minutes = map(int, time[:-2].split(":"))
    if period == "PM" and hours != 12:
        hours += 12
    elif period == "AM" and hours == 12:
        hours = 0
    return hours * 60 + minutes

# Input string
# time_string = "Tuesday: 11:30 AM – 2:30 PM, 5:30 – 8:30 PM"

def time_to_window(time):
    print('time: ', time)
    time = time.upper()
    status = time.split(":")[1].strip()
    if status == "CLOSED":
        return (0, 0)
    # Adjust input string to normalize non-breaking spaces or unusual characters

    normalized_time_string = time.replace("\u202F", "").replace("\u2009", "")

    # Extract time ranges using regex
    matches = re.findall(r'(\d{1,2}:\d{2})', normalized_time_string)
    day_time = re.findall(r'(?:AM|PM)', normalized_time_string)

    print(matches)
    print(day_time)

    lower = matches[0] + day_time[0]
    upper = matches[-1] + day_time[-1]

    # Convert times to minutes
    time_windows = [time_to_minutes(match) for match in [lower, upper]]

    # Get the first and last time from the list
    time_window = (time_windows[0], time_windows[-1])
    return time_window


if __name__ == '__main__':


    weekday_text:list = [
            "Monday: Closed",
            "Tuesday: 11:30 AM – 2:30 PM, 5:30 – 8:30 PM",
            "Wednesday: 11:30 AM – 2:30 PM, 5:30 – 8:30 PM",
            "Thursday: 11:30 AM – 2:30 PM, 5:30 – 8:30 PM",
            "Friday: 11:30 AM – 2:30 PM, 5:30 – 8:30 PM",
            "Saturday: 11:30 AM – 2:30 PM, 5:30 – 8:30 PM",
            "Sunday: 11:30 AM – 2:30 PM, 5:30 – 8:30 PM",
            "Sunday: 5:30 – 8:30 PM"
            ]


    for text in weekday_text:
        print(time_to_window(text))

