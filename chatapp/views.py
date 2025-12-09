from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .chatbot import format_response


def login_view(request):
    """Handle user login"""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        
        # Check credentials
        if user_id == 'health@23' and password == 'gym':
            # Set session to track logged-in user
            request.session['logged_in'] = True
            return redirect('chatbot')
        else:
            return render(request, 'login.html', {'error': 'Invalid User ID or Password'})
    
    return render(request, 'login.html')


def chatbot_view(request):
    """Display chatbot page"""
    # Check if user is logged in
    if not request.session.get('logged_in'):
        return redirect('login')
    
    return render(request, 'chatbot.html')


def chat_api(request):
    """API endpoint for chatbot responses"""
    # Check if user is logged in
    if not request.session.get('logged_in'):
        return JsonResponse({'error': 'Not authenticated'}, status=401)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({'error': 'Empty message'}, status=400)
            
            # Get chatbot response
            bot_response = format_response(user_message)
            
            return JsonResponse({
                'response': bot_response,
                'status': 'success'
            })
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def logout_view(request):
    """Handle user logout"""
    request.session.flush()
    return redirect('login')
