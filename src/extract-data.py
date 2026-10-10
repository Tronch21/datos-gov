import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)

results = client.get("h2jg-r3zg", limit=2000)

results_df = pd.DataFrame.from_records(results)

# Save the DataFrame to a Parquet file
results_df.to_parquet("data.parquet", engine="pyarrow", compression="zstd", index=False)

results_df["tipoentidad"] = pd.to_numeric(results_df["tipoentidad"], errors = 'coerce')
results_df["codigoentidad"] = pd.to_numeric(results_df["codigoentidad"], errors = 'coerce')
results_df["fechacorte"] = pd.to_datetime(results_df["fechacorte"])
results_df["cod_uca"] = pd.to_numeric(results_df["cod_uca"], errors = 'coerce')
results_df["subcuenta"] = pd.to_numeric(results_df["subcuenta"], errors = 'coerce')
results_df["persona_natural"] = pd.to_numeric(results_df["persona_natural"], errors = 'coerce')
results_df["persona_juridica"] = pd.to_numeric(results_df["persona_juridica"], errors = 'coerce')
results_df["total_tarjetas"] = pd.to_numeric(results_df["total_tarjetas"], errors = 'coerce')

print(results_df.head())