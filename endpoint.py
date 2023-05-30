import requests
import csv

url = "https://dummyjson.com/quotes"
response = requests.get(url)
data = response.json()

#Obtener los valores de los campos "quote" y "author"
quotes = data["quotes"]
autor_texto = [(quote["author"], quote["quote"]) for quote in quotes]


#Guardar los valores en formato tabulado en el archivo endpoint.csv
with open("endpoint.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(autor_texto)

print("Datos guardados en endpoint.csv")