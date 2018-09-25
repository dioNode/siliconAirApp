import requests
import json
import csv

class PriorityANN:
    """ANN to use for determining priority listing"""
    def __init__(self):
        print("Initialising...")

    def train(self, api_url):
        azure_cv_endpoint = 'INSERT YOUR ENDPOINT URL HERE'
        azure_cv_key = 'INSERT YOUR KEY HERE'

        flightschedule = self.requestData(
            "https://apigw.singaporeair.com/appchallenge/api/flight/passenger",
            "{ \"flightNo\": \"SQ890\", \"flightDate\": \"2018-07-20\" }"
        )
        self.passengerList = flightschedule.get("response").get("passengerList")
        self.flightSummary = flightschedule.get("response").get("loadSummary")
        for passenger in self.passengerList:
            passenger["willingEvictor"] = True if passenger.get("bookingClass") == "Business" else False

        self.writeCSV("passengerDetails.csv")
        print(self.passengerList)


    def requestData(self, url, payload):
        headers = {
            'content-type': "application/json",
            'apikey': "aghk73f4x5haxeby7z24d2rc",
            'cache-control': "no-cache",
            'postman-token': "53cd8502-4b4b-54d8-c2de-8636e549ba75"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        data = json.loads(response.text)
        return data

    def writeCSV(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = self.passengerList[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for passenger in self.passengerList:
                writer.writerow(passenger)
