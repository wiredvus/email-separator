import secrets
import string
def gerar_senha(tamanho: int) -> str:
    if tamanho <12 :
        print("Cuidado: Tamanho muito pequeno. Gerando 12 caracteres.")
        tamanho = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(secrets.choice(characters) for _ in range(tamanho))
    return senha
if __name__ == "__main__":
    try:
        user_input = input("Digite o tamanho da senha: ")
        tamanho = int(user_input)
        print(f"A sua nova senha é: {gerar_senha(tamanho)}")
    except ValueError:
        print("Erro: Coloque um valor válido")
