import google.generativeai as genai
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
def ask_ai(question):
prompt = f"""
 You are an agriculture expert AI chatbot.
 Answer farmer questions simply.
 Question: {question}
 """
response = model.generate_content(prompt)
return response.text
