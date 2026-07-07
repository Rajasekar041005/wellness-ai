import os
import requests

def clean_key(key):
    if not key:
        return None
    key = key.strip()
    if (key.startswith('"') and key.endswith('"')) or (key.startswith("'") and key.endswith("'")):
        key = key[1:-1].strip()
    return key if key else None

class AIService:
    def __init__(self):
        self.api_key = None
        self.error_reason = None
        self.mock_mode = os.getenv('MOCK_MODE', 'false').lower() == 'true'

        if self.mock_mode:
            print("[OK] Running in Mock Mode")
            return

        groq_key = clean_key(os.getenv('GROQ_API_KEY'))

        if not groq_key:
            self.error_reason = "GROQ_API_KEY is not set in .env"
            print("[ERROR] GROQ_API_KEY not found")
            return

        self.api_key = groq_key
        self._test_connection()

    def _test_connection(self):
        try:
            response = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'llama-3.3-70b-versatile',
                    'messages': [{'role': 'user', 'content': 'Say hello'}],
                    'max_tokens': 10
                }
            )
            if not response.ok:
                raise Exception(f"Status {response.status_code}: {response.text}")
            self.error_reason = None
            print("[OK] Groq API connected successfully")
        except Exception as e:
            self.error_reason = str(e)
            print(f"[ERROR] Groq connection failed: {str(e)}")

    def get_response(self, user_message, system_prompt):
        # Mock mode response
        if self.mock_mode:
            return (
                "Hello! I am currently running in Demo Mode (no API key configured).\n\n"
                "Overview:\nThis is a sample response from the Health Assistant.\n\n"
                "Food Recommendations:\nMaintain a balanced diet with vegetables, fruits, and plenty of water.\n\n"
                "Exercise Suggestions:\nA daily 30-minute walk improves energy and overall health.\n\n"
                "Precautions:\n"
                "⚠️ Disclaimer: This information is for educational purposes only and is not a substitute "
                "for professional medical advice. Please consult a doctor."
            )

        if self.error_reason:
            raise Exception(f"Groq API is not configured: {self.error_reason}")

        try:
            response = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'llama-3.3-70b-versatile',
                    'messages': [
                        {'role': 'system', 'content': system_prompt},
                        {'role': 'user', 'content': user_message}
                    ],
                    'temperature': 0.7,
                    'max_tokens': 1000
                }
            )
            if not response.ok:
                raise Exception(f"Groq API error {response.status_code}: {response.text}")
            data = response.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            raise Exception(f"Groq API error: {str(e)}")

ai_service = AIService()
