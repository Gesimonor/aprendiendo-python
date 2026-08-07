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
X = df[["sepal length (cm)", "sepal width (cm)", #X son los datos pistas por ejemplo 2 + 2
        "petal length (cm)", "petal width (cm)"]]
y = df["especie"]                                 # y Y son las respuestas ejemplo     4 

print(X.shape)
print(y.shape) # Shape me dice cantidad de filas y columnas de un df

#La idea con una IA es que APRENDA NO QUE MEMORIZE entonces una filosofia es que NO se usa el 100% de datos porque no tendria que
#predecir si tiene la informacion de dato, entonces lo que haces por ejemplo tienes la base de 150Flores , no le enseñas con todo le
#usas el 80% de base para que el otro 20% sean flores de prueba para que intente darte la respuesta en base a lo que aprendio eso es overfitting
#Aqui lo que hicimos fue organizar las variables
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
#Y aqui es donde aprende con las variables de arriba las variables TRAIN
from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

print("Modelo entrenado ✅")

# Aqui se pone aprueba con lo que aprndio con las variables TEST
predicciones = modelo.predict(X_test)
print(predicciones) # [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0]
print(y_test.values) #[1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0]
#Aqui por ejemplo si validamos com las predicciones y los datos reales son los mismos , asi que el modelo de prediccion de flores funciona perfecto 

#Esto es para validar que tan efectivo es la prediccion en cuento las flores 
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predicciones)

print(accuracy) #1.0

#Accuary te dice si es un modelo funcional
#0.0 re mal
#0.5 medio medio
#1.0 exelente 

print(f"Precisión del modelo: {accuracy * 100}%")

# Prueba con estas medidas
flor_nueva = [[6.3, 3.3, 6.0, 2.5]]  # ← números más grandes
prediccion = modelo.predict(flor_nueva)
print(iris.target_names[prediccion[0]])
print(iris.target_names[0])
