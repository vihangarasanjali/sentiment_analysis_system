# sentiment_analysis_system

## Overview

This project predicts whether a tweet added by a user is positive or negative using Machine Learning.

The target variable is:

* `1` → Positive tweet
* `0` → Negative tweet

---

## Project Structure

```text
career-match-model/
├── main.py                  # FastAPI prediction service
├── requirements.txt
├── artifacts/               # Dataset (Job_Data.csv)
├── notebooks/
│   ├── model_building.ipynb
└── static/
    └── model/
        └── corpora/
            ├── stopwords/
        ├── model.pickle
        └── vocabulary.txt
```

## Feature Column

* `label`


## Target Variable

* `tweet`

---

## Data Preprocessing

1. Loaded and explored the dataset.
2. Checked for duplicate values and missing values.
3. Removed unnecessary ID column.
4. Built vocabulary using nltk library  
5. Separated features (`X`) and target (`y`).
6. Split into training and testing sets (80/20, stratified to preserve the class distribution).
7. Vectorized the training and testing data.
8. Handled imbalnce of the dataset


## Models Tested

* Logistic Regression
* Multinomial Naive Bayes
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)


## Evaluation Metrics

Accuracy, Precision, Recall and F1-Score. Because the dataset is imbalanced, F1-score and Recall were given particular attention.

## Model Results for Testing data

| Model                   |  Accuracy | Precision |    Recall |  F1-Score |
| ----------------------- | --------: | --------: | --------: | --------: |
| Logistic Regression     |     0.883 |     0.741 |     0.851 | **0.792** |
| Multinomial Naive Bayes |     0.871 |     0.691 |     0.926 |     0.791 |
| Decision Tree           |     0.84  |     0.704 |     0.679 |     0.691 |
| Random Forest           |     0.879 |     0.784 |     0.748 |     0.766 |
| SVM                     |     0.886 |     0.769 |     0.813 |     0.79  |

### Selected Model

**Linear Regression** (highest test F1-score of 0.792).

## Model Saving

The calibrated SVM was saved with `pickle`:

* `static/model/model.pickle`: the trained, calibrated model (includes the scaler).
* `static/model/feature_columns.pickle`: the feature names and order used during training.

Pickles should be loaded with the same scikit-learn version used for training (`scikit-learn==1.9.0`).

