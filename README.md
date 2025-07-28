

## Abstract 
<p> 
Heart disease is one of the most common and life-threatening conditions worldwide. Unfortunately, its treatment can be costly and inaccessible to many. Early prediction can significantly improve treatment outcomes and reduce costs. This project presents a Heart Disease Prediction System leveraging Machine Learning and Data Mining techniques to predict the likelihood of heart disease based on patient data.

Healthcare systems generate vast amounts of data (e.g., text, images), which often go underutilized. This system addresses that by mining historical medical data to make intelligent decisions. It predicts the probability of heart disease using input parameters such as age, sex, cholesterol level, blood pressure, and more. The system uses performance metrics like accuracy, precision, and recall, calculated from a confusion matrix, to evaluate its predictive capabilities.

</p>

## Introduction
<p>
Healthcare organizations collect extensive datasets containing hidden patterns useful for decision-making. This project implements a Heart Disease Prediction System (HDPS) using Naive Bayes, Decision Tree, and Neural Network models to predict the risk of heart disease.

The system uses 13 key medical parameters (e.g., age, cholesterol, obesity) for prediction. We employed a Multilayer Perceptron Neural Network with Backpropagation for training. The results indicate the system effectively predicts heart disease risk levels, offering a valuable tool in medical diagnostics.
</p>

### Aim
<p> 
  To predict heart disease according to input parameter values provided by user and dataset
stored in database.
</p>

### Objective
<p>
  The main objective of this project is to develop a heart disease prediction system. The system
can discover and extract hidden knowledge associated with diseases from a historical heart data
set Heart disease prediction system aims to exploit data mining techniques on medical data set
to assist in the prediction of the heart diseases.
</p>

### Project Scope
<p>
The project has wide applicability across various healthcare organizations. It is designed to be generic, flexible, and accessible to any user or institution. The system provides:

- Patient-friendly interfaces

- Doctor recommendations based on location

- Statistical and visual summaries for deeper insight
</p>

## System Analysis
### Modules:
- **Patient Login:-** *Patient Login to the system using his ID and Password.*
- **Patient Registration:_** *If Patient is a new user he will enter his personal details and he
will user Id and password through which he can login to the system.*
- **My Details:-** *Patient can view his personal details.*
- **Disease Prediction:-** *- Patient will specify the input parameter values. System will take
input values and predict the disease based on the input data values specified by the
patient and system will also suggest doctors based on the locality*
- **Search Doctor:-** *Patient can search for doctor by specifying name, address or type.*
- **Feedback:-** *Patient will give feedback this will be reported to the admin*
- **Doctor Login:-** *Doctor will access the system using his User ID and Password.*
- **Patient Details:-** *Doctor can view patient’s personal details.*
- **Notification:-** *Admin and doctor will get notification how many people had accessed
the system and what all are the diseases predicted by the system.*
- **Admin Login:-** *Admin can login to the system using his ID and Password.*
- **Add Doctor:-** *Admin can add new doctor details into the database.*
- **Add Dataset:-** *Admin can add dataset file in database.*
- **View Doctor:-** *Admin can view various Doctors along with their personal details.*
- **View Disease:-** *Admin can view various diseases details stored in database.*
- **View Patient:-** *Admin can view various patient details that had accessed the system.*
- **View Feedback:-** *Admin can view feedback provided by various users.*
  
### Technology Used:
- #### Languages:
  - ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  - ![JAVASCRIPT](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
  - ![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
- #### FrameWork:
  - ![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
  - ![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
- #### Machine-Learning Algorithms:
  - <a href="https://en.wikipedia.org/wiki/Gradient_boosting">**GRADIENT BOOSTING ALGORITHM**</a>
  - <a href="https://en.wikipedia.org/wiki/Logistic_regression">**LOGISTIC REGRESSION**</a>
- #### ML/DL:
  - ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  - ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  - ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
- Database:
  - The system is integrated with MySQL for robust, production-level database operations
- #### Data-Set for training:
  - <a href="https://github.com/Kumar-laxmi/Heart-Disease-Prediction-System/blob/main/Machine_Learning/heart.csv">Click here for DATA-SET</a>
- #### IDE:
  - ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
  - ![pyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
- #### OS used for testing:
  - ![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
  - ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
  - ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Run Locally

1. Clone the project

```bash
  git clone https://github.com/Aadarshk1/Heart-Disease-Prediction-System
```

2. Go to the project directory

```bash
  cd Heart-Disease-Prediction-System
```

3. Start the server

```bash
  python manage.py runserver
```

## Model Training(Machine Learning)

```javascript
def prdict_heart_disease(list_data):
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)

    X = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    nn_model = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1, random_state=0)
    nn_model.fit(X_train, y_train)
    pred = nn_model.predict([list_data])
    print("Neural Network Accuracy: {:.2f}%".format(nn_model.score(X_test, y_test) * 100))
    print("Prdicted Value is : ", format(pred))
    dataframe = str(df.head())
    return (nn_model.score(X_test, y_test) * 100),(pred)
```
🤝Contribution Guidelines
<p>
We welcome contributions to improve the Heart Disease Prediction System! If you're interested in fixing bugs, adding new features, or improving     documentation, follow the steps below:
</p>
🛠️ How to Contribute
1. Fork the Repository

	Click the Fork button at the top right of the repository page to create your own copy.

2. Clone Your Fork Locally

```bash
git clone https://github.com/Aadarshk1/Heart-Disease-Prediction-System.git
cd Heart-Disease-Prediction-System
```

3. Create a Branch

Create a new branch for your feature or fix:

```bash
git checkout -b feature/your-feature-name
```

4. Make Your Changes

	Add new features or fix bugs

	Write clean, readable, and documented code

	Test your changes thoroughly

5. Commit Your Changes

```bash
git add .
git commit -m "Add: Brief description of your change"
```

6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

7. Open a Pull Request

Go to your forked repository on GitHub and click on New Pull Request. Describe your changes clearly.