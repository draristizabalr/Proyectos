from pandas import read_excel,ExcelWriter

while True:
    try:
        fname = input('Ingresar nombre del archivo: ')
        file = read_excel(fname+'.xlsx')
        break
    except:
        print(f'El archivo con el nombre {fname} no existe. Verificar nombre.')

excel = file
error = ['*','+','/']
titulos = list(excel.columns)

for sim in error:
    excel = excel[(~excel[titulos[1]].str.startswith(sim)) &\
                  (excel[titulos[11]] != 0)]

with ExcelWriter(fname+'_2'+'.xlsx') as write:
    file.to_excel(write,sheet_name='Original')
    excel.to_excel(write,sheet_name='Filtro')