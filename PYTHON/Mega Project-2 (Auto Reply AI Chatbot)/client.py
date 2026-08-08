from groq import Groq

# Initialize the client
client = Groq(api_key="GROQ_API_KEY")

# Chat history
command = """
[15:40, 07/08/2026] MOHAMMED AFFAN: Movie nakko ree
[15:40, 07/08/2026] *M_B_M*: Jainge re meku mlm teku nai aari english magar subtitles rehte tension mat le
[15:41, 07/08/2026] *M_B_M*: Roz roz thodi na jate re bhai apne,apne ku konsa bhejte bolke bgn
[15:42, 07/08/2026] MOHAMMED AFFAN: to movie nakko dusra kuch to bhi
[15:42, 07/08/2026] *M_B_M*: Jainge re bhai
[07/08, 15:42] *M_B_M*: Romantic movie nai hai woh mlm meku
[07/08, 15:42] *M_B_M*: Marvel ki hai
[07/08, 15:44] MOHAMMED AFFAN: marval ki hai isliye ich bolru meku ni smjh me aate woh
[07/08, 15:44] *M_B_M*: Aati new hai ye,puri new story
[07/08, 15:44] *M_B_M*: Jnd ku bhi konsi aati
[07/08, 15:45] *M_B_M*: Bht hype chal ri dekhinge re bhai kya hota
"""

# Generate response
chat = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a person named Affan. "
                "You speak Hindi and English (Hinglish), "
                "you are from India, you are a coder, and you analyze chat history. "
                "Respond exactly like Affan would. and dont like marvel movies but his friend wants to see a movie and  he was convincing affan"
            ),
        },
        {
            "role": "user",
            "content": command,
        },
    ],
)

print(chat.choices[0].message.content)