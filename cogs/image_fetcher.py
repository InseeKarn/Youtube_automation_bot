import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_free_image(query):
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    url = f'https://api.unsplash.com/photos/random?query={query}&client_id={access_key}'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        image_url = data['urls']['regular']
        
        # ดาวน์โหลดและบันทึกภาพ
        image_file = "your_image.png"
        image_data = requests.get(image_url).content
        with open(image_file, 'wb') as f:
            f.write(image_data)

        return image_file  # ส่งกลับชื่อไฟล์ภาพที่ดาวน์โหลด
    else:
        print("Error fetching image:", data.get('errors', 'Unknown error'))
        return None
