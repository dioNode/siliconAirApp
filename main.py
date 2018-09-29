from PriorityANN import PriorityANN

def main():
    priorityANN = PriorityANN()
    while True:
        command = input("What would you like to do?\n [C = Build CSV from current flights to train] \n [E = Evict passengers from flight] \n")
        if command.upper() == "C":
            print("Generating CSV")
            generateCSVModel(priorityANN)
            print("CSV generated and stored in passengerDetails.csv")
        elif command.upper() == "E":
            showFlightEvictors(priorityANN)
        else:
            print("Sorry that is not an option")

    priorityANN.setFlight("SQ890")
    priorityANN.evaluate("SQ890")

def generateCSVModel(priorityANN):
    priorityANN.setFlight("SQ890")
    priorityANN.writeCSV("passengerDetails.csv")

def showFlightEvictors(priorityANN):
    flightNo = input("Which flight would you like to select? \n The available flights are [SQ890]\n").upper()
    while flightNo not in ["SQ890"]:
        print("Sorry, flight "+ flightNo + " does not exist.")
        flightNo = input("Which flight would you like to select? \n The available flights are [SQ890]\n")
    priorityANN.evaluate(flightNo)

if __name__ == "__main__":
    main()