import os

def greet(name: str) -> str:
    return f"Olá, {name}!Bem-vindo à aula 5"

if __name__ == "__main__":
    user = os.getenv("APP_USER", "Mundo")
    print(greet(user))
