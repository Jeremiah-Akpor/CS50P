exp = input("Expression: ")
x,y,z = exp.split()
x = float(x)
z = float(z)

sol = 0

if y.strip() == "+":
    sol = x + z
elif y.strip() == "-":
    sol = x - z
elif y.strip() in ["*", "×"]:
    sol = x * z
elif y.strip() == "/":
    sol = x / z
print(sol)
