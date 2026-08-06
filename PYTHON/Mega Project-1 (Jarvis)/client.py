from groq import Groq

def aiprocess(command):
    client = Groq(api_key="YOUR_API_KEY")

    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": command
            }
        ]
    )

    print(chat.choices[0].message.content)




