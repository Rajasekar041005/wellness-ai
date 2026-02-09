const { GoogleGenerativeAI } = require('@google/generative-ai');

// Initialize Gemini AI
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY || 'YOUR_GEMINI_API_KEY_HERE');

const getGeminiResponse = async (userMessage, systemPrompt) => {
  try {
    console.log('🔑 API Key loaded:', process.env.GEMINI_API_KEY ? 'Yes' : 'No');
    console.log('📝 User message:', userMessage);
    
    // Use Gemini Pro model (stable v1 API)
    const model = genAI.getGenerativeModel({ model: 'gemini-pro' });

    // Combine system prompt with user message
    const fullPrompt = `${systemPrompt}\n\nUser Query: ${userMessage}`;

    // Generate response
    const result = await model.generateContent(fullPrompt);
    const response = result.response;
    const text = response.text();

    console.log('✅ Response received');
    return text;
  } catch (error) {
    console.error('❌ Gemini API error:', error.message);
    console.error('Full error:', error);
    throw new Error('Failed to get response from AI service');
  }
};

module.exports = {
  getGeminiResponse
};
