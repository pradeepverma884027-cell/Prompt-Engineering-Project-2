# prompt_loader.py

import os


def load_prompt(filename):

    base_path = os.path.dirname(os.path.dirname(__file__))

    prompt_path = os.path.join(
        base_path,
        "prompts",
        filename
    )

    try:
        with open(prompt_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return f"Prompt file '{filename}' not found."
