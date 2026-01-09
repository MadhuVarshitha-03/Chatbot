# Chatbot

# 🤖 Gemini Chatbot using Streamlit

An interactive web-based chatbot built with **Streamlit** and **Google Gemini API**, enabling real-time conversational AI through a clean and user-friendly interface.

---

## 🚀 Features
- Real-time AI-powered conversations using **Google Gemini**
- Interactive chat UI similar to ChatGPT
- Session-based chat history management
- Clear Chat functionality
- Fast and cost-efficient responses using **Gemini Flash**
- Secure API key handling

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** – Web application framework
- **Google Gemini API** (via `google-genai` SDK)
- **Gemini Flash Model**

---

## 📂 Project Structure
.
├── sample.py # Main Streamlit application
├── README.md # Project documentation

yaml
Copy code

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
2️⃣ Create a Virtual Environment (Optional)
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install streamlit google-genai
🔑 API Key Setup
Visit Google AI Studio: https://aistudio.google.com/

Create a new Gemini API key

Replace the placeholder in sample.py:

python
Copy code
client = genai.Client(api_key="YOUR_API_KEY")
⚠️ Do not commit your API key to GitHub.

▶️ Running the Application
bash
Copy code
python -m streamlit run sample.py
Open your browser and go to:

arduino
Copy code
http://localhost:8501
💬 Usage
Type a message in the chat input

Receive instant AI-generated responses

Click Clear Chat to reset the conversation

📌 Future Enhancements
Streaming responses

System prompt / personality customization

Authentication & user profiles

Deployment on Streamlit Cloud

Conversation export feature
