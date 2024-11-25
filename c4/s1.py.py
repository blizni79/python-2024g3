nList = input("Wprowadz liste liczb calkowitych odzielonych spacja: ")

Lista = nList.split(" ")

for i in range(len(Lista)):
    print(Lista[i], end=" ")
    for j in range(int(Lista[i])):
        print("*",end="")
    print("\n", end="")


# 
numbers = input("Podaj listę liczb całkowitych dodatnich, oddzielonych spacjami: ")
numbers = numbers.split(" ")
for number in numbers:
    if int(number) > 0:
        print('*' * int(number))