import pandas as pd


def load_dataset(path):

    file_name = path.name.lower()

    # ==============================
    # Excel files
    # ==============================

    if file_name.endswith(".xlsx"):

        # Caso especial: microcredenciales con múltiples hojas
        if "microcredenciales_2026" in file_name:

            xls = pd.ExcelFile(path)
            latest_sheet = xls.sheet_names[-1]

            print(f"Procesando hoja: {latest_sheet}")

            df = pd.read_excel(path, sheet_name=latest_sheet)

        else:
            df = pd.read_excel(path)

    # ==============================
    # CSV files
    # ==============================

    elif file_name.endswith(".csv"):

        # ENOF / SIENFO → separador ;
        if "enof" in file_name or "sienfo" in file_name:

            df = pd.read_csv(
                path,
                sep=";",
                dtype=str,
                low_memory=False
            )

        # CFP → separador ,
        elif "cfp" in file_name:

            df = pd.read_csv(
                path,
                sep=",",
                dtype=str,
                low_memory=False
            )

        # fallback
        else:

            df = pd.read_csv(
                path,
                dtype=str,
                low_memory=False
            )

    else:
        raise ValueError(
            f"Formato de archivo no soportado: {path.name}"
        )

    return df