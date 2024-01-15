# Documentación del Modelo Conserje Inteligente  
### El conserje inteligente es un sistema de recomendación en hoteles, del servicio de habitación, eventos, aliementos y bebidas. En esta primera etapa nos centraremos en el perfil de usuarios y elementos (comidas y bebidas).

## Descripción del Modelo
### El modelo de recomendacióin utilizado, se basa en técnicas de procesamiento de lenguaje natural (NLP) y similitud del coseno para generar recomemdaciones personalizadas. 
### A continuación presentamos una breve descripción del modelo:
## 1. **Vectorización con TF-IDF:**
### **- TF-IDF (Term Frequency-Inverse Document Frequency):** es una técnica utilizada para convertir colecciones de texto en vectores numéricos. Se aplicaron tanto a perfiles de usuarios como 
### elementos (en este caso comidas y bebidas).
### **- Perfil de usuario:** Se crea un perfil para cada usuario en función de su historial de alimentación. Las descripcionews de las preferencias alimenticias se vectorizan utilizando TF-IDF,
### donde cada  palabra clave contribuye a la creación de un vector que representa el  perfil del usuario.
### **- Perfil del elemento:** Las descripciones  relevantes de las comidas y bebidas también se vectorian utilizando TF-IDF.  Cada elemento tiene su propio vector que representa sus caracteristicas
principales.

## **2. Similitud del Coseno:**
### **- Calculo de Similitud del Coseno:** Después de la vectorización, se calcula la similitud del coseno entre los perfiles de usuario y los perfiles de elemento. La similitud del coseno mide 
### la relación angular entre dos vectores y se utiliza para determinar cuán similares son los perfiles de usuario y los elementos.
### **- Generación de Recomendaciones:** Cuando un usuario solicita recomendaciones, el modelo encuentra elementos cuyos perfiles tienen una alta similitud del coseno con el perfill de usuario.
### Cuanto mayor sea la similitud del coseno, más cercanas son las preferencias del usuario a las características del elemento.

## Entrenamiento del Modelo
### El entrenamiento del modelo de recomendación se realiza en varias etapas, el cual involucra el procesamiento de datos y el cálulo de similitudes.

## **1. Procesamiento de Datos:**  
### **- Carga de Datos:** Utilizamos tres conjuntos de datos: datos de comidas ('comidas'), datos de usuarios ('usuarios') y datos de bebidas ('bebidas), los cuales combinamos en un conjunto de datos    
### final ('data_final')  
### **- Creación de perfiles:** Creamos perfiles de usuario y perfiles de elemento a partir de las categorías relevantes en el conjunto de datos finales. Los perfiles los creamos concatenando y     
### procesando las descripciones relevantes.  

## **2. Vectorización con TF-IDF:**
### **- Perfil de Usuario:** Aplicamos el vectorizador TF-IDF a las preferencias alimenticias de los usuarios para convertirlas en vectores numéricos.
### **- Perfil de Elemento:** Utilizamos  el mismo vectorizador TF-IDF para convertir las descripciones de comidas y bebidas en vectores.

## **3. Cálculo de Similitud del Coseno:**
### **- Similitud del Coseno:** Se calcula la similitud del coseno entre los perfiles de usuario y los perfiles de elemento utilizando los vectores generados con TF-IDF. Esto crea una matriz de similitud que representa cuán similares son los perfiles entre sí.

## **4. Generación de Recomendaciones:**
### **- Función de Recomendación:** Creamos una función de recomendación que toma un usuario como entrada y devuelve los elementos recomendados basándose en la similitud del coseno entre el perfil del usuario y   los perfiles de elemento.
### **- Top-N Recomendaciones:** Para un usuario dado, se seleccionan los elementos con la mayor similitud del coseno, y se devuelven como las principales recomendaciones para ese usuario.

