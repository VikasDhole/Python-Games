def calculator():
    print("\n🧮 Calculator")
    print("=" * 30)

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 == 0:
                print("❌ Cannot divide by zero!")
            else:
                print("Result:", num1 / num2)
        else:
            print("❌ Invalid operator!")

    except:
        print("❌ Invalid input!")

    input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    calculator()