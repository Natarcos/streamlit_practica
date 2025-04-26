import streamlit as st
import pandas as pd
import plotly.express as px

# App configuration
st.set_page_config(page_title="Mi primera app", page_icon=":tada", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    
    /* Headers */
    .css-10trblm {
        color: #1f2937;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: 1.5rem;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #ffffff;
        padding: 2rem;
        border-right: 1px solid #e5e7eb;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: #ffffff;
        border-radius: 0.5rem;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #4b5563;
        border-radius: 0.25rem;
        padding: 0.5rem 1rem;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
        color: white;
    }
    
    /* Cards for columns */
    .stColumn {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin: 0.5rem;
    }
    
    /* Dataframe styling */
    .dataframe {
        border: none;
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Alert boxes */
    .stAlert {
        border-radius: 0.5rem;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", width=200)
    st.markdown("### Dashboard")
    st.text("Bienvenido a la aplicación")

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Textos", "🎯 Medios", "📊 Datos"])

with tab1:
    st.markdown("<h1 style='text-align: center;'>Mi primera app</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.header("Encabezado 1")
        st.subheader("Encabezado 2")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Texto y código")
            st.markdown("Hola **mundo**")
            st.code("print('Hola mundo')", language='python')
            
        with col2:
            st.markdown("### Matemáticas")
            st.latex(r"""a^2 + b^2 = c^2""")
    
    # Alerts in a more organized way
    with st.container():
        st.markdown("### Alertas")
        cols = st.columns(2)
        with cols[0]:
            st.info("Información importante")
            st.success("Operación exitosa")
        with cols[1]:
            st.warning("Precaución")
            st.error("Error detectado")

with tab2:
    st.markdown("<h2 style='text-align: center;'>Recursos multimedia</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", 
                caption="Streamlit", 
                use_column_width=True)
    with col2:
        st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")

with tab3:
    st.markdown("<h2 style='text-align: center;'>Análisis de datos</h2>", unsafe_allow_html=True)
    
    df = pd.DataFrame({
        "col1": [1,2,3,4],
        "col2": [5,6,7,8],
        "col3": [8,10,11,12]
    })
    
    st.dataframe(df.style.highlight_max(axis=0))

# Footer
st.markdown("""
    <div style='text-align: center; padding: 1rem; margin-top: 2rem; border-top: 1px solid #e5e7eb;'>
        <p style='color: #6b7280;'>Desarrollado con ❤️ usando Streamlit</p>
    </div>
""", unsafe_allow_html=True)

# Añadir filtros interactivos
st.markdown("### Filtros")
col_filter1, col_filter2 = st.columns(2)
with col_filter1:
    producto_filter = st.multiselect("Seleccionar productos", options=df["Producto"].tolist(), default=df["Producto"].tolist())
with col_filter2:
    min_ventas = st.slider("Ventas mínimas", 0, 2000, 500)
    

