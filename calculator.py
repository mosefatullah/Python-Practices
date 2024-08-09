x = input("What's x? ")
y = input("What's y? ")

print(f"x + y: {(int(x) + int(y)):,}")
print(f"x / y: {(float(x) / float(y)):.2f}")
print(f"x ^ y: {int(x) ** int(y)}") # or, pow(int(x), int(y))
