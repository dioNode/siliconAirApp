import requests
import json

FLIGHT_ROUTE_STATUS = "https://cdn.fs.agorize.com/yHrjo4lSPmvLD6DMe9wv"

trainInput = [["firstName", "lastName", "passengerType", 3, "cabinClass"],
              ["Dion", "Lao", "Infant", 2, "Business"]]

trainOutput = [1, 0]


class PriorityANN:
    """ANN to use for determining priority listing"""
    def __init__(self):
        print("Initialising...")

    def train(self, api_url):
        print("Training on "+api_url)
        azure_cv_endpoint = 'INSERT YOUR ENDPOINT URL HERE'
        azure_cv_key = 'INSERT YOUR KEY HERE'

        flightschedule = self.requestData("/flightschedule")
        print(flightschedule)


    def requestData(self, parameter):
        headers = {"content-type": "application/json",
                   "apikey": "aghk73f4x5haxeby7z24d2rc"}

        # Make a get request to get the latest position of the international space station from the opennotify api.
        response = requests.get(FLIGHT_ROUTE_STATUS+parameter, headers=headers)

        # Print the status code of the response.
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return {}
