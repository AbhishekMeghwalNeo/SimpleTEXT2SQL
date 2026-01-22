from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key= os.getenv("AZURE_OPENAI_KEY"),
    api_version= "2025-01-01-preview",
    azure_endpoint= "https://amiparmar-test-resource.cognitiveservices.azure.com/"
)

response= client.chat.completions.create(
    model= "gpt-4o",
    messages= [
        {
            "role" : "system",
            "content" : "You are a helpful data scientist. Output should not be more than 4 Lines"
        },
        {
            "role" : "user",
            "content" : "Explain Precision and recall in simple terms."
        }
    ]
)

print(response.choices[0].message.content)

# print(os.getenv("AZURE_OPENAI_KEY"))

# # Set Azure OpenAI credentials
# openai.api_type = "azure"
# openai.api_base = "https://amiparmar-test-resource.cognitiveservices.azure.com/"

# openai.api_type = "azure"
# openai.api_version = "2025-01-01-preview"
# openai.api_key = os.environ["AZURE_OPENAI_KEY"]

# # Your deployment name
# deployment_name = "gpt-4o"

# # Chat messages
# messages = [
#     {"role": "system", "content": "You are a helpful assistant that answers concisely."},
#     {"role": "user", "content": "Explain quantum entanglement in one sentence."}
# ]

# # Make the request
# response = openai.chat.completions.create(
#     deployment_id=deployment_name,
#     messages=messages
# )

# # Extract the assistant's reply
# print(response.choices[0].message.content)
