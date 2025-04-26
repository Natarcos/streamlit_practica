#PRIMERO IMPORTAMOS LAS LIBRERIAS A USAR
import streamlit as st
import pandas as pd

#---------------------------------------------------------------------------

#SETUP DE LA APP 
# De layout podemos usar wide or centered
st.set_page_config(page_title="Mi primera app", page_icon=":tada:", layout="centered")


#---------------------------------------------------------------------------
#sidebars
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png",  width=200)
st.sidebar.title("empresa x") # Titulo de la sidebar
st.sidebar.text("Hola mundo") # Texto normal

#---------------------------------------------------------------------------
#Columnas
col1, col2, col3 = st.columns(3) # 3 columnas

with col1:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", width=200)

with col2:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", width=200)


with col3:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", width=200)

#---------------------------------------------------------------------------
#pestañas

tab1, tab2, tab3 = st.tabs(["textos", "medios y recursos", "dataframe"])

with tab1:

    #TEXTOS
    st.title("Mi primera app") # Titulo principal

    #Encabezados 
    st.header("Encabezado 1") # Encabezado 1
    st.subheader("Encabezado 2") # Encabezado 2

    #texto normal 
    st.text("Hola mundo") # Texto normal

    #markdown
    st.markdown("Hola **mundo**") # Texto en markdown

    #latex
    st.latex(r"""a^2 + b^2 = c^2""") # Texto en latex

    #code 
    st.code("print('Hola mundo')", language="python") # Texto en code

    #Informacion, advertencias y errores
    st.info("Esto es una info") # Info
    st.success("Esto es un success") # Success
    st.warning("Esto es un warning") # Warning
    st.error("Esto es un error") # Error
    st.exception("Esto es una exception") # Exception


with tab2:
    # Medios y recursos
    # Imagenes (la ruta puede ser local o una url)
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", width=200)

    #audios
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3") # Audio

    #videos
    st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g") # Video


with tab3:

    #Dataframe ejemplo
    df = pd.DataFrame({
        "col1": [1, 2, 3, 4],
        "col2": [5, 6, 7, 8],
        "col3": [9, 10, 11, 12]
    })

    st.dataframe(df) # Dataframe

#---------------------------------------------------------------------------
# Sessions states son variables que se mantienen en la sesion
# Se pueden usar para guardar datos entre sesiones

#crear contador en estado de sesion
if 'contador' not in st.session_state:
    st.session_state.contador = 0

#funciones auxiliares para incrementar, decrementar y resetear el contador
def incrementa_contador():
    st.session_state.contador += 1

def decrementa_contador():
    st.session_state.contador -= 1

def reset_contador():
    st.session_state.contador = 0

#inferfaz
st.title("Contador")
st.write("Contador:", st.session_state.contador) # Mostrar contador

#botones para incrementar, decrementar y resetear el contador
col1, col2, col3 = st.columns(3) # 3 columnas

with col1:
    if st.button("Incrementar"):
        incrementa_contador() # Incrementar contador

with col2:
    if st.button("Decrementar"):
        decrementa_contador() # Decrementar contador

with col3:
    if st.button("Resetear"):
        reset_contador() # Resetear contador


#---------------------------------------------------------------------------
    

