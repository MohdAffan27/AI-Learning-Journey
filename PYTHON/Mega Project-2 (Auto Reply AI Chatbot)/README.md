🤖 Auto Reply AI Chatbot with Python

An experimental AI-powered auto-reply chatbot built with Python that reads recent chat history from a desktop chat application, analyzes whether the latest message is from a specified sender, generates a natural Hinglish response using Groq's Llama 3.3 70B model, and automatically sends the reply.

«🚧 Project Status: Working Prototype»

✨ Features

- 🤖 AI-generated replies using Groq Llama 3.3 70B
- 💬 Reads chat history directly from the desktop interface
- 👤 Detects whether the latest message is from specific configured senders
- 🧠 Uses a custom AI personality prompt to imitate Affan's communication style
- 🇮🇳 Generates responses in Hinglish with Hyderabadi-style slang
- 📋 Uses clipboard automation to copy chat history and paste generated replies
- 🖱️ Controls the desktop interface using PyAutoGUI
- 🔄 Continuously monitors the chat in a loop
- 🛑 PyAutoGUI fail-safe allows the automation to be stopped by moving the mouse to a screen corner
- ⚡ Automatically sends the generated response

🛠️ Technologies Used

- Python
- Groq API
- Llama 3.3 70B Versatile
- PyAutoGUI — desktop and mouse/keyboard automation
- Pyperclip — clipboard management
- Time — delays and synchronization

🔄 How It Works

Start
  ↓
Initialize Groq AI
  ↓
Open / Focus Chat
  ↓
Select Chat History
  ↓
Copy Chat History
  ↓
Read Clipboard
  ↓
Check Last Message Sender
  ↓
Is message from configured sender?
  ├── No → Continue monitoring
  │
  └── Yes
       ↓
   Send chat history to Groq
       ↓
   Generate Affan-style reply
       ↓
   Copy response to clipboard
       ↓
   Paste into chat
       ↓
   Press Enter
       ↓
   Continue monitoring

🧠 AI Personality

The chatbot is given a system prompt that defines the AI's persona and communication style.

It is instructed to:

- Act as Mohammed Affan
- Use Hindi, English and Hinglish
- Use a natural Hyderabadi conversational style
- Keep replies short and realistic
- Analyze the provided chat history
- Respond according to Affan's stated interests and background
- Handle the specific Marvel movie conversation context

The personality prompt can be customized to create a different communication style or character.

👤 Sender Detection

The function:

is_last_message_from_sender(chat_log, sender_name1="_M_B_M_", sender_name2="jnd")

checks the extracted chat history for the configured sender names.

If either sender is detected in the extracted latest message section, the bot proceeds to generate a reply.

Current configured senders

- "_M_B_M_"
- "jnd"

These can be changed directly in the Python code.

🖥️ Desktop Automation

The project currently uses PyAutoGUI to interact with the chat application.

The automation performs actions such as:

- Moving the mouse
- Selecting chat history
- Clicking the message area
- Copying selected text
- Pasting AI-generated responses
- Pressing Enter to send the message

Because the project relies on screen coordinates, the coordinates may need to be adjusted depending on:

- Screen resolution
- Application window size
- Window position
- Display scaling

📋 Clipboard Workflow

Pyperclip is used as the bridge between the chat application and Python.

Chat input

Chat application
      ↓
Select text
      ↓
Ctrl + C
      ↓
Clipboard
      ↓
Python

AI output

Groq AI
   ↓
Generated response
   ↓
Clipboard
   ↓
Ctrl + V
   ↓
Chat application

🔐 API Key Security

⚠️ Important: Never commit your Groq API key directly to GitHub.

The current code contains an API key directly in the source:

client = Groq(api_key="YOUR_API_KEY")

This should be replaced with an environment variable before publishing the project.

Example:

import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

Then store the key in an environment variable rather than inside the source code.

If an API key has already been exposed publicly, revoke/rotate it immediately.

📦 Installation

1. Clone the repository

git clone https://github.com/MohdAffan27/auto-reply-ai-chatbot.git
cd auto-reply-ai-chatbot

2. Install dependencies

pip install pyautogui pyperclip groq

3. Configure your API key

Set your Groq API key as an environment variable.

4. Configure the chatbot

Update:

- Sender names
- Chat application
- Screen coordinates
- AI personality prompt
- Model configuration

5. Run the program

python auto_reply.py

⚠️ Limitations

This is currently a prototype, so it has several limitations:

- Depends on fixed screen coordinates
- Requires the correct chat window to be open
- Chat history selection is currently partly manual
- Sender detection is relatively simple
- No persistent conversation memory
- No database
- No GUI
- No message deduplication system
- No sophisticated error handling
- Runs continuously until manually stopped
- Requires an active internet connection for Groq API requests

🚀 Future Improvements

Planned improvements could include:

- [ ] Automatic chat-history extraction
- [ ] Better sender/message parsing
- [ ] Prevent duplicate replies
- [ ] Conversation memory
- [ ] Configurable response personality
- [ ] ".env" API-key management
- [ ] Error handling and retry system
- [ ] Response cooldown
- [ ] Multiple chat support
- [ ] Web-based or desktop GUI
- [ ] Message logging
- [ ] AI response preview before sending
- [ ] Configurable target contacts
- [ ] Better automation without fixed screen coordinates

🎯 Learning Objectives

This project was built to practice:

- Python programming
- API integration
- LLM integration
- Prompt engineering
- Desktop automation
- Clipboard automation
- Chat history processing
- Conditional logic
- Infinite loops
- Exception-safe automation concepts
- Building practical AI applications

📌 Project Type

Mega Project 2 — Auto Reply AI Chatbot

This project combines Python + LLM API + desktop automation to create a practical AI assistant capable of analyzing chat context and automatically responding in a personalized communication style.

⚠️ Responsible Use

Use this project only with chats and accounts where you have permission to automate interactions. Automated messages should not be used for spam, impersonation, harassment, or misleading people.

---

👨‍💻 Author

Mohammed Affan

BTech CSE — 3rd Year
Aspiring AI/ML Engineer

Focus Areas: Python • Machine Learning • Deep Learning • LLM Applications • Computer Vision

---

⭐ If you found this project interesting, consider giving the repository a star!