from groq import Groq
import os
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = Groq(
    api_key=os.environ.get("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"),
)

completion = client.chat.completions.create(
 model="llama3-8b-8192",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)