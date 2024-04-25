from openai import OpenAI

client = OpenAI(api_key="sk-proj-o1mZSJe8uGwPuOGbKrruT3BlbkFJc5udmLK27lvD33AkP5rT") 


def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",  # Assuming GPT-4, adjust model as necessary
        messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                  {"role": "user", "content": prompt}])
        # Correctly extract the content from the response
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("WanderPlanner: ", response)