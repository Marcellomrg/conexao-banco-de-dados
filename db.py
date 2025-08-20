# %%
import pandas as pd
import sqlalchemy
# %%
# criando minha conexao
engine = sqlalchemy.create_engine("sqlite:///data/olist.db")
# %%
# lendo minha tabela do banco de dados
df = pd.read_sql_table("tb_sellers",con=engine)
df
# %%
# lendo meu arquivo com a query 
with open("./htl.sql") as open_file:
    open_file = open_file.read()
#Recendo meus dados do banco de dados da minha query
query = pd.read_sql_query(sql=open_file,con=engine)
# %%
query

# %%
