import google.generativeai as genai
API_KEY = "AIzaSyA55SoWZ5IcBNqbJrbUHbVLOKrzHERzesg" 
genai.configure(api_key=API_KEY)
model =genai.GenerativeModel("gemini-2.0-flash")
chat =model.start_chat()
print("Chat with AI (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("AI:", response.text)
