# 🏥 AI-Based Health Assistant Chatbot

An educational health assistant chatbot designed to provide general health information in a simple and accessible manner, powered by Google's Gemini AI.

## 📋 Project Structure

```
health-assistant-chatbot/
│
├── backend/
│   ├── server.js              # Express server
│   ├── routes/
│   │   └── chat.js            # Chat API routes
│   ├── controllers/
│   │   └── chatController.js  # Chat logic and system prompt
│   ├── config/
│   │   └── gemini.js          # Gemini AI configuration
│   ├── package.json           # Backend dependencies
│   └── .env.example           # Environment variables template
│
├── frontend/
│   ├── index.html             # Login page
│   ├── chat.html              # Chatbot interface
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
│
└── README.md                  # This file
```

## ⚠️ Important Disclaimer

**This chatbot provides educational information only and is NOT a substitute for professional medical advice.**

## 🎯 Chatbot Guidelines

You are an AI-based Health Assistant Chatbot created for educational purposes.

### Your Role:
- Answer general health-related questions clearly and simply
- Explain human diseases in an easy-to-understand manner
- Provide information about:
  • Disease causes
  • Symptoms
  • Prevention methods
  • General medication information (name and purpose only)
  • Recommended food and diet
  • Simple exercises and healthy habits

### Guidelines:
- ❌ Do NOT diagnose diseases
- ❌ Do NOT prescribe medicine dosage
- ❌ Do NOT replace professional medical advice
- ❌ Avoid emergency instructions
- ✅ Always advise consulting a qualified doctor for medical issues
- ✅ Be polite, supportive, and user-friendly
- ✅ Use simple English suitable for students and common users

### Response Format:
1. Disease Overview
2. Symptoms
3. Causes
4. Food Recommendations
5. Exercise Suggestions
6. Precautions
7. Disclaimer

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm (comes with Node.js)
- Google Gemini API Key

### Get Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Installation

1. **Clone or download this project**

2. **Install backend dependencies:**
   ```bash
   cd health-assistant-chatbot/backend
   npm install
   ```

3. **Set up environment variables:**
   ```bash
   # Copy the example file
   copy .env.example .env
   
   # Edit .env and add your Gemini API key
   GEMINI_API_KEY=your_actual_api_key_here
   PORT=3000
   ```

### Running the Application

1. **Start the backend server:**
   ```bash
   cd backend
   npm start
   ```
   
   You should see:
   ```
   🏥 Health Assistant Chatbot server running on http://localhost:3000
   📡 API endpoint: http://localhost:3000/api/chat
   ```

2. **Open the application in your browser:**
   ```
   http://localhost:3000
   ```

3. **Login:**
   - Enter any username and password (simple demo login)
   - Click "Login"

4. **Start chatting:**
   - Ask health-related questions
   - Get educational information about diseases, symptoms, diet, and exercise
   - Save a daily check-in to track your habits and receive a suggested routine

## 💻 Development

To run the backend in development mode with auto-restart:

```bash
cd backend
npm run dev
```

## 🔧 API Endpoints

### POST `/api/chat`

Send a message to the chatbot and receive a response.

**Request:**
```json
{
  "message": "What causes diabetes?"
}
```

The API also accepts an optional `trackingData` object for daily check-ins.

**Response:**
```json
{
  "success": true,
  "response": "Disease Overview\nDiabetes is a chronic condition..."
}
```

## 🌟 Features

- ✅ **Clean UI**: Modern, responsive design
- ✅ **Real-time Chat**: Instant responses from Gemini AI
- ✅ **Educational Focus**: Structured health information
- ✅ **Safety First**: Built-in disclaimers and guidelines
- ✅ **Easy Setup**: Simple installation and configuration
- ✅ **Login System**: Basic authentication (demo purposes)
- ✅ **Daily Health Tracker**: Save sleep, water, activity, mood, and notes for each day
- ✅ **Routine Suggestions**: Turn the latest check-in into a practical routine

## 📝 Example Questions to Ask

- "What causes high blood pressure?"
- "How to prevent diabetes?"
- "What foods are good for heart health?"
- "Exercises for lower back pain"
- "Symptoms of vitamin D deficiency"
- "How to improve immunity naturally?"

## 🛠️ Technologies Used

**Backend:**
- Node.js
- Express.js
- Google Gemini AI API
- CORS

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript
- Fetch API

## 📄 License

This project is open source and available for educational purposes.

## ⚠️ Final Disclaimer

**Always end every response with:**

⚠️ Disclaimer: This information is for educational purposes only and is not a substitute for professional medical advice. Please consult a doctor.

---

*Built for educational purposes to help users understand general health concepts and promote health awareness.* 🏥
