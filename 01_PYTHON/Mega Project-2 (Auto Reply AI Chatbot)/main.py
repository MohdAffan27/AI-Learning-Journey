import pyautogui
import pyperclip
import time
from groq import Groq

# Initializing Groq ai

client = Groq(api_key="GROQ_API_KEY")


def is_last_message_from_sender(chat_log, sender_name1="_M_B_M_", sender_name2="jnd"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2026]")[-1]

    if sender_name1 in messages:
        return True
    elif sender_name2 in messages:
        return True
    else:
        return False

# Fail-safe: move mouse to a corner to stop the script

pyautogui.FAILSAFE = True
time.sleep(3) # Time to switch to the target window
pyautogui.click(454, 752)
time.sleep(1)

while True:
    # Clear clipboard first

    pyperclip.copy("")

    # Click the item


    # Select chat_history using explicit mouse down/up

    pyautogui.moveTo(855, 174, duration=0.5)
    pyautogui.mouseDown()

    # Drag slowly

    pyautogui.moveTo(867, 664, duration=1.5)

    pyautogui.mouseUp()
    time.sleep(0.5)

    # Copy

    pyperclip.copy("") # Clear clipboard

    print("You have 3 seconds to manually select some chat_history...")
    time.sleep(3)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    chat_history = pyperclip.paste()
    print(chat_history)
    pyautogui.click(1324, 621)

    # Generate response
    if is_last_message_from_sender(chat_history):
        chat = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                    "You are a person named Affan. You speak Hindi and English (Hinglish), you are from India, you are aa coder, and you analyze chat history. Respond exactly like Affan would in hyderabadi slang. and dont like marvel movies but his friend wants to see a movie and he was convincing affan and dont use timing just a reply and be realistic and complete your scentence in short message, My name is Mohammed Affan. I'm a BTech CSE 3rd-year student in India. I'm focused on becoming an AI/ML Engineer, especially in Python, Deep Learning, LLMs and Computer Vision. I'm currently learning Python and doing a Machine Learning internship at FlyRank.ai. I like building projects, updating GitHub, and improving my LinkedIn/portfolio. I prefer structured daily plans and want honest, practical advice instead of fake motivation."
                    ),
                },

                {
                    "role": "user",
                    "content": chat_history,
                },
            ],
        )

        response = chat.choices[0].message.content

        pyperclip.copy(response)

        pyautogui.click(685, 690)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')