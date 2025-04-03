import os

def create_env_file():
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("")  
        print("`.env` fayli yaratildi!")

def create_utils_folder():
    if not os.path.exists("utils"):
        os.makedirs("utils")
        print("`utils` papkasi yaratildi.")

def create_env_py():
    env_py_path = os.path.join("utils", "env.py")
    with open(".env", "r") as env_file:
        lines = env_file.readlines()

    if not lines:  # Agar .env bo'sh bo'lsa
        print(".env bo'sh")
        return

    with open(env_py_path, "w") as f:
        f.write('''from environs import Env

env = Env()
env.read_env()

''')
        for line in lines:
            if '=' in line:
                key = line.split('=')[0].strip()
                f.write(f"{key} = env('{key}')\n")

    print("`env.py` yangilandi.")

def main():
    create_env_file()
    create_utils_folder()
    create_env_py()

main()
