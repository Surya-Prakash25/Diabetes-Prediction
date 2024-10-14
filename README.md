<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diabetes Prediction</title>
</head>
<body>

<h1>Diabetes Prediction</h1>

<p>This project aims to predict whether an individual has diabetes based on certain diagnostic measurements. The prediction is made using machine learning techniques.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#contributing">Contributing</a></li>
   
</ul>

<h2 id="project-overview">Project Overview</h2>
<p>Diabetes is a chronic condition affecting millions of people worldwide. Early detection is key to effective management. In this project, we use machine learning models to predict whether a patient is diabetic based on medical diagnostic data.</p>
<p>The dataset used for this project contains various health metrics, including glucose levels, blood pressure, and insulin levels. We use these features to build a predictive model that helps identify individuals who are likely to develop diabetes.</p>

<h2 id="dataset">Dataset</h2>
<p>The dataset is sourced from the <a href="https://www.kaggle.com/uciml/pima-indians-diabetes-database">Pima Indians Diabetes Database</a>. It contains 768 instances with the following features:</p>
<ul>
    <li><strong>Pregnancies</strong>: Number of times pregnant</li>
    <li><strong>Glucose</strong>: Plasma glucose concentration</li>
    <li><strong>Blood Pressure</strong>: Diastolic blood pressure (mm Hg)</li>
    <li><strong>Skin Thickness</strong>: Triceps skin fold thickness (mm)</li>
    <li><strong>Insulin</strong>: 2-Hour serum insulin (mu U/ml)</li>
    <li><strong>BMI</strong>: Body mass index (weight in kg/(height in m)^2)</li>
    <li><strong>Diabetes Pedigree Function</strong>: A function which scores likelihood of diabetes based on family history</li>
    <li><strong>Age</strong>: Age (years)</li>
    <li><strong>Outcome</strong>: Whether the patient is diabetic (1) or not (0)</li>
</ul>

<h2 id="technologies-used">Technologies Used</h2>
<ul>
    <li><strong>Python</strong>: Main programming language</li>
    <li><strong>Jupyter Notebook</strong>: For code development</li>
    <li><strong>Libraries</strong>:
        <ul>
            <li><code>pandas</code> for data manipulation</li>
            <li><code>numpy</code> for numerical computations</li>
            <li><code>matplotlib</code> and <code>seaborn</code> for data visualization</li>
            <li><code>scikit-learn</code> for machine learning models</li>
        </ul>
    </li>
</ul>


<h2 id="installation">Installation</h2>
<ol>
    <li>Clone this repository:
        <pre><code>git clone https://github.com/Surya-Prakash25/Diabetes-Prediction.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd Diabetes-Prediction</code></pre>
    </li>
    <li>Install the required dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h2 id="usage">Usage</h2>
<ol>
    <li>Open the Jupyter notebook:
        <pre><code>jupyter notebook notebooks/diabetes_prediction.ipynb</code></pre>
    </li>
    <li>Run the cells in the notebook to:
        <ul>
            <li>Load the dataset</li>
            <li>Perform exploratory data analysis (EDA)</li>
            <li>Preprocess the data</li>
            <li>Train machine learning models</li>
            <li>Evaluate model performance</li>
        </ul>
    </li>
</ol>

<h2 id="results">Results</h2>
<p>The project builds and evaluates several machine learning models such as Logistic Regression, Decision Trees, Random Forest, and XGBoost to predict diabetes. Model accuracy, precision, recall, and F1 score metrics are reported, and feature importance is visualized.</p>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please feel free to submit a Pull Request or raise issues regarding bugs or feature requests.</p>


</body>
</html>

