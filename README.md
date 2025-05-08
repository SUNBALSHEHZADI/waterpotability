

## 🚀 **Project Overview**

The goal of this project is to build a model that can predict water potability based on chemical features. The model is trained using a dataset containing various features like pH, hardness, sulfate levels, and other water quality indicators. The trained model is then deployed via a **Streamlit** app where users can input values and receive predictions on the potability of water.

---

## 🧑‍💻 **Technologies Used**

* **Python**: The main programming language used for data processing, modeling, and Streamlit app development.
* **Random Forest**: The machine learning algorithm used for prediction.
* **Pandas**: For data manipulation and analysis.
* **Streamlit**: For creating the interactive web application.
* **Matplotlib** and **Seaborn**: For data visualization.
* **Joblib**: For saving and loading the trained model.

---

## 📥 **Installation Instructions**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SUNBALSHEHZADI/water-potability-prediction.git
   cd water-potability-prediction
   ```

2. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes all necessary libraries for the project. If it’s not available, you can manually install them using:

   ```bash
   pip install pandas numpy scikit-learn streamlit seaborn matplotlib joblib
   ```

---

## 🔑 **How to Use**

1. **Train the Model** (if not already trained):

   * The dataset should be loaded, and the model trained using Random Forest.
   * Save the trained model using `joblib`.

   ```python
   import joblib
   from sklearn.ensemble import RandomForestClassifier

   # Load dataset and preprocess
   # Train model
   model = RandomForestClassifier()
   model.fit(X_train, y_train)

   # Save model
   joblib.dump(model, 'water_potability_model.pkl')
   ```

2. **Run the Streamlit App**:

   * Ensure the saved model file `water_potability_model.pkl` is present in the same directory.
   * Start the Streamlit app with the following command:

   ```bash
   streamlit run app.py
   ```

3. **Input Features**:

   * Once the app is running, the user can input values for the following features:

     * pH
     * Hardness
     * Solids
     * Chloramines
     * Sulfate
     * Conductivity
     * Organic Carbon
     * Trihalomethanes
     * Turbidity

4. **Output**:

   * The app will display whether the water is **Potable** or **Not Potable** based on the inputted features.

---

## 📊 **Project Flow**

1. **Data Collection**: The dataset used contains various chemical features of water like pH, sulfate, and others.
2. **Data Preprocessing**: Missing values were handled, and the dataset was split into training and testing sets.
3. **Model Training**: A Random Forest model was trained on the dataset to classify water as either potable or not.
4. **Model Deployment**: The trained model was deployed in a **Streamlit** app where users can input chemical features and receive predictions.

---

## 📜 **Dataset Information**

The dataset used in this project contains information about water quality parameters, which are essential in determining if the water is potable or not. You can download the dataset from [Kaggle's Water Potability Dataset](https://www.kaggle.com/datasets/devanshibavaria/water-potability-dataset-with-10-parameteres).

---

## 📋 **File Structure**

* `app.py`: Streamlit application for the user interface.
* `water_potability_model.pkl`: Saved Random Forest model.
* `requirements.txt`: List of required libraries.
* `README.md`: This file.

---

## ✨ **Contributing**

Feel free to fork the repository, create a pull request, or suggest any improvements. Contributions are always welcome!

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔑 **Acknowledgments**

* Special thanks to the Kaggle community for providing the dataset.
* Thanks to Streamlit for enabling easy web application development.

---

### **Enjoy using the Water Potability Prediction app! 💧**

---

This README should give a comprehensive overview of the project and guide users through setup, usage, and contributions. Let me know if you need any other modifications or additional sections!
