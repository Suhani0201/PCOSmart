# PCOSmart
Early PCOS Risk Detection using ML | EDA, feature analysis, classifier comparison, and Streamlit-based UI for personalized risk prediction.
COSmart: Early Detection of PCOS Risk using ML

**PCOSmart** is an end-to-end machine learning project focused on the **early prediction and risk analysis of Polycystic Ovary Syndrome (PCOS)**. It combines robust EDA, statistical insights, classifier benchmarking, and a Streamlit-based UI to deliver a user-friendly prediction system.

---

## 📌 What is PCOS?

Polycystic Ovary Syndrome (PCOS) is a hormonal disorder common among women of reproductive age. Early detection can reduce long-term complications like infertility, metabolic syndrome, and type 2 diabetes.

---

## 🌟 Key Features

- 📊 **EDA & Statistical Analysis** to identify most reactive features
- 🤖 **Comparative Study of Classifiers**: SVM, Random Forest, XGBoost, etc.
- 📈 **Feature Importance** tracking using model insights
- 🧪 **Data Preprocessing** and scaling with saved `.pkl` models
- 💻 **Streamlit Web App** for real-time risk assessment
- 📷 Visual output from UI (`Streamlit_UI.png`) included

📈 Dataset Info
Contains clinical and lifestyle features of patients:

Physical parameters: Waist, Hip, BMI, etc.

Cycle attributes: Duration, Regularity, etc.

Symptoms: Acne, Hair growth, Weight gain

Target: PCOS diagnosed (1) or not (0)

✅ Future Scope
Deployment on HuggingFace or Streamlit Cloud

Use of Explainable AI (XAI) for model transparency

API integration for healthcare applications

## 📂 Repository Structure
📁 PCOSmart/
│
├── PCOS_Project1.ipynb # Jupyter notebook: EDA, preprocessing, model building
├── pcos_appn.py # Streamlit app for PCOS risk prediction
├── SVC_model.pkl # Trained SVM model (used in Streamlit)
├── scaler.pkl # Scaler used for preprocessing inputs
├── map_pcos.xlsx # Encoded/processed dataset (mapped)
├── Streamlit_UI.png # Screenshot of the live Streamlit UI
├── README.md # This documentation file

## 🚀 How to Run Locally

1. **Clone the repo**

git clone https://github.com/Suhani0201/PCOSmart.git

cd PCOSmart

#Install dependencies

pip install -r requirements.txt

#Launch the app

streamlit run pcos_appn.py

