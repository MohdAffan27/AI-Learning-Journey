# Jarvis - AI Voice Assistant 🤖🎙️

An AI-powered voice assistant built with **Python** that can recognize voice commands, open websites, play music, fetch the latest news, and answer general questions using the **Groq Llama 3.3-70B** language model.

---

## ✨ Features

* 🎤 Voice activation using the wake word **"Jarvis"**
* 🌐 Open popular websites

  * Google
  * YouTube
  * Instagram
  * Facebook
* 🎵 Play songs from a custom music library
* 📰 Read the latest news headlines using **NewsAPI**
* 🤖 AI-powered conversations using **Groq Llama 3.3-70B**
* 🔊 Text-to-Speech responses using **pyttsx3**
* 🎙️ Speech Recognition using Google's Speech Recognition API

---

## 🛠️ Technologies Used

* Python 3.x
* SpeechRecognition
* PyAudio
* pyttsx3
* Groq API
* Requests
* NewsAPI
* Webbrowser

---

## 📂 Project Structure

```
Jarvis/
│
├── main.py              # Main voice assistant
├── musiclibrary.py      # Dictionary of songs and links
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Jarvis.git

cd Jarvis
```

---

### 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it

Windows

```bash
myenv\Scripts\activate
```

Linux/macOS

```bash
source myenv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install SpeechRecognition PyAudio pyttsx3 requests groq
```

---

## 🔑 API Keys

### Groq API

Create a free account and generate an API key.

[https://console.groq.com](https://console.groq.com)

Replace

```python
client = Groq(api_key="YOUR_API_KEY")
```

with

```python
client = Groq(api_key="YOUR_GROQ_API_KEY")
```

---

### NewsAPI

Create a free API key.

[https://newsapi.org/](https://newsapi.org/)

Replace

```python
newsapi = "YOUR_NEWS_API_KEY"
```

with your own key.

---

## 🎵 Music Library

Create a file named

```python
musiclibrary.py
```

Example

```python
music = {
    "believer": "https://youtu.be/7wtfhZwyrcc",
    "shape": "https://youtu.be/JGwWNGJdvx8",
    "faded": "https://youtu.be/60ItHLz5WEA"
}
```

---

## 🚀 Usage

Run

```bash
python main.py
```

Jarvis will start listening for the wake word

```
Jarvis
```

After activation, give your command.

---

## 💬 Supported Commands

| Command            | Action                              |
| ------------------ | ----------------------------------- |
| Jarvis             | Wake the assistant                  |
| Open Google        | Opens Google                        |
| Open YouTube       | Opens YouTube                       |
| Open Instagram     | Opens Instagram                     |
| Open Facebook      | Opens Facebook                      |
| Play Believer      | Plays a song from the music library |
| News               | Reads the latest headlines          |
| Any other question | Answered using Groq AI              |

---

## 📸 Example

```
You:
Jarvis

Jarvis:
Yeah...

You:
Open Google

Jarvis:
Opening Google
```

---

```
You:
Jarvis

Jarvis:
Yeah...

You:
What is Artificial Intelligence?

Jarvis:
Artificial Intelligence (AI) is the simulation of human intelligence by machines...
```

---

## 📋 Requirements

```
SpeechRecognition
PyAudio
pyttsx3
requests
groq
```

---

## 🔮 Future Improvements

* GUI Interface
* Weather Updates
* Email Sending
* WhatsApp Messaging
* System Controls (Volume, Brightness)
* Calendar & Reminders
* Chat History
* Face Recognition
* Home Automation
* AI Memory for Personalized Conversations
* Multiple Wake Words
* Cross-platform support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Mohammed Affan**

* Python Developer
* AI & Machine Learning Enthusiast
* Building AI-powered applications with Python and Generative AI

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
