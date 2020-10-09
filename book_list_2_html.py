import pandas as pd 

filePath = "D:\\Documents\\Lista de Livros.xlsx"

sheet_list = ["Livros", "Banda Desenhada", "Coleções BD", "Manuais", "eBooks"]

df_books = pd.read_excel(filePath, sheet_name=sheet_list[0])

cols = df_books.columns.values

cols = [cols[0], cols[1], cols[2], cols[3]]


df_books = df_books[cols]
df_books = df_books.fillna("-")

print(df_books.head(5))

#df_books.to_html("test.html")

html = df_books.to_html()

with open("dataframe.html", "w", encoding="utf-8") as file:
    file.writelines('<meta charset="UTF-8">\n')
    file.write(html)