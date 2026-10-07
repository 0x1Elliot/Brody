# This is a simple Python script that interacts with the user by asking for their name and then greeting them. It uses a language model to generate responses based on the user's input and can also utilize specific tools for certain tasks, such as retrieving the current date and time or performing calculations.
from model import generate_response, choose_tool
from tools import (
    get_current_datetime,
    calculate,
    calculate_relative_datetime,
    parse_relative_datetime
)

# The script starts by initializing an empty list called `conversation` to keep track of the conversation history. It then prompts the user for their name and greets them. The main conversation loop continues until the user types "quit". Within the loop, the user's message is appended to the conversation, and the `choose_tool` function is called to determine if a specific tool should be used to respond. Depending on the decision, the appropriate tool function is called, and the result is appended to the conversation. Finally, a response is generated using `generate_response`, which is also appended to the conversation and printed to the console.
conversation = []

# This is a simple Python script that interacts with the user by asking for their name and then greeting them.
name = input("What is your name? ")
print("Nice to meet you,", name)


# Main conversation loop
while True:
    message = input("")


    if message.lower() == "quit":
        print("Goodbye!")
        break   

# The user's message is appended to the conversation list with the role of "user". The `generate_response` function is called with the updated conversation, and the model generates a response. The response is then appended to the conversation list with the role of "assistant" and printed to the console.
    conversation.append(
        {"role": "user", "content": message}
    )

# The `choose_tool` function is called with the user's message to determine if a specific tool should be used to respond. If the decision is "DATETIME", the current date and time is retrieved using `get_current_datetime`, and the result is appended to the conversation. If the decision is "CALCULATOR", the `calculate` function is called with the user's message, and the result is appended to the conversation. Finally, a response is generated using `generate_response`, and it is appended to the conversation and printed to the console.
    decision = choose_tool(message)

    if decision == "DATETIME":
        tool_result = get_current_datetime()

        response = tool_result

        conversation.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        print(response)
        continue

    elif decision == "RELATIVE_DATETIME":
        offsets = parse_relative_datetime(message)

        tool_result = calculate_relative_datetime(
            years=offsets["years"],
            days=offsets["days"],
            hours=offsets["hours"],
            minutes=offsets["minutes"]
        )

        response = tool_result

        conversation.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        print(response)
        continue

    elif decision == "CALCULATOR":
        tool_result = calculate(message)

        response = tool_result
        
        conversation.append(
            {
                "role": "assistant",
                "content": response
            }
        )
    response = generate_response(conversation)

    conversation.append(
        {"role": "assistant", "content": response}
    )

    print(response)
    continue

