# 🌸 Iris Flower Classification Project

Welcome to the **Iris Flower Classification** project! This project demonstrates how to use machine learning to classify iris flowers into three species—Setosa, Versicolor, and Virginica—based on their physical measurements. It includes a Jupyter notebook for model training and a beautiful Streamlit web app for interactive predictions.

---

## 📂 Project Structure

```
CodeAlpha_Iris_Flower_Classification/
│
├── Dataset/
│   └── Iris.csv
├── Iris_Flower_Classification.ipynb
├── iris_knn_model.pkl
├── iris_streamlit_app.py
└── README.md
```

---

## 📊 Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/uciml/iris)
- **File:** `Dataset/Iris.csv`
- **Features:**
  - `SepalLengthCm`
  - `SepalWidthCm`
  - `PetalLengthCm`
  - `PetalWidthCm`
- **Target:** `Species` (Setosa, Versicolor, Virginica)

---

## 🤖 Model & Approach
- **Algorithm:** K-Nearest Neighbors (KNN)
- **Libraries:** pandas, scikit-learn, numpy, pickle, streamlit
- **Workflow:**
  1. Load and preprocess the data
  2. Split into training and test sets
  3. Train a KNN classifier
  4. Evaluate accuracy and performance
  5. Save the trained model as a pickle file
  6. Build a Streamlit UI for real-time predictions

---

## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone <your-repo-url>
cd CodeAlpha_Iris_Flower_Classification
```

### 2. **Install Requirements**
```bash
pip install -r requirements.txt
```
Or, install manually:
```bash
pip install pandas scikit-learn numpy streamlit
```

### 3. **Run the Jupyter Notebook**
Open `Iris_Flower_Classification.ipynb` in Jupyter Notebook or JupyterLab to see data exploration, model training, and evaluation.

### 4. **Run the Streamlit App**
```bash
streamlit run iris_streamlit_app.py
```
- Enter flower measurements in the UI
- Click **Predict Species** to see the result with beautiful visuals

---

## 🖥️ Screenshots
## 🖥️ Screenshots

Here’s how the Streamlit app looks:

![Streamlit App Screenshot](D:/Internships/CodeAlpha/Project/CodeAlpha_Iris_Flower_Classification/images/main-dashboard.png)
---

## 📝 Requirements
- Python 3.7+
- pandas
- scikit-learn
- numpy
- streamlit

---

## 🙏 Credits
- **Dataset:** Kaggle
- **Author:** Abdul Haseeb
- **UI Inspiration:** Streamlit community

---

## 📬 Contact
For questions or feedback, please open an issue or contact [abdulhaseeb13095@gmail.com](mailto:abdulhaseeb13095@gmail.com).

---

Enjoy classifying Iris flowers! 🌸🌱🌷