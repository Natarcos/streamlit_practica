#PRIMERO IMPORTAMOS LAS LIBRERIAS A USAR
import streamlit as st
import pandas as pd
import plotly.express as px

#---------------------------------------------------------------------------
# Custom CSS for better styling
def local_css():
    st.markdown("""
    <style>
        /* Main container styling */
        .main {
            padding: 2rem;
            border-radius: 10px;
            background-color: #f8f9fa;
        }
        
        /* Card styling for columns */
        .stImage {
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        .stImage:hover {
            transform: translateY(-5px);
        }
        
        /* Custom headers */
        h1, h2, h3 {
            color: #1E88E5;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #f1f3f4;
            border-radius: 5px 5px 0px 0px;
            padding-left: 20px;
            padding-right: 20px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #1E88E5 !important;
            color: white !important;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f1f3f4;
        }
        
        /* Dataframe styling */
        .dataframe {
            border-collapse: collapse;
            width: 100%;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .dataframe th {
            background-color: #1E88E5;
            color: white;
            padding: 12px;
            text-align: left;
        }
        .dataframe td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        .dataframe tr:hover {
            background-color: #f2f2f2;
        }
    </style>
    """, unsafe_allow_html=True)

#SETUP DE LA APP 
# De layout podemos usar wide or centered
st.set_page_config(page_title="Mi primera app", page_icon=":tada:", layout="centered")

# Apply custom CSS
local_css()

#---------------------------------------------------------------------------
# Custom header with logo and title
st.markdown("""
    <div style="display: flex; align-items: center; background-color: #ffffff; padding: 1rem; border-radius: 10px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <img src="https://www.streamlit.io/images/brand/streamlit-mark-color.png" style="width: 60px; margin-right: 20px;">
        <div>
            <h1 style="margin: 0; color: #1E88E5; font-size: 2rem;">Mi Primera App</h1>
            <p style="margin: 0; color: #666;">Análisis de datos profesional</p>
        </div>
    </div>
""", unsafe_allow_html=True)

#---------------------------------------------------------------------------
#sidebars
st.sidebar.markdown("""
    <div style="text-align: center; padding-bottom: 20px;">
        <img src="https://www.streamlit.io/images/brand/streamlit-mark-color.png" width="150">
    </div>
""", unsafe_allow_html=True)
st.sidebar.title("Empresa X") # Titulo de la sidebar
st.sidebar.markdown("""
    <div style="background-color: white; padding: 15px; border-radius: 5px; margin-top: 20px;">
        <p>Bienvenido a nuestra aplicación de análisis. Utilice las opciones a continuación para personalizar su experiencia.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar options (new)
st.sidebar.markdown("### Opciones")
st.sidebar.checkbox("Mostrar datos avanzados")
st.sidebar.selectbox("Seleccionar periodo", ["Diario", "Semanal", "Mensual", "Anual"])
st.sidebar.slider("Nivel de detalle", 0, 100, 50)

#---------------------------------------------------------------------------
# Metrics row (new)
st.markdown("### Indicadores clave")
col_metrics1, col_metrics2, col_metrics3, col_metrics4 = st.columns(4)
col_metrics1.metric(label="Ventas", value="$12,456", delta="+4.5%")
col_metrics2.metric(label="Usuarios", value="1,234", delta="+11.2%")
col_metrics3.metric(label="Conversión", value="3.2%", delta="-0.5%")
col_metrics4.metric(label="Tiempo medio", value="2:34 min", delta="+0.8%")

#---------------------------------------------------------------------------
#Columnas
st.markdown("### Nuestros servicios")
col1, col2, col3 = st.columns(3) # 3 columnas

with col1:
    st.markdown("""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; height: 250px;">
        <img src="https://www.streamlit.io/images/brand/streamlit-mark-color.png" width="100">
        <h3>Análisis de datos</h3>
        <p>Convierte tus datos en información accionable</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; height: 250px;">
        <img src="https://www.streamlit.io/images/brand/streamlit-mark-color.png" width="100">
        <h3>Visualización</h3>
        <p>Gráficos interactivos para mejor comprensión</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; height: 250px;">
        <img src="https://www.streamlit.io/images/brand/streamlit-mark-color.png" width="100">
        <h3>Machine Learning</h3>
        <p>Modelos predictivos para tu negocio</p>
    </div>
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------
#pestañas
st.markdown("### Contenido principal")
tab1, tab2, tab3 = st.tabs(["📝 Textos", "📊 Medios y recursos", "🔢 Dataframe"])

with tab1:
    #TEXTOS
    st.header("Textos y elementos de UI") 

    # Two column layout for better organization
    col_text1, col_text2 = st.columns(2)
    
    with col_text1:
        st.subheader("Formatos de texto")
        st.markdown("Texto normal para párrafos informativos.")
        st.markdown("**Texto en negrita** para énfasis")
        st.markdown("*Texto en cursiva* para destacar conceptos")
        st.code("print('Hola mundo')", language="python")
        st.latex(r"""a^2 + b^2 = c^2""")
    
    with col_text2:
        st.subheader("Notificaciones")
        st.info("📝 Esto es una información importante")
        st.success("✅ Operación completada con éxito")
        st.warning("⚠️ Precaución: acción requerida")
        st.error("❌ Ha ocurrido un error")
        st.exception("Exception: División por cero")


with tab2:
    # Medios y recursos
    col_media1, col_media2 = st.columns(2)
    
    with col_media1:
        st.subheader("Imagen del producto")
        st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=250)
        st.markdown("""
        <div style="background-color: white; padding: 15px; border-radius: 5px;">
            <p>Nuestro producto ha sido diseñado con las últimas tecnologías para garantizar la mejor experiencia al usuario.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_media2:
        st.subheader("Demostración de audio")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
        st.subheader("Video explicativo")
        st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")


with tab3:
    st.subheader("Análisis de datos")
    
    # Crear un dataframe más interesante
    df = pd.DataFrame({
        "Producto": ["Laptop", "Smartphone", "Tablet", "Monitor"],
        "Ventas": [1254, 1896, 657, 824],
        "Crecimiento": ["+12.3%", "+7.8%", "-2.3%", "+4.5%"],
        "Satisfacción": [4.7, 4.2, 3.9, 4.5]
    })

    col_df1, col_df2 = st.columns([3, 2])
    
    with col_df1:
        st.markdown("### Datos de ventas")
        st.dataframe(df, use_container_width=True)
    
    with col_df2:
        st.markdown("### Gráfico de ventas")
        fig = px.bar(df, x='Producto', y='Ventas', color='Satisfacción',
                     color_continuous_scale='blues',
                     title="Ventas por producto")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Añadir filtros interactivos
    st.markdown("### Filtros")
    col_filter1, col_filter2 = st.columns(2)
    with col_filter1:
        producto_filter = st.multiselect("Seleccionar productos", options=df["Producto"].tolist(), default=df["Producto"].tolist())
    with col_filter2:
        min_ventas = st.slider("Ventas mínimas", 0, 2000, 500)