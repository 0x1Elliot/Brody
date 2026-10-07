# This is a simple Python script that interacts with the user by asking for their name and then greeting them. It uses a language model to generate responses based on the user's input and can also utilize specific tools for certain tasks, such as retrieving the current date and time or performing calculations.
from model import generate_response, choose_tool
from tools import (
    get_current_datetime,
    calculate,
    calculate_relative_datetime,
    parse_relative_datetime
)
from memory import load_memory, save_memory

# The script starts by initializing an empty list called `conversation` to keep track of the conversation history. It then prompts the user for their name and greets them. The main conversation loop continues until the user types "quit". Within the loop, the user's message is appended to the conversation, and the `choose_tool` function is called to determine if a specific tool should be used to respond. Depending on the decision, the appropriate tool function is called, and the result is appended to the conversation. Finally, a response is generated using `generate_response`, which is also appended to the conversation and printed to the console.
conversation = []

# Load memory from the memory.json file. If the file does not exist, an empty dictionary is returned. The memory is used to store information that the assistant can remember during the conversation.
memory = load_memory()

# This is a simple Python script that interacts with the user by asking for their name and then greeting them.
name = input("What is your name? ")
print("Nice to meet you,", name)


# Main conversation loop
while True:
    message = input("")


    if message.lower() == "quit":
        print("Goodbye!")
        break   

    if message.lower().startswith("remember "):
        fact = message[len("remember "):]

        if "facts" not in memory:
            memory["facts"] = []

        memory["facts"].append(fact)
        save_memory(memory)

        print("I will remember that.")
        continue

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

        print(response)
        continue

    model_context = conversation.copy()

    if memory.get("facts"):
        model_context.insert(
            0,
            {
                "role": "system",
                "content": (
                    "Long-term memories about the user:\n"
                    + "\n".join(f"- {fact}" for fact in memory["facts"])
                )
            }
        )

    response = generate_response(model_context)

    conversation.append(
        {"role": "assistant", "content": response}
    )

    print(response)