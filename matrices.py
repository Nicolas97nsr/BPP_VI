class Matrizz:
    """En esta clase veremos distintas operaciones de matrices.

    Atributos
    =========
    Matriz:
        Valores con la que se van a realizar las operaciones.

    Métodos:
    ========
    Suma valores:
        Método para sumar todos los valores de una matriz.
    Suma fila:
        Método para sumar los elementos de la fila de una matriz.
    Suma columna:
        Método para sumar los elementos de la columna de una matriz.
    Indica negativos:
        Método que indica si hay números negativos en una matriz.
    
    Ejemplo:
    ========

    >>>>suma_valores_matriz[[2,3,4], [7,9,1], [2,6,-3]]

    >>>>suma_fila_matriz[[2,3,4]

    >>>>suma_columna_matriz[[2,3,4], [7,9,1], [2,6,-3]]

    >>>>negativo_matriz[[2,3,4], [7,9,1], [2,6,-3]]
    """

    def  __init__(self,matriz):
        """Constructor de la clase matriz
        Args:
            matriz: matriz 1
        """
        self.matriz = matriz


    def suma_valores_matriz(self,matriz:list)->int:
        """Función que permite sumar todos los valores de la matriz.

        Args:
            sefl (class): es el argumento por defecto de la clase matrizz.

            matriz: El argumento son los valores de la matriz.
        """
        suma=0
        for i in range(len(matriz)):
            for j in range(len(self.matriz[i])):
                suma+=self.matriz[i][j]
        return suma

        
    def suma_fila_matriz(self,matriz:list,fila:int)->int:
        """Función que permite sumar los valores una fila de la matriz.

        Args:
            sefl (class): es el argumento por defecto de la clase matrizz.

            matriz: El argumento son los valores de la matriz.

            fila: Indice (POSICIÓN) de una de las filas de la matriz.
        """        
        suma=0
        for j in range(len(matriz[fila])):
            suma+=matriz[fila][j]
        return suma

        
    def suma_columna_matriz(matriz:list,columna:int)->int:
        """Función que permite sumar los valores una columna de la matriz.

        Args:
            sefl (class): es el argumento por defecto de la clase matrizz.

            matriz: El argumento son los valores de la matriz.

            columna: Indice (POSICIÓN) de una de las columnas de la matriz.
        """
        suma=0
        for i in range(len(matriz)):
            suma+=matriz[i][columna]
        return suma
        
        
    def negativo_matriz(matriz:list)->int:
        """Función que permite identificar si hay los valores negativos en la matriz.

        Args:
            sefl (class): es el argumento por defecto de la clase matrizz.

            matriz: El argumento son los valores de la matriz.
        """
        rta=True
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if(matriz[i][j]<0):
                    rta=True
        return rta