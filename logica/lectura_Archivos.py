import pandas as pd

def lectura_archivos_exel(ruta):
    df = pd.read_excel(ruta)
    df = df.drop('Ventaja Principal',axis=1)
    df[['Localidad', 'Provincia']] = df['Lugar de Operación'].str.split('[/,(]', expand=True)
    df = df.drop('Lugar de Operación',axis=1)
    df["Velocidad (Mbps)"] = df["Velocidad (Mbps)"].str.replace(" Mbps", "").astype(float)
    print(df.head())

    return df

