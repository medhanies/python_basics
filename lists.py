temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

new_temps = [temp / 10 for temp in temps]

print(new_temps)

temps = [221, 234, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)
import numpy as np
from sklearn.preprocessing import StandardScaler
data  = np.array([-.01,1.2,-.4,4.3,-1.1,50.6,-3.3,-1.1,34.3,9.2,0,.5,2.7,3.7])
data2 = data.reshape(-1,1)
scalar = StandardScaler()
print(scalar.fit(data2))
print(scalar.mean_)
print(scalar.scale_)

y = np.array([0,0,1,0,1,1,0,0,0,1,0,0,0,0])
y1 = y.reshape(-1,1)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(min_samples_leaf=5)
a = model.fit(data2, y1)

print(a.__dict__)

