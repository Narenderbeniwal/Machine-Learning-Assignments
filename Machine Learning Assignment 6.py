#!/usr/bin/env python
# coding: utf-8

# 1. In the sense of machine learning, what is a model? What is the best way to train a model?
# 2. In the sense of machine learning, explain the "No Free Lunch" theorem.
# 3. Describe the K-fold cross-validation mechanism in detail.
# 
# 4. Describe the bootstrap sampling method. What is the aim of it?
# 
# 5. What is the significance of calculating the Kappa value for a classification model? Demonstrate how to measure the Kappa value of a classification model using a sample collection of results.
# 
# 6. Describe the model ensemble method. In machine learning, what part does it play?
# 
# 7. What is a descriptive model's main purpose? Give examples of real-world problems that descriptive models were used to solve.
# 
# 8. Describe how to evaluate a linear regression model.
# 
# 9. Distinguish :
# 
# 1. Descriptive vs. predictive models
# 
# 2. Underfitting vs. overfitting the model
# 
# 3. Bootstrapping vs. cross-validation
# 
# 10. Make quick notes on:
# 
#             1. LOOCV.
# 
#             2. F-measurement
# 
#             3. The width of the silhouette
# 
#              4. Receiver operating characteristic curve
# 

# ## 1. In the sense of machine learning, what is a model? What is the best way to train a model?
# 
# Sol:
# In sence of the machine learning :- A machine learning model is a file that has been trained to recognize certain types of patterns. You train a model over a set of data, providing it an algorithm that it can use to reason over and learn from those data.
# 
# 3 steps to training a machine learning model
# 
# Step 1: Begin with existing data. Machine learning requires us to have existing data—not the data our application will use when we run it, but data to learn from.
# 
# Step 2: Analyze data to identify patterns.
# 
# Step 3: Make predictions.
# 

# ## 2. In the sense of machine learning, explain the "No Free Lunch" theorem.
# Sol:
# 
#     The No Free Lunch Theorem is often thrown around in the field of optimization and machine learning, often with little understanding of what it means or implies. The theorem states that all optimization algorithms perform equally well when their performance is averaged across all possible problems.
# ![No+Free+Lunch+Theorem+It+is+the+assumptions+about+the+learning+algorithm+that+are+important..jpg](attachment:No+Free+Lunch+Theorem+It+is+the+assumptions+about+the+learning+algorithm+that+are+important..jpg)

# ## 3. Describe the K-fold cross-validation mechanism in detail.
# Sol:
#     
#     Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample.
# The procedure has a single parameter called k that refers to the number of groups that a given data sample is to be split into. As such, the procedure is often called k-fold cross-validation. When a specific value for k is chosen, it may be used in place of k in the reference to the model, such as k=10 becoming 10-fold cross-validation.
# 
# The general procedure is as follows:
# 
# 1. Shuffle the dataset randomly.
# 
# 2. Split the dataset into k groups
# 
# 3. For each unique group:
# 
#    Take the group as a hold out or test data set
#    
#    Take the remaining groups as a training data set
#    
#    Fit a model on the training set and evaluate it on the test set
#    
#    Retain the evaluation score and discard the model
# 4. Summarize the skill of the model using the sample of model evaluation scores
# 

# # 4. Describe the bootstrap sampling method. What is the aim of it?
# Sol:
# 
#     Bootstrapping is a statistical procedure that resamples a single dataset to create many simulated samples. This process allows you to calculate standard errors, construct confidence intervals, and perform hypothesis testing for numerous types of sample statistics.

# ## 5. What is the significance of calculating the Kappa value for a classification model? Demonstrate how to measure the Kappa value of a classification model using a sample collection of results.
# 
# Sol: 
# 
# 
# It basically tells you how much better your classifier is performing over the performance of a classifier that simply guesses at random according to the frequency of each class. Cohen's kappa is always less than or equal to 1. Values of 0 or less, indicate that the classifier is useless.21

# ## 6. Describe the model ensemble method. In machine learning, what part does it play?
# 
# Sol: An ensemble is a machine learning model that combines the predictions from two or more models. In machine learning with the help
#     of this method we can get the better accureacy for the ML models.
# 

# ## 7. What is a descriptive model's main purpose? Give examples of real-world problems that descriptive models were used to solve.
# 
# Sol: 
# 
# A descriptive model describes a system or other entity and its relationship to its environment. It is generally used to help specify and/or understand what the system is, what it does, and how it does it.
# 

# ## 8. Describe how to evaluate a linear regression model.
# Sol:
#     
#     There are 3 main metrics for model evaluation in regression:
#         
# 1. R Square/Adjusted R Square.
# 
# 2. Mean Square Error(MSE)/Root Mean Square Error(RMSE)
# 
# 3. Mean Absolute Error(MAE)

# ## 1. Descriptive vs. predictive models
# 
# A descriptive model will exploit the past data that are stored in databases and provide you with the accurate report. In a Predictive model, it identifies patterns found in past and transactional data to find risks and future outcomes.

# ## 2. Bootstrapping vs. cross-validation
# 
# Cross validation splits the available dataset to create multiple datasets, and 
# 
# Bootstrapping method uses the original dataset to create multiple datasets after resampling with replacement. 
# 
# Bootstrapping it is not as strong as Cross validation when it is used for model validation
# 

# ## 1. LOOCV.
# 
# The Leave-One-Out Cross-Validation, or LOOCV, procedure is used to estimate the performance of machine learning algorithms when they are used to make predictions on data not used to train the model.

# ## 2. F-measurement
# 
# In statistical analysis of binary classification, the F-score or F-measure is a measure of a test's accuracy.
# 

# In[ ]:




