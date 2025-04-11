import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(paragraph_topic):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  # Or "gpt-3.5-turbo-instruct" if supported
        prompt=f"Write a blog post about {paragraph_topic}.",
        max_tokens=400,
        temperature=0.5
    )
    return response.choices[0].text.strip()

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog_post(paragraph_topic))
  else:
    keep_writing = False