def run_basic_profile(df):

    print("\n=== INFO GENERAL ===")
    df.info()

    print("\n=== COLUMNAS ===")
    print(df.columns.tolist())

    print("\n=== PRIMERAS FILAS ===")
    print(df.head())