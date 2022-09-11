A=np.array([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0]])
b=np.array([1,2,3])
columnas=np.size(A,1)
filas=np.size(A,0)

comb = combinations(range(columnas),columnas-filas)# paso 1 encontrar todas las combinaciones posibles 5,2
#print(list(comb))
dire = {'Solución':[],'Base':[]}

#crear matriz B
columnas_set=set(np.array(range(columnas))) 

for i in list(comb):
    no_basicas=set(i)
    columnas_mantener=columnas_set^no_basicas#diferencia siemtrica entre conjuntos( lo que no es comun entre los conjuntos), columnas con las cuales construire las soluciones basicas
    B=A[:,list(columnas_mantener)] # paso 2 crear todas las matrices 3x3
    x=np.zeros(columnas)
    Bas=np.zeros((filas,columnas))
    #solucionar B xb=b
    if np.linalg.det(B)!=0: #evitar matrices singulares
            
            xb=np.linalg.solve(B, b)
            x[list(columnas_mantener)]=xb
        
            
            Bas[:,list(columnas_mantener)]=B# se reconstruye la matriz B con las 5 variables 2 en 0
            #print(list(columnas_mantener))
            #guardar en el diccionario
            dire['Solución'].append(x)
            dire['Base'].append(Bas)

pd.set_option('max_colwidth',100)    
out = pd.DataFrame(dire)       
print(out)
            