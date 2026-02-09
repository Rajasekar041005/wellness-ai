// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
  // Auto-focus on input
  userInput?.focus();
});

// Clear Chat functionality
document.getElementById('clearChatBtn')?.addEventListener('click', () => {
  if (confirm('Are you sure you want to clear the current chat?')) {
    chatMessages.innerHTML = `
      <div class="message bot-message">
        <div class="message-content">
          <p>👋 Hello! I'm your Health Assistant. I can help you with general health information about diseases, symptoms, prevention, food recommendations, and healthy lifestyle tips.</p>
          <p><strong>Remember:</strong> I provide educational information only and cannot diagnose or prescribe treatments. Always consult a doctor for medical advice.</p>
        </div>
      </div>
    `;
  }
});

// Chat functionality
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const chatMessages = document.getElementById('chatMessages');
const sendBtn = document.getElementById('sendBtn');

// API endpoint (adjust if your backend is on a different port)
const API_URL = 'http://localhost:3000/api/chat';

chatForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const message = userInput.value.trim();
  if (!message) return;

  // Add user message to chat
  addMessage(message, 'user');
  userInput.value = '';

  // Show typing indicator
  const typingIndicator = addTypingIndicator();

  try {
    // Send message to backend
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();

    // Remove typing indicator
    typingIndicator.remove();

    if (data.success) {
      // Add bot response to chat
      addMessage(data.response, 'bot');
    } else {
      addMessage('Sorry, I encountered an error. Please try again.', 'bot');
    }
  } catch (error) {
    console.error('Error:', error);
    typingIndicator.remove();
    addMessage('Sorry, I could not connect to the server. Please make sure the backend is running.', 'bot');
  }

  // Scroll to bottom
  scrollToBottom();
});

function addMessage(text, type) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${type}-message`;
  
  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  
  // Convert line breaks to paragraphs
  const paragraphs = text.split('\n').filter(p => p.trim());
  paragraphs.forEach(paragraph => {
    const p = document.createElement('p');
    p.textContent = paragraph;
    contentDiv.appendChild(p);
  });
  
  messageDiv.appendChild(contentDiv);
  chatMessages.appendChild(messageDiv);
  
  return messageDiv;
}

function addTypingIndicator() {
  const messageDiv = document.createElement('div');
  messageDiv.className = 'message bot-message';
  
  const typingDiv = document.createElement('div');
  typingDiv.className = 'typing-indicator';
  
  for (let i = 0; i < 3; i++) {
    const dot = document.createElement('div');
    dot.className = 'typing-dot';
    typingDiv.appendChild(dot);
  }
  
  messageDiv.appendChild(typingDiv);
  chatMessages.appendChild(messageDiv);
  scrollToBottom();
  
  return messageDiv;
}

function scrollToBottom() {
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Auto-focus on input
userInput?.focus();
