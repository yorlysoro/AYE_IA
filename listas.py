#Uso de listas en python

lista = [ 1, 2, 3, 4 ,5 , 6]


#Usando las listas como pilas

stack = []

stack.append(5)
stack.append(3)
stack.append(8)

#Calculadora RPN con pila

stack = []
aux_stack = []
entrada = ''

while entrada != 'q':
    entrada = input('In:')
    if entrada == 'q':
        break
    else:
        stack.append(entrada)
        if entrada == '+':
            stack.pop()
            stack.append(int(stack.pop()) + int(stack.pop()))
            print(stack)
        elif entrada == '-':
            stack.pop()
            stack.append(int('-1')*(int(stack.pop()) - int(stack.pop())))
            print(stack)
        elif entrada == '*':
            stack.pop()
            stack.append(int(stack.pop()) * int(stack.pop()))
            print(stack)
        elif entrada == '/':
            stack.pop()
            stack.append(int(stack.pop()) / int(stack.pop()))
            print(stack)
        
