from urllib.request import urlopen
import pandas as pd
import json
import os
import sys

#expected to be passed in from main
year = sys.argv[1]

# Get the past data from the API, farthest record is 2023
response = urlopen(f'https://api.openf1.org/v1/meetings?year={year}')
data = json.loads(response.read().decode('utf-8'))
print(data)
df = pd.DataFrame(data)

# Save the data to a JSON file
filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', f'{year}.json'))
if not os.path.exists(filename):
    with open(filename, 'w') as file:
        json.dump(data, file)