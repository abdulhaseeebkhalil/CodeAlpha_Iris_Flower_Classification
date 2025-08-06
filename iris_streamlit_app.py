import streamlit as st
import pickle
import numpy as np

# Custom CSS for background and fonts
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 30px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #6a11cb;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 2em;
        font-size: 1.1em;
    }
    .stButton>button:hover {
        background-color: #2575fc;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", use_column_width=True)
st.sidebar.title("🌸 Iris Classifier Project")
st.sidebar.markdown("""
**Author:** Abdul Haseeb  
[GitHub](https://github.com/) | [Dataset Source](https://www.kaggle.com/datasets/uciml/iris)
""")

# Main content
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.title("🌺 Iris Flower Species Classifier")
    st.markdown("""
    <h4>Predict the species of an Iris flower by entering its measurements below.</h4>
    <ul>
        <li>Setosa 🌱</li>
        <li>Versicolor 🌷</li>
        <li>Virginica 🌸</li>
    </ul>
    """, unsafe_allow_html=True)

    # Load the trained model
    with open('iris_knn_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Input fields in columns
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, max_value=10.0, value=5.1, step=0.1)
        petal_length = st.number_input('Petal Length (cm)', min_value=0.0, max_value=10.0, value=1.4, step=0.1)
    with col2:
        sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, max_value=10.0, value=3.5, step=0.1)
        petal_width = st.number_input('Petal Width (cm)', min_value=0.0, max_value=10.0, value=0.2, step=0.1)

    # Predict button
    if st.button('🔮 Predict Species'):
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)[0]
        emoji = {"Iris-setosa": "🌱", "Iris-versicolor": "🌷", "Iris-virginica": "🌸"}
        color = {"Iris-setosa": "#a8e063", "Iris-versicolor": "#f7971e", "Iris-virginica": "#f953c6"}
        st.markdown(
            f"<div style='background-color:{color.get(prediction, '#fff')};"
            "padding:1.5em;border-radius:12px;text-align:center;font-size:1.5em;'>"
            f"Predicted species: <b>{prediction}</b> {emoji.get(prediction, '')}</div>",
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)