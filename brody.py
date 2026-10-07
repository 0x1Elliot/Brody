from model import generate_response


# This is a simple Python script that interacts with the user by asking for their name and then greeting them.
name = input("What is your name? ")
print("Nice to meet you,", name)


# Main conversation loop
while True:
    message = input("")

    if message.lower() == "quit":
        print("Goodbye!")
        break   
    response = generate_response(message)
    print(response)

