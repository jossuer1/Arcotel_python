def insertar_datos(conn, df):
    cursor = None

    try:
        # Crear cursor para ejecutar SQL
        cursor = conn.cursor()

        # Query de inserción
        query = """
        INSERT INTO empresa (
            Empresa,
            Tecnologia,
            Velocidad_Mbps,
            Costo_Mensual_Est,
            Costo_por_Mbps,
            Localidad,
            Provincia
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Seleccionar columnas del DataFrame y convertir a tuplas
        data = df[[
            "Empresa",
            "Tecnología",
            "Velocidad (Mbps)",
            "Costo Mensual (Est.)",
            "Costo por Mbps",
            "Localidad",
            "Provincia"
        ]].to_numpy()

        # Ejecutar inserción masiva
        cursor.executemany(query, data)

        # Confirmar cambios en la base de datos
        conn.commit()

        print("Datos insertados correctamente")

    except Exception as e:
        print("Error al insertar datos:", e)
        conn.rollback()

    finally:
        if cursor:
            cursor.close()