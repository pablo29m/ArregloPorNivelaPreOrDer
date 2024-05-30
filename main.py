def preorder(arr):
    if len(arr)==0:
        print("No es posible ordenar. El arreglo esta vacio")
        return []

    n = len(arr)
    stack = [0]
    preorder = []

    while stack:
        index = stack.pop()
        if index < n:
            preorder.append(arr[index])  # Visito
            stack.append(2 * index + 2)  # Hijo derecho
            stack.append(2 * index + 1)  # Hijo izquierdo

    return preorder

def main():
    arreglopornivel = ["H","D","M","A","F","I","N"]
    arreglopreorder = preorder(arreglopornivel)
    print(arreglopreorder)

main()
