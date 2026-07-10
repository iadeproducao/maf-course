from openai import OpenAI

client = OpenAI()

def somar(a: float, b: float) -> float:
    return a + b

# Exemplo didático: em um fluxo real, você declararia esta função como tool
# para o modelo decidir quando chamá-la.
resultado = somar(2, 3)
print(f"Resultado da tool somar: {resultado}")
