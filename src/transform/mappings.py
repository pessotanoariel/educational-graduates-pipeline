"""Mapping definitions for schema standardization."""

COLUMN_MAPPINGS = {

    # ==============================
    # Document Information
    # ==============================

    "Tipo de documento": "document_type",
    "tipo_doc": "document_type",
    "tipo_documento": "document_type",
    "tipodoc": "document_type",

    "Nro de documento": "document_number",
    "nro_doc": "document_number",
    "numero_documento": "document_number",
    "nrodoc": "document_number",
    "DNI": "document_number",
    "dni": "document_number",
    "nro_documento": "document_number",

    # ==============================
    # Personal Information
    # ==============================

    "Nombre Estudiante": "full_name",
    "apellido_nombre": "full_name",
    "apenom": "full_name",

    "nombre": "first_name",
    "nombres": "first_name",

    "apellido": "last_name",
    "apellidos": "last_name",

    "Genero": "gender",
    "genero": "gender",
    "sexo": "gender",

    "fecha_nacimiento": "birth_date",
    "fecha_nac": "birth_date",
    "fechanac": "birth_date",

    "mail": "email",
    "email": "email",
    "recipient": "email",

    "celular": "phone_number",
    "telefono": "phone_number",

    "nacionalidad": "nationality",

    "jurisdiccion": "jurisdiction",
    "provincia": "jurisdiction",

    # ==============================
    # Academic Information
    # ==============================

    "egresado": "graduated",

    "oferta": "offer",
    "Indicador título y Orientación": "offer",
    "nom_curso": "offer",
    "badge_name": "offer",

    "tipo_oferta": "offer_type",
    
    # SiTED educational sector classification
    "Área educativa": "education_sector",

    "Nombre establecimiento": "institution_name",
    "ubicacion": "institution_name",
    "nom_centro_xc": "institution_name",
    "programa": "institution_name",

    "periodo": "academic_period",

    "año": "academic_year",
    "anio": "academic_year",
}

# ==============================
# Gender Value Mapping
# ==============================

GENDER_MAPPING = {

    "m": "masculino",
    "masculino": "masculino",

    "f": "femenino",
    "femenino": "femenino",

    "x": "no_binario",
    "otro": "no_binario",
    "no_binario": "no_binario",

    "sin_datos": "sin_datos",
    "sin datos": "sin_datos"
}