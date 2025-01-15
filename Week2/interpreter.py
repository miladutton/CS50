expression = input("Ask me a math problem ")

x, y, z = expression.split(" ")

match y:
    case "+":
        answer = float(x) + float(z)
        print(answer)
    case "-":
        answer = float(x) - float(z)
        print(answer)
    case "*":
        answer = float(x) * float(z)
        print(answer)
    case "/":
        answer = float(x) / float(z)
        print(answer)
