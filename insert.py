import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Read CSV
df = pd.read_csv("Income_expense_data.csv")

# MySQL Connection
password = quote_plus("kaushik@2006")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/FinancialDataBase"
)

# Insert into MySQL
df.to_sql(
    name="income_expense_data",
    con=engine,
    if_exists="replace",   # first time use replace
    index=False
)

print("Data inserted successfully!")