import openai

openai.api_key = "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"

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = chat_gpt(user_input)
        print("Chatbot:", response)
