# This is a simple Python script that interacts with the user by asking for their name and then greeting them. It also maintains a conversation history and generates responses using a language model.
from model import generate_response, choose_tool
from tools import get_current_datetime, calculate

# The script starts by initializing an empty conversation list to keep track of the conversation history. It then prompts the user for their name and greets them. The main conversation loop continues until the user types "quit". For each user message, it checks if the message requires the current date and time using the `should_use_datetime` function. If so, it retrieves the current date and time using `get_current_datetime` and appends it to the conversation. The user's message is then added to the conversation, and a response is generated using the `generate_response` function. The response is also added to the conversation and printed to the console.
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
        
        conversation.append(
            {
                "role": "user",
                "content": f"Tool result: {tool_result}"
            }
        )

    elif decision == "CALCULATOR":
        tool_result = calculate(message)
        
        conversation.append(
            {
                "role": "user",
                "content": f"Tool result: {tool_result}"
            }
        )
    response = generate_response(conversation)

    conversation.append(
        {"role": "assistant", "content": response}
    )
    print(response)

