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
        passengerList = flightschedule.get("response").get("passengerList")
        flightSummary = flightschedule.get("response").get("loadSummary")
        print(flightSummary)
        print(passengerList[0])


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

    def writeCSV(self, data):
        # with open('dict.csv', 'wb') as csv_file:
        #     writer = csv.writer(csv_file)
        #     for key, value in data.items():
        #         writer.writerow([key, value])
        for key, value in data.get("response").items():
            print(key, value)