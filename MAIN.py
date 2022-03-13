import StudiKasus2
import os
import pandas as pd

case = StudiKasus2.StudiKasus2('localhost', '3306', 'root',"")
df = case.import_csv('example.csv')
print(case.create_db('ASDOS'))
print(case.create_table('example', 'name', df))
print(case.load_data('example', 'name'))