import pandas as pd
import re

file_path = "crimes-et-delits-enregistres-par-les-services-de-gendarmerie-et-de-police-depuis-2012.xlsx"

excel = pd.ExcelFile(file_path)

all_data = []

for sheet in excel.sheet_names:
    if "Présentation" in sheet:
        continue

    print("Traitement :", sheet)

    year = int(re.search(r"\d{4}", sheet).group())
    is_police = "PN" in sheet
    service = "Police nationale" if is_police else "Gendarmerie nationale"

    df = pd.read_excel(file_path, sheet_name=sheet, header=None)

    if is_police:
        header_dep   = df.iloc[0]
        header_per   = df.iloc[1]
        header_base  = df.iloc[2]
        df_data = df.iloc[3:].copy()
    else:
        header_dep   = df.iloc[0]   
        header_per   = None         
        header_base  = df.iloc[1]  
        df_data = df.iloc[2:].copy()

    df_data = df_data.rename(columns={0: "code_index", 1: "libelle"})

    rows = []

    for _, row in df_data.iterrows():
        code_index = row["code_index"]
        libelle = row["libelle"]

        if pd.isna(libelle):
            continue

        for col in range(2, len(df.columns)):
            value = row[col]

            if pd.notna(value) and str(value).strip().isdigit():
                if is_police:
                    departement = header_dep[col]
                    perimetre   = header_per[col] if pd.notna(header_per[col]) else None
                    base_brigade = header_base[col]
                else:
                    departement  = header_dep[col]
                    perimetre    = None
                    base_brigade = header_base[col]

                rows.append({
                    "annee":        year,
                    "service":      service,
                    "departement":  str(departement).strip() if pd.notna(departement) else None,
                    "perimetre":    str(perimetre).strip()   if perimetre is not None and pd.notna(perimetre) else None,
                    "base_brigade": str(base_brigade).strip() if pd.notna(base_brigade) else None,
                    "code_index":   code_index,
                    "libelle":      libelle,
                    "nombre_faits": int(value),
                })

    sheet_df = pd.DataFrame(rows)
    all_data.append(sheet_df)

final_df = pd.concat(all_data, ignore_index=True)
final_df = final_df[final_df["nombre_faits"] > 0]

final_df["annee"]        = final_df["annee"].astype("int16")
final_df["code_index"]   = final_df["code_index"].astype("int16")
final_df["nombre_faits"] = final_df["nombre_faits"].astype("int32")

output_path = "statistiques_normalisees.csv.gz"
final_df.to_csv(output_path, index=False, compression="gzip")

print(f"✅ Fichier généré : {output_path}")
print(f"   Lignes : {len(final_df):,}")
print(f"   Colonnes : {list(final_df.columns)}")

gn_sample = final_df[final_df["service"] == "Gendarmerie nationale"].head(3)
print("\nÉchantillon GN :")
print(gn_sample[["annee","service","departement","perimetre","base_brigade","libelle","nombre_faits"]].to_string())
