def build_operational_dataset(df):
    """Build operational dataset for downstream systems."""

    operational_df = df.copy()

    # Operational dataset only contains graduates.
    # Graduation status is therefore always true ("T").

    operational_df["graduated"] = "T"

    operational_df["clave_persona"] = (
        operational_df["document_type"]
        + "_"
        + operational_df["document_number"]
    )

    operational_df = operational_df[
        operational_df["document_number"]
        .fillna("")
        .str.strip()
        != ""
    ]

    operational_df = operational_df[
        [
            "clave_persona",
            "document_type",
            "document_number",
            "gender",
            "full_name",
            "graduated"
        ]
    ]

    operational_df["gender"] = (
        operational_df["gender"]
        .fillna("sin_datos")
    )

    operational_df = operational_df.rename(
        columns={
            "document_type": "tipo_doc",
            "document_number": "nro_doc",
            "gender": "genero",
            "full_name": "nombre_apellido",
            "graduated": "egresado"
        }
    )

    return operational_df