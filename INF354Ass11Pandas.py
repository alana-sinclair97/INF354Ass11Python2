import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt

sample_data = pd.read_csv('tips.csv')

#sample_data['total survived'] = count(data['survived'])
print(sample_data)

sample_data["percentage of tip"] = sample_data["tip"]/sample_data["total_bill"]*100

print(sample_data)

print("Non Smokers")
print(sample_data[sample_data["smoker"]=='No'])

print("Correlation Coefficient")
print(np.corrcoef(sample_data["total_bill"], sample_data["tip"]))

smokers = sample_data[sample_data.smoker == 'Yes']
smokersTotal = smokers['total_bill'].sum()

nonsmokers = sample_data[sample_data.smoker == 'No']
nonSmokersTotal = nonsmokers['total_bill'].sum()

x_axis = ['Smoker', 'Non-Smoker']
y_axis = [smokersTotal, nonSmokersTotal]

ind = np.arange(len(x_axis))

plt.bar(ind, y_axis,color=['green', 'blue'])
plt.ylabel('Total Bills')
plt.xlabel('Smokers / Non-Smokers')
plt.title('Total Bills per category of smoker??')
plt.xticks(ind, x_axis)
plt.show()