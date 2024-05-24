from openai import OpenAI
from Ipython.display import Markdown

client = OpenAI()

image_gen = client.images.generate(
  model="dall-e-3",
  prompt="A cute baby sea otter",
  n=1,
  size="1024x1024"
)
image_url = image_gen.data[0].url
Markdown(f'![alt text]({image_url})')