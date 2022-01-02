#!/usr/bin/env python
# coding: utf-8
1. What is the definition of a target function? In the sense of a real-life example, express the target
function. How is a target function fitness assessed?
2. What are predictive models, and how do they work? What are descriptive types, and how do you
use them? Examples of both types of models should be provided. Distinguish between these two
forms of models.
3. Describe the method of assessing a classification model efficiency in detail. Describe the various
measurement parameters.
4.
i. In the sense of machine learning models, what is underfitting? What is the most common
reason for underfitting?
ii. What does it mean to overfit? When is it going to happen?
iii. In the sense of model fitting, explain the bias-variance trade-off.
5. Is it possible to boost the efficiency of a learning model? If so, please clarify how.
6. How would you rate an unsupervised learning model success? What are the most common
success indicators for an unsupervised learning model?
7. Is it possible to use a classification model for numerical data or a regression model for categorical
data with a classification model? Explain your answer.
8. Describe the predictive modeling method for numerical values. What distinguishes it from
categorical predictive modeling?
9. The following data were collected when using a classification model to predict the malignancy of a
group of patients&#39; tumors:
i. Accurate estimates – 15 cancerous, 75 benign
ii. Wrong predictions – 3 cancerous, 7 benign
Determine the model error rate, Kappa value, sensitivity, precision, and F-measure.
10. Make quick notes on:
    1. The process of holding out
    2. Cross-validation by tenfold
    3. Adjusting the parameters
11. Define the following terms:
    1. Purity vs. Silhouette width
    2. Boosting vs. Bagging
    3. The eager learner vs. the lazy learner
# ## Q.1. What is the definition of a target function? In the sense of a real-life example, express the target function. How is a target function fitness assessed?
# 
# Sol: 
# A target function, in machine learning, is a method for solving a problem that an AI algorithm parses its training data to find. Once an algorithm finds its target function, that function can be used to predict results (predictive analysis).
# 
# Analyzing the massive amounts of data related to its given problem, an AI derives understanding of previously unspecified rules by detecting consistencies in the data. The observations of inherent rules about how the studied subject operates inform the AI on how to process future data that does not include an output by applying this previously unknown function.
# 
# 

# ## Q. 2. What are predictive models, and how do they work? What are descriptive types, and how do you use them? Examples of both types of models should be provided. Distinguish between these two forms of models.
# 
# Sol: 
# In short, predictive modeling is a statistical technique using machine learning and data mining to predict and forecast likely future outcomes with the aid of historical and existing data. It works by analyzing current and historical data and projecting what it learns on a model generated to forecast likely outcomes.
# 
# 
# 
# The descriptive analysis uses mainly unsupervised learning approaches for summarizing, classifying, extracting rules to answer what happens was happened in the past. 
# 
# 
# Descriptive analysis is used to understand the past and predictive analysis is used to predict the future. Both of these concepts are important in machine learning because a clear understanding of the problem and its implications is the best way to make the right decisions.
# 
# ![descriptive-predictive.jpeg](attachment:descriptive-predictive.jpeg)

# ## Q. 3. Describe the method of assessing a classification model efficiency in detail. Describe the various measurement parameters.
# 
# Sol:
#     
# The most commonly used Performance metrics for classification problem are as follows,
# 1. Accuracy:
#     Accuracy is the simple ratio between the number of correctly classified points to the total number of points.
# 
# 
# 
# 
# 2. Confusion Matrix
# 3. Precision, Recall, and F1 score
# 4. ROC AUC
# 5. Log-loss
# 

# ## Q. 4 (i): In the sense of machine learning models, what is underfitting? What is the most common reason for underfitting?
# Sol: 
#      Underfitting refers to a model that can neither model the training data nor generalize to new data. An underfit machine learning model is not a suitable model and will be obvious as it will have poor performance on the training data.
#      most common reason for underfitting are less data availabe, noise in the data, wrong model etc
# ## ii. What does it mean to overfit? When is it going to happen?
# Sol: 
# 
# Overfitting happens when a model learns the detail and noise in the training data to the extent that it negatively impacts the performance of the model on new data. This means that the noise or random fluctuations in the training data is picked up and learned as concepts by the model.
# 
# Overfitting is an error that occurs in data modeling as a result of a particular function aligning too closely to a minimal set of data points.
# 
# ## iii. In the sense of model fitting, explain the bias-variance trade-off.
# Sol :
# 
# Bias is the simplifying assumptions made by the model to make the target function easier to approximate. Variance is the amount that the estimate of the target function will change given different training data. Trade-off is tension between the error introduced by the bias and the variance.
# 

# ## 5. Is it possible to boost the efficiency of a learning model? If so, please clarify how.
# 
# Methods to Boost the Accuracy of a Model
# 
# Add more data. Having more data is always a good idea. 
# 
# Treat missing and Outlier values. 
# 
# Feature Engineering. 
# 
# Feature Selection. 
# 
# Multiple algorithms. 
# 
# Algorithm Tuning.
# 
# Ensemble methods.
# 

# ## Q. 6. How would you rate an unsupervised learning model success? What are the most common success indicators for an unsupervised learning model?
# Sol :
# 
# In some sense I think this question is unanswerable. I say this because how well a particular unsupervised method performs will largely depend on why one is doing unsupervised learning in the first place, i.e., does the method perform well in the context of your end goal? Obviously this isn't completely true, people work on these problems and publish results which include some sort of evaluation. I'll outline a few of the approaches I'm familiar with below.
# 
# How well a particular unsupervised method performs will largely depend on why one is doing unsupervised learning in the first place" pretty much sums it up. Don't go looking for a some magic number that you can somehow use to justify a given result without actually interpreting the result.
# 
# - Clustering Performance Evaluation Metrics
# 

# ## Q. 7. Is it possible to use a classification model for numerical data or a regression model for categorical data with a classification model? Explain your answer.

# ## 8. Describe the predictive modeling method for numerical values. What distinguishes it from categorical predictive modeling?
# 
# Sol : predictive modeling is a statistical technique using machine learning and data mining to predict and forecast likely future outcomes with the aid of historical and existing data. It works by analyzing current and historical data and projecting what it learns on a model generated to forecast likely outcomes
## 9. The following data were collected when using a classification model to predict the malignancy of a
group of patients tumors:
i. Accurate estimates – 15 cancerous, 75 benign
ii. Wrong predictions – 3 cancerous, 7 benign
Determine the model error rate, Kappa value, sensitivity, 
, and F-measure.

Sol: 
Accuracy =  90/10 = 90percent 
error rate = 1-.9 = 0.1 

# ## Q.11 Boosting vs. Bagging
# 
# Sol :Bagging is a way to decrease the variance in the prediction by generating additional data for training from dataset using combinations with repetitions to produce multi-sets of the original data. Boosting is an iterative technique which adjusts the weight of an observation based on the last classification.

# In[ ]:




