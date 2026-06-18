car_started = False

print("Type 'help' to see available commands")

while True:
    command = input("> ").lower()

    if command == "start":
        if car_started:
            print("Car is already started.")
        else:
            car_started = True
            print("Car started.")

    elif command == "stop":
        if not car_started:
            print("Car is already stopped.")
        else:
            car_started = False
            print("Car stopped.")

    elif command == "help":
        print(" start - start the car")
        print(" stop  - stop the car")
        print(" quit  - quit the game")

    elif command == "quit":
        print("Exiting....")
        break

    else:
        print("invalid input. type 'help' for commands")
