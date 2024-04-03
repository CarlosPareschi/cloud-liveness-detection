# Detecção de Vida em Nuvem

Acesse o projeto no streamlit sharing [aqui](https://cloud-liveness-detection.streamlit.app).

## Índice

- [Introdução](#introdução)
- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Dependências](#dependências)
- [Contribuindo](#contribuindo)
- [Agradecimentos](#agradecimentos)
- [Contato](#contato)

## Introdução

Bem-vindo ao repositório do Detecção de vida em nuvem! Este aplicativo Streamlit foi criado para identificar conteúdos falsificados, conhecidos como deepfakes, em imagens e vídeos, aplicando técnicas e modelos avançados. Oferece uma interface simples e intuitiva para que os usuários possam facilmente enviar seus arquivos e receber análises sobre a presença de deepfakes, com a possibilidade de ajustar os parâmetros de detecção conforme necessário.

# Parâmetros definidos:
 - Modelo: **EfficientNetAutoAttB4**
 - Conjunto de dados: **DFDC**

### Recursos

- **Seleção de Tipo de Arquivo**: Escolha entre fazer upload de uma imagem ou um vídeo para detecção de deepfake.
- **Limiar Ajustável**: Defina um limiar para a probabilidade de deepfake para controlar a sensibilidade.
- **Seleção de Quadros de Vídeo**: Se estiver analisando um vídeo, escolha o número de quadros para processar.
- **Resultados Detalhados**: Obtenha resultados detalhados com probabilidades e pistas visuais indicando a probabilidade de conteúdo deepfake.
- **Informação do Projeto**: Exiba informações adicionais sobre o projeto, como créditos, links para o GitHub e colaboradores.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/
```

2. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Uso

Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```
Visite a URL local fornecida para acessar o aplicativo no seu navegador.

## Estrutura de Arquivos
- **app.py**: Script principal para o aplicativo Streamlit.
- **api.py**: Inclui funções para analisar imagens e vídeos através de modelos específicos para identificação de deepfakes.
- **uploads/**: Diretório destinado ao armazenamento de arquivos enviados pelos usuários.
- **requirements.txt**: Relação de pacotes Python necessários para o projeto.

## Dependências
Para visualizar as dependências necessárias, acesse: [requirements.txt](https://github.com/CarlosPareschi/cloud-liveness-detection/blob/main/requirements.txt)

## Contato
Em caso de dúvidas ou sugestões, por favor, entre em contato com:
- [![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555&logoColor=white)](https://www.linkedin.com/in/carlos-alberto-pareschi/) Carlos Alberto Pareschi

