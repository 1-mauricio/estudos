import numpy as np
def main():
    # ones / zeros / full / empty
    vetor = np.empty(4, int)
    print(vetor)
    
    matriz = np.zeros((3,4), float)
    print(matriz.shape)
    print(matriz)

    matriz1 = np.array([[1,2,3.],[0,3,1]])
    print(matriz1)
    matriz1.reshape(3,2)
    print(matriz1)

    mat = np.arange(10)
    print(mat)

if __name__ == "__main__":
    main()