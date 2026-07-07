import os
import json
from flask import request, jsonify
from config.gemini import ai_service

SYSTEM_PROMPT = '''You are an AI-based Health Assistant Chatbot created for educational purposes.

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
  • Daily check-in review and routine suggestions based on sleep, hydration, movement, mood, and notes

Guidelines:
- Do NOT diagnose diseases.
- Do NOT prescribe medicine dosage.
- Do NOT replace professional medical advice.
- Avoid emergency instructions.
- Always advise consulting a qualified doctor for medical issues.
- Be polite, supportive, and user-friendly.
- Use simple English suitable for students and common users.
- When the user shares a daily check-in, summarize the data first and then suggest a realistic morning, afternoon, and evening routine.
- Keep routine suggestions short, practical, and tailored to the user's reported energy, mood, sleep, hydration, and activity.
- If the daily check-in is incomplete, ask for the missing details before giving a routine.

Response format:
Use clear headings and structure without asterisks. Organize information clearly with line breaks.
Include sections like: Overview, Symptoms, Causes, Food Recommendations, Exercise Suggestions, Precautions.

Important: Do NOT use asterisks (**) or markdown formatting. Use plain text with clear structure and line breaks.

Always end the response with:
"⚠️ Disclaimer: This information is for educational purposes only and is not a substitute for professional medical advice. Please consult a doctor."'''

def normalize_tracking_data(tracking_data):
    if not tracking_data:
        return None
    
    if isinstance(tracking_data, str):
        try:
            return json.loads(tracking_data)
        except Exception:
            return {"rawSummary": tracking_data}
            
    return tracking_data

def build_system_prompt(tracking_data):
    normalized_tracking_data = normalize_tracking_data(tracking_data)
    
    if not normalized_tracking_data:
        return SYSTEM_PROMPT
        
    tracking_data_str = json.dumps(normalized_tracking_data, indent=2)
    return f"{SYSTEM_PROMPT}\n\nDaily tracking context:\n{tracking_data_str}\n\nUse this context to tailor the reply and suggest a practical routine for today."

def get_ai_response(user_message, tracking_data):
    try:
        print(f"User message: {user_message}")
        system_prompt = build_system_prompt(tracking_data)
        return ai_service.get_response(user_message, system_prompt)
    except Exception as e:
        print(f"AI API error: {str(e)}")
        raise e

def handle_chat():
    try:
        data = request.get_json() or {}
        
        message = data.get('message')
        tracking_data = data.get('trackingData')
        
        if not message or message.strip() == '':
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
            
        # Get response from AI
        try:
            response_text = get_ai_response(message, tracking_data)
            return jsonify({
                'success': True,
                'response': response_text
            })
        except Exception as api_err:
            # Handle invalid/expired API key issues gracefully as requested by requirement 14
            print(f"Chat error during AI generation: {str(api_err)}")
            return jsonify({
                "success": False,
                "error": "Invalid API key"
            }), 400
        
    except Exception as e:
        print(f"Chat error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Failed to process your request. Please try again.'
        }), 500
