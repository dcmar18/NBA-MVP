# NBA-MVP
Using Machine  Learning to Predict NBA MVP

# Project Goal

## Use machine learning to predict NBA MVP. <br>
Which model worked best?

## Analyze model accuracy.<br>
How accurate were the models?<br>
How do we improve upon them?

## Statistical analysis.<br>
Which statistics are the strongest indicators?

# Project Scope

Dataset used is NBA statistical data from 1979-2017
(1979-1980 season is introduction of 3-point shot)

Data collected from Kaggle <br>
CSV file scraped from basketball-reference.com


Machine learning models applied: <br>
- Neural Network 
- Logistic Regression

# Data Exploration

Created heatmap to select which columns to use as features, based on correlation<br>
![Heatmap](./images/heat_map.png)

Used RandomForestClassifier to discover most impactful features
![Random Forest](./images/random_forest.png)<br>

## Aimed to improve prediction accuracy by reducing the dataset

Filtered the top 10 MVP candidates for each individual season.
As opposed to the total pool of 450-500 players
![Reuced Data](./images/reduce_data.png)

# Data Analyis Results

## Logistic Regression with all data
![All Data LR](./images/all_data_lr.png)

## Nueral Network with all data
![All Data NN](./images/all_data_nn.png)

## Logistic Regression with just MVP candidates
![Limited Data LR](./images/limited_data_lr.png)

## Nueral Network with just MVP candidates
![Limited data NN](./images/limited_data_nn.png)

# Conclusion

Which machine learning model was best?<br>
Overall Logistic Regression was best at predicting the MVP.


Are more features better?<br>
Except for Logistic Regression model where we passed in all the player data and all the features, more features did better than when only the top 15 features were used.

Is more data better?<br>
For Logistic Regression the results were about the same. But for Nueral Networks using more data gave the best results.
