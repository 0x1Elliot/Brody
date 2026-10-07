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


def should_use_datetime(message):
    messages = [
        {
            "role": "system",
            "content": (
                "Decide whether the user's message requires the current real-world date and/or time."
                "Respond with exactly USE_DATETIME or NO_TOOL."
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
        max_tokens=10
    )

    return decision.strip()