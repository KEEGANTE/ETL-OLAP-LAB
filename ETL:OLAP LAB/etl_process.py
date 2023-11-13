import pandas as pd

# Read data from the original CSV file
data = pd.read_csv('sales_data.csv')

#Calculate the Total Revenue by multiplying Quantity and Revenue
data['Total Revenue'] = data['Quantity'] * data['Revenue']

#Print data 
print(data)

#save
data.to_csv('transformed_sales_data', index=False)