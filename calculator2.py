#This is the upgraded version of the previous calculator I made (calculator1.py)
#Feel free to give any feedback

import time

time.sleep(1)

print("Hi! You must be here looking for a calculator, but,")
time.sleep(2)
# extra lines / small demo added by the assistant
print()
print("-- Quick demo --")
num1 = 7
num2 = 3
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print()
time.sleep(3)
print("Need a full interactive calculator? I can add one next.")
time.sleep(1)

choice = input("Would you like to see the full interactive calculator? (yes/no): ").strip().lower()

while True:

    if choice == "yes":
        print("Alright! Here's all that boring info:")
        time.sleep(1)
        operations = [
            "1. Add",
            "2. Subtract",
            "3. Multiply",
            "4. Divide",
            "5. Exponentiation",
            "6. Modulus",
        ]

        for operation in operations:
            print(operation)
        print("Please select an operation...")
        op = input("Enter operation number (1-6) or name: ").strip().lower()

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            c_input = input("Enter the third number (optional, press Enter to skip): ").strip()
            d_input = input("Enter the fourth number (optional, press Enter to skip): ").strip()
            c = float(c_input) if c_input != "" else None
            d = float(d_input) if d_input != "" else None

        except ValueError:
            print("Invalid number entered. Exiting.")
            quit()

        if op in ("1", "add", "addition", "+"):
            total = a + b + (c if c is not None else 0) + (d if d is not None else 0)
            print(
                f"Result: {a} + {b} + {c if c is not None else 0} + {d if d is not None else 0} = {total}"
            )
        elif op in ("2", "subtract", "sub", "-"):
            total = a - b - (c if c is not None else 0) - (d if d is not None else 0)
            print(
                f"Result: {a} - {b} - {c if c is not None else 0} - {d if d is not None else 0} = {total}"
            )
        elif op in ("3", "multiply", "mul", "*"):
            prod = a * b
            if c is not None:
                prod *= c
            if d is not None:
                prod *= d
            c_val = c if c is not None else 0
            d_val = d if d is not None else 0
            print(f"Result: {a} * {b} * {c_val} * {d_val} = {prod}")
        elif op in ("4", "divide", "div", "/"):
            divisors = [x for x in (b, c, d) if x is not None]
            if any(x == 0 for x in divisors):
                print("Cannot divide by zero.")
            else:
                res = a
                for x in divisors:
                    res = res / x
                b_val = b
                c_val = c if c is not None else 0
                d_val = d if d is not None else 0
                print(f"Result: {a} / {b_val} / {c_val} / {d_val} = {res}")
        elif op in ("5", "exponent", "exponentiation", "^"):
            exponents = [x for x in (b, c, d) if x is not None]
            try:
                res = a
                for x in exponents:
                    res = res ** x
                b_val = b
                c_val = c if c is not None else 0
                d_val = d if d is not None else 0
                print(f"Result: {a} ** {b_val} ** {c_val} ** {d_val} = {res}")
            except OverflowError:
                print("Result too large.")
        elif op in ("6", "modulus", "mod", "%"):
            moduli = [x for x in (b, c, d) if x is not None]
            if any(x == 0 for x in moduli):
                print("Cannot modulus by zero.")
            else:
                res = a
                for x in moduli:
                    res = res % x
                b_val = b
                c_val = c if c is not None else 0
                d_val = d if d is not None else 0
                print(f"Result: {a} % {b_val} % {c_val} % {d_val} = {res}")
        else:
            print("Invalid operation selected. Exiting.")
    else:
        print("No problem! Come back next time!")
        break
            

