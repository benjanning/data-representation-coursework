# Import requests and json libraries
import requests
import json

# Define the URL for the dataset
URL = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Get the response from the URL
response = requests.get(URL)

# Check if the response is successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    # Open a file called cso.json in write mode
    with open("cso.json", "w") as f:
        # Write the JSON data to the file
        json.dump(data, f)
    # Print a success message
    print("The dataset has been saved to cso.json")
else:
    # Print an error message
    print("The request failed with status code", response.status_code)
