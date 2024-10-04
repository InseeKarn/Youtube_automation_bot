from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

app = Flask(__name__)

@app.route('/api/story-ideas', methods=['GET'])
def get_story_ideas():
    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}',
        'Content-Type': 'application/json'
    }
    url = 'https://ai.google.dev/api/embeddings?hl=th#endpoint'  # แก้ไขให้ตรงกับ URL ที่ถูกต้อง

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # ถ้าตอบกลับไม่เป็น 200 จะเกิดข้อผิดพลาด
        data = response.json()

        if not data.get('ideas'):
            return jsonify({"result": "error", "message": "ไม่พบแนวคิดสำหรับเรื่องราว."})

        return jsonify({"result": "success", "ideas": data['ideas']})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching ideas: {e}")
        return jsonify({"result": "error", "message": "เกิดข้อผิดพลาดในการเรียก API."})

if __name__ == '__main__':
    app.run(debug=True)
