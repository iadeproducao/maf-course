import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
if not deployment:
    raise ValueError("Defina AZURE_OPENAI_DEPLOYMENT no ambiente.")

response = client.responses.create(
    model=deployment,
    input="Explique em uma frase o que é um agente de IA."
)

print(response.output_text)
