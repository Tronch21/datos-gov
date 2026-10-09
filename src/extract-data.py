import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)

# client = Socrata("https://www.datos.gov.co/api/v3/views/h2jg-r3zg/query.json",
#                MyAppTokenHere,
#                username="davidfsalgadog3@gmail.com",
#                password="Holamundo24028" )

results = client.get("h2jg-r3zg", limit=2000)

df = pd.read_parquet("datos.parquet", columns=["NOMBREENTIDAD", "PERSONA_NATURAL", "PERSONA_JURIDICA"])

print(df)

results_df = pd.DataFrame.from_records(results)

print(results_df.head())