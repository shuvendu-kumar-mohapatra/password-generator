from src.generator import generate_password
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)