def convert_time_windows(time_windows):
    # Define a function to convert time to minutes
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    # Define a dictionary to hold the converted values
    converted = {}

    base_time, _ = map(time_to_minutes, time_windows['Depot'])

    for location, time_window in time_windows.items():
        start_time, end_time = time_window
        start_minutes = time_to_minutes(start_time)
        end_minutes = time_to_minutes(end_time) 
        converted[location] = (start_minutes - base_time, end_minutes - base_time)

    return converted

# Define the time windows
time_windows = {
    "Depot": ("4:30", "9:30"),
    "Loc1": ("5:00", "9:00"),
    "Loc2": ("5:00", "7:00"),
    "Loc3": ("5:00", "7:00"),  # Assuming Loc3 was meant to be Loc2 again
    "Loc4": ("5:00", "6:00")
}

# Convert the time windows
converted_time_windows = convert_time_windows(time_windows)

# Display the result
for location, (start, duration) in converted_time_windows.items():
    print(f"{location}: ({start}, {duration})")
