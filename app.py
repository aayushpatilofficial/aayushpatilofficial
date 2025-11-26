from flask import Flask, request, jsonify, send_from_directory
import os
from openai import OpenAI

app = Flask(__name__, static_folder='.')

client = None

def get_openai_client():
    global client
    if client is None:
        api_key = os.environ.get('OPENAI_API_KEY')
        if api_key:
            client = OpenAI(api_key=api_key)
    return client

SYSTEM_PROMPT = """You are Aayush's AI Assistant on his portfolio website. You help visitors learn about Aayush Patil, a 14-year-old AI Engineer & Digital Innovator.

About Aayush:
- Age: 14 years old
- Role: AI Engineer & Digital Innovator
- Contact: aayushpatilofficial@gmail.com, +91 8217575558, WhatsApp available

His 18 Projects:
1. LovelyAayush4U Website - Portfolio with advanced animations, interactive UI, YouTube integration
2. Aswathama Classes Website - Gift for tuition teacher with Windows-11-style animations
3. V Network Regd - Complete news publishing website
4. NGO Connector - Platform connecting NGOs with people, search by category/city, donations
5. Class-Only Website - Flask + PostgreSQL secure platform with admin panel
6. Advanced Math Quiz (Django) - Learning platform with leaderboard, badges, progress tracking
7. Advanced Math Proof Website (Flask) - Upload and showcase math proofs
8. Portfolio/3D Startup Prompts - Custom prompts for professional 3D websites
9. NeuraSync / BrowserSync - Browser-sync concept with documentation
10. Custom AI Personality Model - Fine-tuned AI using Ollama with real chat data
11. HopePulse AI Prototype - Mental health detection for wearable bracelet
12. Python Math Website + App - Math platform with Play Store app plans
13. Formula-Making Practice Set - Chemistry problems for elements 1-30
14. Math Hero Comic-Style Trailer - Animated promotional concept
15. HopePulse 15-Minute Speech - Stage speech for VenuDhwani on emotional awareness
16. HopePulse Radio Interview - 45-minute radio interview script
17. HopePulse Wearable Bracelet - FLAGSHIP: Bracelet detecting emotionally distressed people nearby
18. Sustainable Futures Project - Interschool science competition project

His Skills: Python, TensorFlow, PyTorch, Machine Learning, NLP, React, Node.js, JavaScript, APIs, UI/UX Design, Automation

Be friendly, helpful, and concise. Answer questions about Aayush's projects, skills, and how to contact him. If asked about hiring or collaboration, encourage them to reach out via email or WhatsApp."""

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/chat', methods=['POST'])
def chat():
    openai_client = get_openai_client()
    
    if not openai_client:
        print("ERROR: OpenAI client not initialized - API key missing or invalid")
        return jsonify({'error': 'AI service not configured. Please add your OpenAI API key.'}), 503
    
    try:
        data = request.json or {}
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        print(f"Sending message to OpenAI: {user_message[:50]}...")
        
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300
        )
        
        reply = response.choices[0].message.content
        print(f"Got reply from OpenAI: {reply[:50]}...")
        return jsonify({'reply': reply})
    
    except Exception as e:
        print(f"ERROR in chat: {type(e).__name__}: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
