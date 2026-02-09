const SYSTEM_PROMPT = `You are an AI-based Health Assistant Chatbot created for educational purposes.

Your role:
- Answer general health-related questions clearly and simply.
- Explain human diseases in an easy-to-understand manner.
- Provide information about:
  • Disease causes
  • Symptoms
  • Prevention methods
  • General medication information (name and purpose only)
  • Recommended food and diet
  • Simple exercises and healthy habits

Guidelines:
- Do NOT diagnose diseases.
- Do NOT prescribe medicine dosage.
- Do NOT replace professional medical advice.
- Avoid emergency instructions.
- Always advise consulting a qualified doctor for medical issues.
- Be polite, supportive, and user-friendly.
- Use simple English suitable for students and common users.

Response format:
- Disease Overview
- Symptoms
- Causes
- Food Recommendations
- Exercise Suggestions
- Precautions
- Disclaimer

Always end the response with:
"⚠️ Disclaimer: This information is for educational purposes only and is not a substitute for professional medical advice. Please consult a doctor."`;

// Use direct REST API calls
const getAIResponse = async (userMessage) => {
  try {
    console.log('📝 User message:', userMessage);
    
    // Use Groq API (Fast & Free)
    if (process.env.GROQ_API_KEY) {
      console.log('🤖 Using Groq API (Llama 3.3)');
      
      const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.GROQ_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: 'llama-3.3-70b-versatile',
          messages: [
            { role: 'system', content: SYSTEM_PROMPT },
            { role: 'user', content: userMessage }
          ],
          temperature: 0.7,
          max_tokens: 1000
        })
      });
      
      if (!response.ok) {
        const error = await response.text();
        console.error('Groq error:', error);
        throw new Error(`Groq API error: ${response.statusText}`);
      }
      
      const data = await response.json();
      console.log('✅ Response received from Groq');
      return data.choices[0].message.content;
    }
    
    throw new Error('No valid API key configured');
    
  } catch (error) {
    console.error('❌ AI API error:', error.message);
    throw error;
  }
};

const handleChat = async (req, res) => {
  try {
    const { message } = req.body;

    if (!message || message.trim() === '') {
      return res.status(400).json({
        success: false,
        error: 'Message is required'
      });
    }

    // Get response from AI
    const response = await getAIResponse(message);

    res.json({
      success: true,
      response: response
    });

  } catch (error) {
    console.error('Chat error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to process your request. Please try again.'
    });
  }
};

module.exports = {
  handleChat
};
