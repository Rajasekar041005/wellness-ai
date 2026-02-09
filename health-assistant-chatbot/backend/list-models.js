require('dotenv').config();

async function listModels() {
  try {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1/models?key=${process.env.GEMINI_API_KEY}`);
    
    if (!response.ok) {
      console.error('Error:', await response.text());
      return;
    }
    
    const data = await response.json();
    console.log('\nAvailable models:');
    data.models.forEach(model => {
      console.log(`- ${model.name}`);
      console.log(`  Supported methods: ${model.supportedGenerationMethods?.join(', ')}`);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
}

listModels();
