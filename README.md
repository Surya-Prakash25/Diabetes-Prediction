<h2>Diabetes Prediction</h2>
  This project aims to predict whether an individual has diabetes based on certain diagnostic measurements. The prediction is made using machine learning techniques.

<h2>Table of Contents</h2>
<ul>
<li>Project Overview</li>
<li>Dataset </li>
<li>Technologies Used</li>
<li>  Installation</li>
<li>Usage</li>
<li>Results</li>
<li>Contributing</li>
</ul>
<h2>Project Overview</h2>
Diabetes is a chronic condition affecting millions of people worldwide. Early detection is key to effective management. In this project, we use machine learning models to predict whether a patient is diabetic based on medical diagnostic data.

The dataset used for this project contains various health metrics, including glucose levels, blood pressure, and insulin levels. We use these features to build a predictive model that helps identify individuals who are likely to develop diabetes.

<h2>Dataset<h2>
The dataset is sourced from the Pima Indians Diabetes Database. It contains 768 instances with the following features:

Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration
Blood Pressure: Diastolic blood pressure (mm Hg)
Skin Thickness: Triceps skin fold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml)
BMI: Body mass index (weight in kg/(height in m)^2)
Diabetes Pedigree Function: A function which scores likelihood of diabetes based on family history
Age: Age (years)
Outcome: Whether the patient is diabetic (1) or not (0)

Technologies Used
  Python: Main programming language
  Jupyter Notebook: For code development
  Libraries:
    pandas for data manipulation
    numpy for numerical computations
    matplotlib and seaborn for data visualization
    scikit-learn for machine learning models

Installation
Clone this repository:
git clone https://github.com/Surya-Prakash25/Diabetes-Prediction.git
Navigate to the project directory:
cd Diabetes-Prediction
Install the required dependencies:
pip install -r requirements.txt


Usage
Open the Jupyter notebook:
jupyter notebook notebooks/diabetes_prediction.ipynb

Run the cells in the notebook to:

Load the dataset
Perform exploratory data analysis (EDA)
Preprocess the data
Train machine learning models
Evaluate model performance

Results
The project builds and evaluates several machine learning models such as Logistic Regression, Decision Trees, Random Forest, and XGBoost to predict diabetes. Model accuracy, precision, recall, and F1 score metrics are reported, and feature importance is visualized.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request or raise issues regarding bugs or feature requests.
