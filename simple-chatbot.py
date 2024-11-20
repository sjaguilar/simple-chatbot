import ollama

# Chat loop
print("Chatbot: Hello! Type '/bye' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "/bye":
        print("Chatbot: Goodbye!")
        break

    # Generate response
    response = ollama.chat(
        model='dolphin-llama3:8b',
        messages=[
            {'role': 'user', 'content': user_input}
        ]
    )
    print(f"Chatbot: {response['message']['content']}")
