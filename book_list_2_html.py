import pandas as pd 

filePath = "D:\\Documents\\Lista de Livros.xlsx"

sheet_list = ["Livros", "Banda Desenhada", "Coleções BD", "Manuais", "eBooks"]

df_books = pd.read_excel(filePath, sheet_name=sheet_list[0])
df_bd = pd.read_excel(filePath, sheet_name=sheet_list[1])
df_collect = pd.read_excel(filePath, sheet_name=sheet_list[2])
df_textbook = pd.read_excel(filePath, sheet_name=sheet_list[3])

df_list = [df_books, df_bd, df_collect, df_textbook]

cols = df_books.columns.values

cols = [cols[0], cols[1], cols[2], cols[3]]

i = 0

for df in df_list:
    df = df[cols]
    df = df.fillna("-")
    
    html = df.to_html(index=False)

    fileName = "df_"+str(i)+".html"

    with open(fileName, 'w', encoding='utf-8') as f:
        f.writelines('<meta charset="UTF-8">\n')
        f.writelines('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n') 
        f.write(html)
    i += 1