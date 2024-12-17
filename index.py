from openai import OpenAI

client = OpenAI()


def chat_with_tutor(prompt: str) -> str:
    """Create conversation with gpt-4o-mini as an Akan Twi tutor."""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an Akan Twi tutor."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=200,
    )
    return completion.choices[0].message.content.strip()


if __name__ == "__main__":
    print("Akwaaba! Let's learn some Twi today! ('exit' to quit)")
    while True:
        student_input = input("You: ")
        if student_input.lower() == "exit":
            break
        completion = chat_with_tutor(student_input)
        print(f"Tutor: {completion}")
