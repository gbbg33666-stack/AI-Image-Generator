import requests

# اترك التوكن فارغاً للرفع الآمن على GitHub
API_TOKEN = "" 
API_URL = "https://api-inference.huggingface.co/models/ali-vilab/modelscope-damo-text-to-video-hd"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def create_video(prompt):
    print(f"جاري تحويل نصك إلى فيديو: {prompt}")
    print("انتظر قليلاً، طبخ الفيديو يحتاج دقة...")
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.content

# اكتب وصف الفيديو هنا (مثال: أسد يركض في الغابة بدقة عالية)
my_prompt = "A majestic lion running in the forest, cinematic, 4k"
video_data = create_video(my_prompt)

with open("my_ai_video.mp4", "wb") as f:
    f.write(video_data)

print("مبروك! الفيديو جاهز باسم my_ai_video.mp4")
