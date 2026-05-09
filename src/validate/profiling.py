import pandas as pd
from config.settings import RAW_DATA_DIR
from src.utils.logger import logger
from src.extract.loaders import load_dataset

# ==============================
# Selección de archivo
# ==============================

# archivo = "graduados_cac.xlsx"
# archivo = "graduados_ingles.xlsx"
# archivo = "graduados_tt.xlsx"
# archivo = "graduados_microcredenciales_historico.xlsx"
# archivo = "graduados_microcredenciales_2026.xlsx"
# archivo = "graduados_cfp.csv"
# archivo = "graduados_enof_historico.csv"
# archivo = "graduados_enof_2026_1.csv"
archivo = "egresados_sited_2026-04-23.csv"
# archivo = "graduados_secundarte.xlsx"

# ==============================
# Ruta
# ==============================

path = RAW_DATA_DIR / archivo

if not path.exists():
    raise FileNotFoundError(f"No se encontró el archivo en: {path}")

logger.info(f"Archivo seleccionado: {archivo}")

# ==============================
# Carga del dataset
# ==============================

df = load_dataset(path)
logger.info("Archivo cargado correctamente")

# ==============================
# Profiling básico
# ==============================

print("\n=== INFO GENERAL ===")
df.info()

print("\n=== COLUMNAS ===")
print(df.columns.tolist())

print("\n=== PRIMERAS FILAS ===")
print(df.head())
