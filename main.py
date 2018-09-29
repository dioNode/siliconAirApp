from PriorityANN import PriorityANN

def main():
    priorityANN = PriorityANN()
    # while True:
    #     flightNo = input("Flight No: ")
    #     print("Setting flight No "+flightNo+"...")
    priorityANN.setFlight("SQ890")
    print(priorityANN.passengerList)
    priorityANN.evaluate()


if __name__ == "__main__":
    main()