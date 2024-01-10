
# Función para cargar los datos
def cargar_datos():
    comidas = pd.read_csv("Comidas - comidas-villa-magna.csv")
    usuarios = pd.read_csv("Usuarios - usuarios-villa-magna.csv")
    bebidas = pd.read_csv("Bebidas - bebidas-villa-magna.csv")

    # Unimos todas las tablas en una sola
    data_final = pd.concat([comidas, usuarios, bebidas])

    # Lista de columnas a eliminar
    columnas_a_eliminar = ['_Id', 'User_email', 'User_pass']

    # Elimina las columnas del DataFrame
    data_final = data_final.drop(columns=columnas_a_eliminar)

    # Llenamos NaN en las columnas relevantes
    data_final = data_final.fillna('')

    return data_final

# Función para generar matrices
def generar_matrices(data_final):
    # Crear perfiles de usuario y elementos
    perfiles_usuario = data_final[['User_name', 'Alimentacion']]
    perfiles_elemento = data_final[['Plato_name', 'Plato_tipo', 'Bebida_name', 'Tipo_bebida']]

    # Creamos perfiles de usuario y elementos
    perfiles_usuario = data_final[['User_name', 'Alimentacion']]
    perfiles_elemento['Perfil'] = perfiles_elemento[['Plato_name', 'Plato_tipo', 'Bebida_name', 'Tipo_bebida']].apply(lambda x: ' '.join(str(val) for val in x), axis=1)

    perfiles_usuario = perfiles_usuario.astype(str)
    perfiles_elemento = perfiles_elemento.astype(str)

    # Elimina duplicados
    perfiles_elemento.drop_duplicates(subset='Perfil', inplace=True)

    # Reemplazar NaN con una cadena vacía ('') antes de aplicar el vectorizador
    perfiles_usuario['Alimentacion'].fillna('', inplace=True)
    perfiles_elemento.fillna('', inplace=True)

    # Hacer una copia explícita para evitar SettingWithCopyWarning
    perfiles_usuario = perfiles_usuario.copy()
    perfiles_elemento = perfiles_elemento.copy()

    # Concatenamos las descripciones relevantes para el vectorizador TF-IDF
    perfiles_usuario.loc[:, 'Perfil'] = perfiles_usuario['Alimentacion']
    perfiles_elemento.loc[:, 'Perfil'] = perfiles_elemento.apply(lambda x: ' '.join(str(val) for val in x), axis=1)

    return perfiles_usuario, perfiles_elemento

# Función para calcular la similitud de coseno
def calcular_similitud(perfiles_usuario, perfiles_elemento):
    # Usamos el vectorizador TF-IDF para convertir las descripciones en vectores
    vectorizer = TfidfVectorizer(stop_words='english')
    perfil_matrix = vectorizer.fit_transform(perfiles_usuario['Perfil'])
    elemento_matrix = vectorizer.transform(perfiles_elemento['Perfil'])

    # Calculamos similitud de coseno entre perfiles de usuario y elementos
    cosine_similarities = linear_kernel(perfil_matrix, elemento_matrix)

    # Creamos un DataFrame con las similitudes
    similarity_df = pd.DataFrame(cosine_similarities, index=perfiles_usuario['User_name'], columns=perfiles_elemento.index)

    return similarity_df

# Función para recomendar elementos a un usuario
def recomendar_elementos(usuario, similarity_df, perfiles_elemento, top_n=5):
    if usuario in similarity_df.index:
        recomendaciones_indices = similarity_df.loc[usuario].sort_values(ascending=False).head(top_n).index
        recomendaciones_nombres = perfiles_elemento.loc[recomendaciones_indices, 'Perfil']
        return recomendaciones_nombres
    else:
        return []

# Cargar datos y generar matrices
data_final = cargar_datos()
perfiles_usuario, perfiles_elemento = generar_matrices(data_final)
similarity_df = calcular_similitud(perfiles_usuario, perfiles_elemento)

# Ejemplo de cómo usar la función de recomendación
usuario_ejemplo = 'Usuario_009'
recomendaciones_usuario = recomendar_elementos(usuario_ejemplo, similarity_df, perfiles_elemento)
print(f"Recomendaciones para {usuario_ejemplo}: {recomendaciones_usuario}")
