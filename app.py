"""A small Streamlit app that predicts an Iris flower species."""

import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


@st.cache_resource
def train_model():
    """Load the built-in Iris dataset and train a simple classifier once."""
    iris = load_iris()
    x_train, _, y_train, _ = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )
    model = DecisionTreeClassifier(random_state=42, max_depth=3)
    model.fit(x_train, y_train)
    return model, iris.target_names


st.set_page_config(page_title="Iris Flower Classifier", page_icon="🌸")
st.title("🌸 Iris Flower Classification")
st.write("Enter four flower measurements to predict its species.")

st.sidebar.header("Flower measurements (cm)")
sepal_length = st.sidebar.number_input("Sepal length", min_value=0.0, value=5.1, step=0.1)
sepal_width = st.sidebar.number_input("Sepal width", min_value=0.0, value=3.5, step=0.1)
petal_length = st.sidebar.number_input("Petal length", min_value=0.0, value=1.4, step=0.1)
petal_width = st.sidebar.number_input("Petal width", min_value=0.0, value=0.2, step=0.1)

if st.button("Predict flower species", type="primary"):
    model, species_names = train_model()
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0][prediction] * 100

    st.success(f"Prediction: **{species_names[prediction].title()}**")
    st.info(f"Model confidence: {confidence:.1f}%")

st.divider()
st.caption(
    "This project uses the Iris dataset included with scikit-learn and a Decision Tree classifier."
)
