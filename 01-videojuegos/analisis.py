import pandas as pd
import matplotlib.pyplot as plt

# Dataset embebido - Top 50 videojuegos más vendidos
data = {
    "Name": [
        "Wii Sports", "Super Mario Bros.", "Mario Kart Wii", "Wii Sports Resort",
        "Pokemon Red/Blue", "Tetris", "New Super Mario Bros.", "Wii Play",
        "New Super Mario Bros. Wii", "Duck Hunt", "Nintendogs", "Mario Kart DS",
        "Pokemon Gold/Silver", "Wii Fit", "Wii Fit Plus", "Kinect Adventures",
        "Grand Theft Auto V", "Grand Theft Auto San Andreas", "Super Mario World",
        "Brain Age", "Pokemon Diamond/Pearl", "Super Mario Bros. 3",
        "Call of Duty Black Ops", "FIFA 16", "Pokemon X/Y",
        "Call of Duty Modern Warfare 3", "The Elder Scrolls V: Skyrim",
        "Super Mario 64", "Gran Turismo", "Call of Duty Black Ops II",
        "Minecraft", "Pokemon Sun/Moon", "FIFA 18", "Wii Party",
        "Super Smash Bros. Brawl", "Animal Crossing Wild World",
        "Halo 3", "The Legend of Zelda Ocarina of Time", "FIFA 15",
        "Super Mario Odyssey", "Red Dead Redemption 2", "Overwatch",
        "The Witcher 3", "Dark Souls", "Among Us",
        "Cyberpunk 2077", "Stardew Valley", "Hollow Knight",
        "Celeste", "Undertale"
    ],
    "Platform": [
        "Wii","NES","Wii","Wii","GB","GB","DS","Wii","Wii","NES",
        "DS","DS","GBC","Wii","Wii","X360","PS4","PS2","SNES","DS",
        "DS","NES","X360","PS4","3DS","X360","PS3","N64","PS","X360",
        "PC","3DS","PS4","Wii","Wii","DS","X360","N64","PS4","Switch",
        "PS4","PC","PC","PS3","PC","PC","PC","PC","PC","PC"
    ],
    "Year": [
        2006,1985,2008,2009,1996,1989,2006,2006,2009,1984,
        2005,2005,1999,2007,2009,2010,2013,2004,1990,2005,
        2006,1988,2010,2015,2013,2011,2011,1996,1997,2012,
        2011,2016,2017,2010,2008,2005,2007,1998,2014,2017,
        2018,2016,2015,2011,2020,2020,2016,2017,2018,2015
    ],
    "Genre": [
        "Sports","Platform","Racing","Sports","Role-Playing","Puzzle","Platform","Misc","Platform","Shooter",
        "Simulation","Racing","Role-Playing","Sports","Sports","Misc","Action","Action","Platform","Misc",
        "Role-Playing","Platform","Shooter","Sports","Role-Playing","Shooter","Role-Playing","Platform","Racing","Shooter",
        "Sandbox","Role-Playing","Sports","Party","Fighting","Simulation","Shooter","Adventure","Sports","Platform",
        "Action","Shooter","Role-Playing","Action","Party","Action","Simulation","Adventure","Platform","Role-Playing"
    ],
    "Global_Sales": [
        82.74,40.24,37.14,33.00,31.38,30.26,30.01,29.02,28.62,28.31,
        24.76,23.60,23.10,22.72,21.82,21.82,21.40,20.81,20.61,20.22,
        18.36,17.28,15.09,14.96,16.44,15.09,13.27,11.89,10.95,12.73,
        20.00,16.27,14.10,8.11,13.10,11.75,12.11,7.60,12.65,14.00,
        17.00,15.00,12.00,8.00,14.50,13.00,10.00,5.00,3.50,700.50
    ]
}
#Quiero que escribas una función que recorra los juegos y los clasifique así:
#Ventas > 30 millones   → "Éxito masivo"
#Ventas > 15 millones   → "Muy vendido"
#Ventas > 5 millones    → "Vendido"
#Ventas <= 5 millones   → "Poco vendido"
df = pd.DataFrame(data)

entrada_juego = input("Escriba el juego a buscar: ")

for juego, venta in df.iterrows():
  if venta["Name"] == entrada_juego:
    if venta["Global_Sales"] > 30:
      estado = "Exito masivo"
    elif venta["Global_Sales"] > 15:
        estado = "Muy vendido"
    elif venta["Global_Sales"] > 5:
        estado = "Vendido"
    elif venta["Global_Sales"] <= 5:
      estado = "Poco vendido"
    print(venta["Name"], venta["Global_Sales"] , estado)
    #print(venta["Name"], venta["Global_Sales"])

#print("=== PRIMERAS FILAS ===")
#print(df.head())
#print("\n=== INFO DEL DATASET ===")
#print(df.info())
#print("\n=== ESTADÍSTICAS ===")
#print(df.describe())

# Pregunta 1: ¿Cuántos juegos hay por género?
# Pista: usa .value_counts()

def juegos_x_genero(df):
  return df["Genre"].value_counts()
print(juegos_x_genero(df))

# Pregunta 2: ¿Cuál es el juego con más ventas globales?
# Pista: usa .max() o .idxmax()

def juego_mas_vendido(df):
  indice = df["Global_Sales"].idxmax()
  return df.loc[indice,"Name"]

print(juego_mas_vendido(df))
# Pregunta 3: ¿Cuál es el género con MÁS ventas en total?
# Pista: usa .groupby() y .sum()

def genero_mas_ventas(df):
  return df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False).head(1)


print(genero_mas_ventas(df))

# Pregunta 4: Top 5 juegos más vendidos
# Pista: usa .sort_values() y .head()
print(df["Name"].duplicated().sum())
def juegos5masvendidos(df):
  return df[["Name","Global_Sales"]].sort_values(by="Global_Sales", ascending=False).head(5)
print(juegos5masvendidos(df))


# Gráfica 1 - Ventas por género
df.groupby("Genre")["Global_Sales"].sum().sort_values().plot(kind="pie", figsize=(10,6), color="steelblue")
plt.title("Ventas globales por género")
plt.xlabel("Millones de copias")
plt.tight_layout()
plt.show()

