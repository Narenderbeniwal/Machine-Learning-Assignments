#!/usr/bin/env python
# coding: utf-8
1. What exactly is a feature? Give an example to illustrate your point.
2. What are the various circumstances in which feature construction is required?
3. Describe how nominal variables are encoded.

4. Describe how numeric features are converted to categorical features.

5. Describe the feature selection wrapper approach. State the advantages and disadvantages of this approach?

6. When is a feature considered irrelevant? What can be said to quantify it?

7. When is a function considered redundant? What criteria are used to identify features that could be redundant?

8. What are the various distance measurements used to determine feature similarity?

9. State difference between Euclidean and Manhattan distances?

10. Distinguish between feature transformation and feature selection.

11. Make brief notes on any two of the following:

          1.SVD (Standard Variable Diameter Diameter)

          2. Collection of features using a hybrid approach

          3. The width of the silhouette

          4. Receiver operating characteristic curveQ. 1. What exactly is a feature? Give an example to illustrate your point.
Sol:


In machine learning, features are individual independent variables that act like a input in your system. Actually, while making the predictions, models use such features to make the predictions. And using the feature engineering process, new features can also be obtained from old features in machine learning.
To understand in more simple way, lets take an example, where you can consider one column of your data set to be one feature which is also know as “variables or attributes” and the more number of features are known as dimensions. And depending on what you are trying to analyze the features you include in your dataset can vary widely.Q. 2. What are the various circumstances in which feature construction is required?

Sol: Accuracy improvements.
Overfitting risk reduction.
Speed up in training.
Improved Data Visualization.
Increase in explainability of our model.

Q. 3. Describe how nominal variables are encoded.

Sol: Nominal — groups without order — discrete

. A column with nominal data has values that cannot be ordered in any meaningful way. Nominal data is most often one-hot (aka dummy) encoded, but there are many options that might perform better for machine learning.
Q. 4. Describe how numeric features are converted to categorical features.
 Sol: 
astype() method is used to cast a pandas object to a specified dtype. astype() function also provides the capability to convert any suitable existing column to categorical type.
# In[2]:


get_ipython().set_next_input('Q. 5.Describe the feature selection wrapper approach. State the advantages and disadvantages of this approach');get_ipython().run_line_magic('pinfo', 'approach')


# Q. 5.Describe the feature selection wrapper approach. State the advantages and disadvantages of this approach?
# 
# Sol: In wrapper methods, the feature selection process is based on a specific machine learning algorithm that we are trying to fit on a given dataset.
# 
# It follows a greedy search approach by evaluating all the possible combinations of features against the evaluation criterion. The evaluation criterion is simply the performance measure which depends on the type of problem, for e.g. For regression evaluation criterion can be p-values, R-squared, Adjusted R-squared, similarly for classification the evaluation criterion can be accuracy, precision, recall, f1-score, etc. Finally, it selects the combination of features that gives the optimal results for the specified machine learning algorithm.
# 
# ![Advantages-and-disadvantages-of-wrapper-methods%20%281%29.png](attachment:Advantages-and-disadvantages-of-wrapper-methods%20%281%29.png)
Q. 6. When is a feature considered irrelevant? What can be said to quantify it?
 Sol: You can get the feature importance of each feature of your dataset by using the feature importance property of the model. Feature importance gives you a score for each feature of your data, the higher the score more important or relevant is the feature towards your output variable.Q. 7 When is a function considered redundant? What criteria are used to identify features that could be redundant?

Sol:For example, if two features {X1, X2} are highly cor/'related, then the two features become redundant features since they have same information in terms of correlation measure. In other words, the correlation measure provides statistical association between any given a pair of features.Q. 8. What are the various distance measurements used to determine feature similarity?

Sol: 
Three of the most commonly used distance measures in machine learning are as follows: Hamming Distance. Euclidean Distance. Manhattan Distance.Q. 9. State difference between Euclidean and Manhattan distances?

Sol: Euclidean distance is the shortest path between source and destination which is a straight line.

Manhattan distance is sum of all the real distances between source(s) and destination(d) and each distance are always the straight linesQ. 10. Distinguish between feature transformation and feature selection.

Sol: feature transformation: transformation of data to improve the accuracy of the algorithm; feature selection: removing unnecessary features.