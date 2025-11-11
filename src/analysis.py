import os
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")

df = pd.read_sql("SELECT * FROM test_data", DATABASE_URL)

print(df.head())
