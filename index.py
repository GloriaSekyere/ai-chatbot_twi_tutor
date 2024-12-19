from openai import OpenAI

client = OpenAI()


def chat_with_tutor(prompt: str) -> str:
    """Create conversation with gpt-4o-mini as an Asante Twi tutor."""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a native Asante Twi tutor."},
            {"role": "user", "content": prompt},
        ],
    )
    return completion.choices[0].message.content.strip()


if __name__ == "__main__":
    print(
        "Akwaaba! Let's learn how to order food. (Enter 'exit' to quit.)\n"
        "Example:\n"
        "\tHow do you ask: Do you sell tomatoes?\n"
        "\tTranslation: Wo tɔn ntosi?\n"
    )
    while True:
        question: str = input("How do you ask: ")
        if question.lower() == "exit":
            break
        response: str = chat_with_tutor(question)
        print(f"Translation: {response}")
