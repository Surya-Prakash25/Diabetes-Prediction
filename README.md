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

<h2>Dataset</h2>
The dataset is sourced from the Pima Indians Diabetes Database. It contains 768 instances with the following features:
<ol>
<li>Pregnancies: Number of times pregnant</li>
<li>Glucose: Plasma glucose concentration</li>
<li>Blood Pressure: Diastolic blood pressure (mm Hg)</li>
<li>Skin Thickness: Triceps skin fold thickness (mm)</li>
<li>Insulin: 2-Hour serum insulin (mu U/ml)</li>
<li>BMI: Body mass index (weight in kg/(height in m)^2)</li>
<li>Diabetes Pedigree Function: A function which scores likelihood of diabetes based on family history</li>
<li>Age: Age (years)</li>
<li>Outcome: Whether the patient is diabetic (1) or not (0)</li>
</ol>

<h2>Technologies Used </h2>
<ul>
 <li> Python: Main programming language</li>
  <li>Jupyter Notebook: For code development</li>
  </ul>
  Libraries:
  <ol>
    <li>pandas for data manipulation</li>
    <li>numpy for numerical computations</li>
    <li>matplotlib and seaborn for data visualization</li>
    <li>scikit-learn for machine learning models</li>
  </ol>

<h2>Installation</h2>
Clone this repository:<br>
 $ git clone https://github.com/Surya-Prakash25/Diabetes-Prediction.git <br>
Navigate to the project directory:<br>
$ cd Diabetes-Prediction <br>
Install the required dependencies:<br>
$ pip install -r requirements.txt <br>


<h2>Usage</h2>
Open the Jupyter notebook:<br>
jupyter notebook notebooks/diabetes_prediction.ipynb

Run the cells in the notebook to:
<ul>
<li>Load the dataset</li>
<li>Perform exploratory data analysis (EDA)</li>
<li>Preprocess the data</li>
<li>Train machine learning models</li>
<li>Evaluate model performance</li>
</ul>

<h2>Results</h2>
The project builds and evaluates several machine learning models such as Logistic Regression, Decision Trees, Random Forest, and XGBoost to predict diabetes. Model accuracy, precision, recall, and F1 score metrics are reported, and feature importance is visualized.

<h2>Contributing</h2>
Contributions are welcome! Please feel free to submit a Pull Request or raise issues regarding bugs or feature requests.
