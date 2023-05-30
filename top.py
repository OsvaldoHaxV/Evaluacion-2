import re
from collections import Counter

# Leer el archivo endpoint.csv
with open('endpoint.csv', 'r') as file:
    # Leer todas las líneas del archivo
    lines = file.readlines()

# Crear una lista para almacenar todas las palabras
words = []

# Recorrer las líneas y extraer las palabras del campo "texto"
for line in lines[1:]:
    # Utilizar expresiones regulares para encontrar las palabras
    line = line.strip().split('\t')
    text = line[1]
    text = re.sub(r'[^\w\s]', '', text)  # Remover signos de puntuación
    words.extend(text.lower().split())

# Definir una lista de palabras a excluir (artículos y conectores)
excluded_words = ["a", "an", "the", "and", "or", "but", "in", "on", "at", "to"]

# Contar la frecuencia de las palabras excluyendo las palabras excluidas
word_counts = Counter(word for word in words if word not in excluded_words)

# Obtener el ranking top ten de las palabras más repetidas
top_ten = word_counts.most_common(10)

# Imprimir el ranking top ten
print("Ranking top ten de palabras más repetidas:")
for word, count in top_ten:
    print(f"{word}: {count}")
