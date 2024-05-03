import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyAJhZZg0fiBqNCZpRX3zHwKroIEGXXBElY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')
import PIL
image = PIL.Image.open('assets/VK.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content(["Generate a json of ingredients with their count present in the image",image])
print(response.text)