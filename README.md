# Documentación del Modelo Conserje Inteligente
### El conserje inteligente es un sistema de recomendación en hoteles, del servicio de habitación, eventos, aliementos y bebidas. En esta primera etapa nos centraremos en el perfil de usuarios y elementos (comidas y bebidas).

## Descripción del modelo
### El modelo de recomendacióin utilizado, se basa en técnicas de procesamiento de lenguaje natural (NLP) y similitud del coseno para generar recomemdaciones personalizadas. 
### A continuación presentamos una breve descripción del modelo:
## 1) Vectorización con TF-IDF:
### **- TF-IDF (Term Frequency-Inverse Document Frequency):** es una técnica utilizada para convertir colecciones de texto en vectores numéricos. Se aplicaron tanto a perfiles de usuarios como 
### elementos (en este caso comidas y bebidas).
### **- Perfil de usuario:** Se crea un perfil para cada usuario en función de su historial de alimentación. Las descripcionews de las preferencias alimenticias se vectorizan utilizando TF-IDF,
### donde cada  palabra clave contribuye a la creación de un vector que representa el  perfil del usuario.
### **- Perfil del elemento:** Las descripciones  relevantes de las comidas y bebidas también se vectorian utilizando TF-IDF.  Cada elemento tiene su propio vector que representa sus caracteristicas
### principales.
