import requests
import json
import csv
import urllib

class PriorityANN:
    """ANN to use for determining priority listing"""
    def __init__(self):
        print("Initialising...")
        self.desiredParameters = ['firstName', 'lastName', 'bookingClass', 'email', 'checkInStatus', 'willingEvictor']
        self.passengerList = []

    def setFlight(self, flightNo):
        self.passengerList = self._getPassengerDetails(flightNo)
        self.writeCSV("passengerDetails.csv")

    def train(self, api_url):
        # do nothing
        print("nothing")


    def evaluate(self):
        data = {

            "Inputs": {

                "input1":
                    {
                        "ColumnNames": ["firstName", "lastName", "bookingClass", "KFTier", "email", "checkInStatus",
                                        "willingEvictor"],
                        "Values": [["Dion", "Lao", "Business", "EGTP", "dion_lao@hotmail.com", "Checked In", "0"],
                                   ["Hello", "Mate", "Economy", "EGTP", "coolios@hotmail.com", "Checked In", "0"], ]
                    }, },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/8334317b4f7a4e8ba1058977846f6f84/services/1594f6de0f8c42abbd0ce53bcf9a712f/execute?api-version=2.0&details=true'
        api_key = '42zafbAj/h0j6xwLp6hiEgllwnm4S4LtNKwI9FmyQoHTN0pUEKQQOYeAkb+1N2c+i65bLR6con1LjtYUdDNzBQ=='
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)

            # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            # req = urllib.request.Request(url, body, headers)
            # response = urllib.request.urlopen(req)

            result = response.read()
            print(result)
        except urllib.error.HTTPError:
            print("The request failed with status code: ")


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

    def _getPassengerDetails(self, flightNo):
        flightschedule = self.requestData(
            "https://apigw.singaporeair.com/appchallenge/api/flight/passenger",
            "{ \"flightNo\": \""+flightNo+"\", \"flightDate\": \"2018-07-20\" }"
        )
        passengerList = flightschedule.get("response").get("passengerList")
        flightSummary = flightschedule.get("response").get("loadSummary")
        for passenger in passengerList:
            passenger["willingEvictor"] = False if passenger.get("bookingClass") == "Business" else True

        return passengerList

    def _getBaggageDetails(self):

        url = "https://apigw.singaporeair.com/appchallenge/api/flightroutestatus"

        payload = "{\"originAirportCode\": \"SIN\", \"destinationAirportCode\": \"DXB\", \"scheduledDepartureDate\": \"2018-08-15\"}"
        headers = {
            'content-type': "application/json",
            'apikey': "aghk73f4x5haxeby7z24d2rc",
            'cache-control': "no-cache",
            'postman-token': "9a6ab98c-9f7f-cf6d-d081-100676469fad"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        return response.text

