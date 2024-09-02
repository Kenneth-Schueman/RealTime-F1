import os
import json

year = input("Enter the year you are searching for.\nNote: The farthest available data is 2023.\nYear: ")

# Check if the file in pastRaces/data exists with the year name
data_file = os.path.join("pastRaces", "data", f"{year}.json")
if not os.path.isfile(data_file):
     # Construct the path to the getMeetings file
    getMeetings = os.path.join("pastRaces", "getMeetings.py")
    # Execute the getMeetings file with the year as an argument
    os.system(f"python {getMeetings} {year}")
    
# Parse the data_file
with open(data_file, 'r') as file:
    data = json.load(file)

# Print the location tag
for i, meeting in enumerate(data, start=1):
    print(f"{i}. {meeting['meeting_name']}: {meeting['location']}, {meeting['country_name']} ({meeting['date_start']})")

selectedMeeting = input("\nPlease select a meeting to display the details. (Example: 1)\nSelection: ")
# Construct the path to the displayMeetings file
displayMeetings = os.path.join("displayMeeting", "displayMeeting.py")