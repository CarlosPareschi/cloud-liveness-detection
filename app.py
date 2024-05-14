from PIL import Image
import streamlit as st
from api import process_image, process_video

# Estilos da página
page_styles = """
<style>
/* Resetar o estilo padrão do Streamlit nos elementos raiz e principais */
body, #root, .stApp {
    background-color: #F5F5DC; /* Fundo */
    color: #1e4532; /* Texto branco */
}

/* Ajustar o tamanho e a cor do título */
h1 {
    color: #1e4532 !important; /* Verde metálico */
}

/* Estilo para a linha divisória */
.stHorizontal {
    background-color: #1e4532 !important; /* Verde metálico */
}

/* Ajustar a cor da fonte dos rótulos dos botões de rádio */
.stRadio label, .stSelectbox label, .stSlider label, .st.file_uploader, .stMultiSelect label, .stTextInput label {
    color: #1e4532 !important; /* Texto branco */
}

/* Ajustar a cor da fonte das palavras "Imagem" e "Vídeo" */
.stRadio label, .stSelectbox label {
    color: #1e4532 !important; /* Texto branco */
}

</style>
"""


st.markdown(page_styles, unsafe_allow_html=True)

# Layout para título e logo
col1, col2 = st.columns([3, 1])
with col1:
    st.title('Detecção de Vida em Nuvem')
with col2:
    st.image('logo.jpg', use_column_width=True)  # Ajustado para colocar o logotipo à direita

# Definição do aplicativo
# Escolha entre upload de imagem e vídeo
file_type = st.radio("Selecione o tipo de arquivo:", ("Imagem", "Vídeo"))

# Upload do arquivo via Streamlit
uploaded_file = st.file_uploader(f"Escolha um {file_type.lower()}...", type=["jpg", "jpeg", "png", "mp4"])

# Definição padrão do modelo e conjunto de dados
default_model = "EfficientNetAutoAttB4ST"
default_dataset = "DFDC"

# Limiar ajustável
threshold = st.slider("Selecione o Limiar", 0.0, 1.0, 0.5)

# Se o tipo de arquivo for vídeo, permita selecionar o número de frames
if file_type == "Vídeo":
    frames = st.slider("Selecione os Frames", 0, 100, 50)

# Exibir o arquivo carregado
if uploaded_file is not None:
    if file_type == "Imagem":
        # Exibir a imagem carregada
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Imagem Carregada", width=200)
        except Exception as e:
            print(e)
            st.error("Erro: Tipo de arquivo inválido")
    else:
        st.video(uploaded_file)

    # Verificar se o usuário deseja realizar a detecção de deepfake
    if st.button("Verificar Deepfake"):
        # Converter o arquivo para bytes para a solicitação da API
        if file_type == "Imagem":
            result, pred = process_image(image=uploaded_file, model=default_model, dataset=default_dataset, threshold=threshold)
            if result == 'real':
                pred = 100 - pred
            st.markdown(
                f'''
                <style>
                    .result {{
                        color: {'#ff4b4b' if result == 'fake' else '#6eb52f'};
                    }}
                </style>
                <h3>A {file_type.lower()} é: <span class="result"> {result} </span> com uma probabilidade de <span class="result">{pred:.2f}</span>%</h3>''', unsafe_allow_html=True)
        else:
            with open(f"uploads/{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.read())

            video_path = f"uploads/{uploaded_file.name}"
            result, pred = process_video(video_path, model=default_model, dataset=default_dataset, threshold=threshold, frames=frames)
            if result == 'real':
                pred = 100 - pred

            st.markdown(
                 f'''
                <style>
                    .result {{
                        color: {'#ff4b4b' if result == 'fake' else '#6eb52f'};
                    }}
                </style>
                <h3>O {file_type.lower()} é: <span class="result"> {result} </span> com uma probabilidade de <span class="result">{pred:.2f}</span>%</h3>''', unsafe_allow_html=True)
else:
    st.info("Por favor, faça upload de um arquivo.")

# Informações adicionais sobre o projeto
st.divider()

import streamlit as st

st.markdown(
    """
    <div style="text-align:center; background-color: #F5F5DC; color: #ffffff">
        <h2 style="color: #1e4532; font-weight: bold;">Informações do Projeto</h2>
        <p style="text-align: left; color: #1e4532; font-weight: bold;">Este aplicativo Streamlit aceita uma imagem ou um vídeo como entrada e prevê se é uma deepfake ou não.</p>
        <p style="text-align: left; color: #1e4532; font-weight: bold;">Projeto de conclusão da disciplina de Computer Vision do MBA em Data Science & IA da FIAP.</p>
    </div>
    """,
    unsafe_allow_html=True
)
