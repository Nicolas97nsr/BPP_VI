import pandas as pd
import matplotlib.pyplot as plt


try:

# - Comprobamos la existencia del archivo y lo abrimos
    df = pd.read_csv("finanzas2020[1].csv", sep='\t', header=0)
    #creo un nuevo dataframe copiando el dataframe original para guardar los datos del archivo original en caso que tengamos que volver a utilizar
    df1= df.copy()
    #print(df1)

except FileNotFoundError:
    print("El fichero no existe o no se encuentra en el directorio indicado")

# - En el caso que el archivo este OK y lo lea correctamente continuaremos
# - Obtenemos el número de filas y columnas
else:

    n_filas = len(df1.index)
    n_columnas = len(df1.columns) 

# - Comprobamos que el fichero tiene 12 columnas
    assert(n_columnas==12), "El número de columnas no corresponde a los doce meses"
# - Comprobamos que las doce columnas coinciden con los meses del año
    mes = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
           'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    assert(list(df1.columns)==mes), "Las columnas del fichero no corresponden a los meses del año"
# - Comprobamos que hay datos en más de una fila
    assert(n_filas>1), "No hay datos en el fichero"

# - Comprobando que los datos son correctos y si no es así los invalidamos
    for i in range(12):
        if df1[mes[i]].dtype==object:
            df1[mes[i]] = pd.to_numeric(df1[mes[i]], errors='coerce')
            ''' df1[mes].fillna(0, inplace=True) *Aqui he intentado hacerlo de esta forma
            pero me daba el error al obtener el máximo de las columnas'''
            print("Hay datos incorrectos en la columna", mes[i], "\n")

# - Continuaremos despues de corregir los datos incorrectos        
# - Calculamos los totales de cada lista.
    suma_meses = []
    for i in range(12):
        suma_meses.append(df1[mes[i]].sum(axis=0))#guardamos los la lista suma_meses el resultado del valance de los ingresos y gastos de cada mes
        print("El resultado de los ingresos menos los gastos (BALANCE) es:",
        
         suma_meses)
    
    
# - Obtenemos mediante bucle los ingresos y gastos, los guardamos en listas para su posterior uso
    '''    total =[]
    for i in range(len(df1.columns)):
            total.append(list(df1[mes[i]]))
    print(total)

    gastos =[]
    for j in (total):
        if j < 0:
            gastos.append(j)
    print(gastos)

    * Intente hacerlo de esta forma para conseguir todos los gastos y los ingresos pero me
    da el error al meterlo en la lista de "gastos" ya que la lista "total" es un 
    conjunto de listas por las columnas de los meses del dataframey no permite el salto
    de lista a lista --> "[...], [...]" '''

    def mes_gasto_ingreso(datos_df, n):
        i = 0   
        gastos = 0 # - En la variable "gastos obtenemos la suma por mes de todos los gastos"
        ingresos = 0 # - En la variable "ingresos obtenemos la suma por mes de todos los ingresos"
        for i in range(n):
            if datos_df[i] < 0:
             gastos = gastos - datos_df[i]
            elif datos_df[i] >= 0:
                ingresos = ingresos + datos_df[i]
        return gastos, ingresos

    gastos_mes = [] # - Lista con todos los gastos del año
    ingresos_mes =[] # - Lista con todos los ingresos del año
    for j in range(12):
        datos = mes_gasto_ingreso(df1[mes[j]], n_filas) 
        gastos_mes.append(datos[0])
        ingresos_mes.append(datos[1])


# - Creamos un nuevo dataframe las nuevas listas para guardar los datos que necesitamos para hacer los cálculos
    datos_año = { 'Mes' : mes,
                  'Gastos' : gastos_mes,
                  'Ingresos': ingresos_mes,
                  'Balance mes': suma_meses}
    df2 = pd.DataFrame(datos_año)

    print("\n")
    print(df2)
    print("\n")

#  - Mes con el mayor gasto
    max_gasto = df2.loc[df2["Gastos"] == df2["Gastos"].max()]['Mes'].values
    print("El mes de mayor gasto ha sido", max_gasto[0], "con un gasto de:", df2["Gastos"].max())

    ''' Utilizamos ".loc" para selecionar los Gastos del df2, utilizamos ".max" para obtener 
        el mes con los gastos más altos y utilizamos ".value" para identificar los valores del df2'''


#  - Mes que más a ahorrado
    max_ahorro = df2.loc[df2["Balance mes"] == df2["Balance mes"].max()]['Mes'].values
    print("El mes de mayor ahorro ha sido", max_ahorro[0], "con un beneficio de:", df2["Balance mes"].max()) 


#  - Media de gastos del año
    print("La media de gastos del año ha sido: ", df2["Gastos"].mean())

#  - El gasto total de a lo largo del año
    print("El gasto de total del año ha sido: ", df2['Gastos'].sum(axis=0))

#  - Ingresos totales a lo largo del año
    print("Los ingresos totales a lo largo del año han sido: ", df2['Ingresos'].sum(axis=0))

#  - Gráfica de evoluvión de ingresos anual
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(mes, ingresos_mes)
    plt.show()




        
            



    







'''def extraer(nombre_archivo, indice_columna):
    numero_fila = 0
    with open(nombre_archivo, "r") as entrada:
        csv_reader = csv.reader(entrada, delimiter=',')
        for fila in csv_reader:
            yield numero_fila, fila[indice_columna]
            numero_fila += 1

salida = [x[1] for x in extraer("finanzas2020.csv", 0) if x[0] >= 2]
print(salida)'''

