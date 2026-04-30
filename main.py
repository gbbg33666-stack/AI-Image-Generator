import request

# هذا هو المفتاح الخاص بك الذي استخرجته
API_TOKEN =" "
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    print("جاري إرسال الطلب للمطبخ العالمي... انتظر قليلاً")    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# هنا يمكنك تغيير الوصف لصنع أي صورة تريدها (بالانجليزية)
my_prompt = "A majestic lion wearing a golden crown, digital art, 4k"

image_bytes = query({"inputs": my_prompt})

# حفظ الصورة الناتجة
with open("my_ai_image.png", "wb") as f:
    f.write(image_bytes)

print("مبروك! تم توليد الصورة بنجاح وحفظها باسم: my_ai_image.png")
