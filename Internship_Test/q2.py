num1 = int(0)
num2 = int(1)
num3 = int(0)

print("Consulte se um número pertence à Sequência de Fibonacci.")

num = int(input("Digite um número:"))

while num > num3:
    num3 = num1 + num2
    num1 = num2
    num2 = num3

if num == 0 | num == 1:
    print("O número " + str(num) + " está na sequência de Fibonacci.")
elif num == num3:
    print("O número " + str(num) + " está na Sequência de Fibonacci.")
else:
    print("O número não está presente na Sequência de Fibonacci.")