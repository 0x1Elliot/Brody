# This is a simple example of how to use the SmolLM2-360M-Instruct model to generate a response based on a user prompt. The model is loaded using the `load` function from the `mlx_lm` library, and the tokenizer is used to format the input messages into a prompt suitable for the model. The `generate` function is then called to produce a response, which is printed to the console.
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Qwen2.5-1.5B-Instruct-4bit")


def generate_response(conversation):
    messages = [
        {"role": "system",
         "content": (
            "You are a helpful assistant. Use the conversation history to answer questions. "
            "Remember facts the user tells you during the conversation. "
            "Do not invent remembered facts. "
            "If the answer appears earlier in the conversation, use that information. "
            "Keep answers clear and concise unless the user asks for detail."
         )
         },
    ] + conversation

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
# The `generate_response` function takes a conversation history as input, formats it into a prompt using the tokenizer, and then generates a response using the loaded model. The response is returned to be used in the main conversation loop in `brody.py`.
    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=200
    )

    return response


# The 'choose_tool' function takes a user message as input and determines which tool (if any) should be used to respond to the message. It formats the input message into a prompt using the tokenizer and generates a decision using the loaded model. The decision is returned as a string, which can be "NO_TOOL", "DATETIME", or "CALCULATOR".
def choose_tool(message):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a tool router."
                "Do not answer the user's question."

                "Return exactly one of these labels and nothing else:\n"
                "DATETIME - if the user is asking for the current date and time.\n"
                "CALCULATOR - if the user is asking to perform a calculation.\n"
                "NO_TOOL - if the user is asking a question that does not require a tool.\n\n"

                "Examples:\n"
                "User: What time is it? -> DATETIME\n"
                "User: What is today's date? -> DATETIME\n"
                "User: 25 * 150 -> CALCULATOR\n"
                "User: What is 400 divided bty 4.5? -> CALCULATOR\n"
                "User: What is the capital of France? -> NO_TOOL\n"
                "User: Who is the president of the United States? -> NO_TOOL\n"
                "User: Tell me about wolves. -> NO_TOOL\n"

                "Return the label only."
            )
        },
        {
            "role": "user",
            "content": message
        }
    ]


    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    decision = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=5
    )

    return decision.strip()