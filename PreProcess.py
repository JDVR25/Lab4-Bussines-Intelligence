import numpy as np

def prepararDatos(data):
   # columnasAnalisis=['alcohol','hepatitis_B','bmi','under_five_deaths',
   #                'polio','diphtheria','hiv_aids','thinness_10_19_years','income_composition_of_resources','schooling']
   #columnasAnalisis=['Alcohol', 'Hepatitis B', 'BMI', 'under-five deaths',
   #   'Polio', 'Diphtheria', 'HIV/AIDS', 'thinness 10-19 years',
   #   'Income composition of resources', 'Schooling']


   #print(data.columns)
   #data=data[columnasAnalisis]
   # Se identifican las filas que tengan una esperanza de vida de 0 años, para luego quitarlas
   # data['Life expectancy'].replace({0:np.nan},inplace=True)
  
   # Se eliminan las filas que reporten más de 1000 muertes de menores de 5 años por cada 1000 habitantes
   # data.loc[ data['under_five_deaths'] > 1000, 'under_five_deaths' ] = np.nan

    #Se convierten las muertes confirmadas por VIH/SIDA por cada 1000 nios nacidos 
    #vivos en una variable binaria, que indica si hubo o casos reportados
   # data.loc[ data['hiv_aids'] <= 1, 'hiv_aids' ] = 0
   # data.loc[ data['hiv_aids'] > 1, 'hiv_aids' ] = 1

    #Se eliminan las filas que tengan un valor nulo
   # data.dropna(inplace=True)

   #data['Alcohol']=data['alcohol']
   #data['Hepatitis B']=data['hepatitis_B']
   #data['BMI']=data['bmi']
   #data['under-five deaths']=data['under_five_deaths']
   #data['Polio']=data['polio']
   #data['Diphtheria']=data['diphtheria']
   # data['HIV/AIDS']=data['hiv_aids']
   data['thinness  10-19 years']=data['thinness 10-19 years']
   #data['thinness  10-19 years']=data['thinness_10_19_years']
   # data['Income composition of resources']=data['income_composition_of_resources']
   # data['Schooling']=data['schooling']

   return data