# This is a simple example of how to use the SmolLM2-360M-Instruct model to generate a response based on a user prompt. The model is loaded using the `load` function from the `mlx_lm` library, and the tokenizer is used to format the input messages into a prompt suitable for the model. The `generate` function is then called to produce a response, which is printed to the console.
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/SmolLM2-360M-Instruct")


def generate_response(message):
    messages = [
        {"role": "system", "content": "Give clear, accurate, detailed answers. Explain important ideas in several complete sentences. If you don't know the answer, simply say 'I don't know'."},
        {"role": "user",
         "content": message
         }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=500
    )

    return response