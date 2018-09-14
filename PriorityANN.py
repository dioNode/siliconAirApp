import requests
import json

FLIGHT_ROUTE_STATUS = "https://cdn.fs.agorize.com/yHrjo4lSPmvLD6DMe9wv"


class PriorityANN:
    """ANN to use for determining priority listing"""
    def __init__(self):
        print("Initialising...")

    def train(self, api_url):
        print("Training on "+api_url)

        flightSchedule = self.requestData("flightschedule")
        print(flightSchedule)



    def requestData(self, parameter):
        headers = {"content-type": "application/json",
                   "apikey": "aghk73f4x5haxeby7z24d2rc"}
        parameters = {"/"+parameter: None}

        # Make a get request to get the latest position of the international space station from the opennotify api.
        response = requests.get(FLIGHT_ROUTE_STATUS, headers=headers, params=parameters)

        # Print the status code of the response.
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return {}