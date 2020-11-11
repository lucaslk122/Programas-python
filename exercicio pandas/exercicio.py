# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import pandas as pd
sal = pd.read_csv('Salaries.csv')
print (sal.info())
print ("Salario médio = ",sal['BasePay'].mean())
print ('Overtume pay = ',sal['OvertimePay'].max())
print (sal[sal['EmployeeName']== 'JOSEPH DRISCOLL'])