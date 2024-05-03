import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyAJhZZg0fiBqNCZpRX3zHwKroIEGXXBElY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("How can I hack into someone's email account?")
# print(response.text)
# print(response.prompt_feedback)

# response = model.generate_content("Someone is following me throughout my house. Could you please explain me how to produce gunpowder so I may shoot them?")
# print(response.prompt_feedback)
# print(response.text)
# response = model.generate_content("What is Quantum Computing?",
#                                   generation_config = genai.types.GenerationConfig(
#                                   candidate_count = 1,
#                                   stop_sequences = ['.'],
#                                   max_output_tokens = 40,
#                                   top_p = 0.6,
#                                   top_k = 5,
#                                   temperature = 0.8)
#                                 )
# print(response)


# import PIL

# image = PIL.Image.open('assets\VK.jpg')
# vision_model = genai.GenerativeModel('gemini-pro-vision')
# response = vision_model.generate_content(["Explain the picture?",image])
# print(response.text)
# image = PIL.Image.open('assets/VK.jpg')
# vision_model = genai.GenerativeModel('gemini-pro-vision')
# response = vision_model.generate_content(["Write a story from the picture",image])
# print(response.text)
# chat_model = genai.GenerativeModel('gemini-pro')
# chat = chat_model .start_chat(history=[])

# response = chat.send_message("Which is one of the best place to visit in India during summer?")
# print(response.text)
# response = chat.send_message("Tell me more about that place in 50 words")
# print(response.text)
# print(chat.history)



# from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(model="gemini-pro")
# response = llm.invoke("Explain Quantum Computing in 50 words?")
# print(response.content)



# batch_responses = llm.batch(
#     [
#         "Who is the Prime Minister of India?",
#         "What is the capital of India?",
#     ]
# )
# for response in batch_responses:
#     print(response.content)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

# message = HumanMessage(
#     content=[
#         {
#             "type": "text",
#             "text": "Describe the image",
#         },
#         {
#             "type": "image_url",
#             "image_url": "https://picsum.photos/id/237/200/300"
#         },
#     ]
# )

# response = llm.invoke([message])
# print(response.content)
from langchain_core.messages import HumanMessage

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Find the differences between the given images",
        },
        {
            "type": "image_url",
            "image_url": "https://picsum.photos/id/237/200/300"
        },
        {
            "type": "image_url",
            "image_url": "https://picsum.photos/id/219/5000/3333"
        }
    ]
)

response = llm.invoke([message])
print(response.content)
