import sys
import pandas
print("pandas imported")
# Example: Using pandas to create a simple DataFrame

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pandas.DataFrame(data)
print('DataFrame:')
print(df)