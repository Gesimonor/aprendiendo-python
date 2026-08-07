from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["especie"] = iris.target

print(df.head(10))
print(df.shape)

#print(dir(iris))

#print(type(iris.target_names))
#DESCR = str > descripción del dataset
#data = numpy.ndarray > los números de las flores
#data_module = str
#feature_names = list
#filename = str
#frame = NoneType > vacío, no se usó
#target = numpy.ndarray > las especies
#target_names =  numpy.ndarray > ["setosa", "versicolor", "virginica"]
