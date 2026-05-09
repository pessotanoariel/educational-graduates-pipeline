import pandas as pd
from config.settings import RAW_DATA_DIR

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

print(f"Archivo seleccionado: {archivo}")

# ==============================
# Carga del dataset
# ==============================

if archivo.endswith(".xlsx"):

    # Caso especial: microcredenciales con múltiples hojas
    if "microcredenciales_2026" in archivo:
        xls = pd.ExcelFile(path)
        sheet_ultima = xls.sheet_names[-1]
        print(f"Procesando hoja: {sheet_ultima}")
        df = pd.read_excel(path, sheet_name=sheet_ultima)
    else:
        df = pd.read_excel(path)

elif archivo.endswith(".csv"):

    # ENOF / SIENFO → separador ;
    if "enof" in archivo or "sienfo" in archivo:
        df = pd.read_csv(path, sep=";", dtype=str, low_memory=False)

    # CFP (query SQL / DBeaver) → separador ,
    elif "cfp" in archivo:
        df = pd.read_csv(path, sep=",", dtype=str, low_memory=False)

    # fallback (otros CSV)
    else:
        df = pd.read_csv(path, dtype=str, low_memory=False)

else:
    raise ValueError(f"Formato de archivo no soportado: {archivo}")

print("Archivo cargado correctamente ✔")

# ==============================
# Profiling básico
# ==============================

print("\n=== INFO GENERAL ===")
df.info()

print("\n=== COLUMNAS ===")
print(df.columns.tolist())

print("\n=== PRIMERAS FILAS ===")
print(df.head())
