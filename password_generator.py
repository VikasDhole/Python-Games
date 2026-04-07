import random
import string

def password_generator():
    print("\n🔐 Password Generator")
    print("=" * 30)

    length = input("Enter password length: ").strip()

    if not length.isdigit():
        print("❌ Enter a valid number!")
        return

    length = int(length)

    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))

    print("Generated Password:", password)

    input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    password_generator()