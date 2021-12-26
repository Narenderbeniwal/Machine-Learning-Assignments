#!/usr/bin/env python
# coding: utf-8
1. What are the key tasks that machine learning entails? What does data pre-processing imply?
2. Describe quantitative and qualitative data in depth. Make a distinction between the two.
3. Create a basic data collection that includes some sample records. Have at least one attribute from each of the machine learning data types.

4. What are the various causes of machine learning data issues? What are the ramifications?

5. Demonstrate various approaches to categorical data exploration with appropriate examples.

6. How would the learning activity be affected if certain variables have missing values? Having said that, what can be done about it?

7. Describe the various methods for dealing with missing data values in depth.

8. What are the various data pre-processing techniques? Explain dimensionality reduction and function selection in a few words.

9. What is the IQR? What criteria are used to assess it?



10. Make brief notes on any two of the following:

              1. Data collected at regular intervals

               2. The gap between the quartiles

               3. Use a cross-tab

1. Make a comparison between:

1. Data with nominal and ordinal values

2. Histogram and box plot

3. The average and median

# ##  Q. 1 What are the key tasks that machine learning entails? What does data pre-processing imply?
# Sol: 
# Following are the key machine learning task:
# 
# 1. Data gathering.
# 2. Data preprocessing.
# 3. Exploratory data analysis (EDA)
# 4. Feature engineering.
# 5. Training machine learning models of the following kinds: Regression. Classification. Clustering.
# 6. Multivariate querying.
# 7. Density estimation.
# 8. Dimensionality reduction.
# 
# 
# In machine learning data preprocessing, we divide our dataset into a training set and test set. ... Training Set: A subset of dataset to train the machine learning model, and we already know the output. Test set: A subset of dataset to test the machine learning model, and by using the test set, model predicts the output.

# ## Q. 2. Describe quantitative and qualitative data in depth. Make a distinction between the two.
# Sol: 
#     
#     Quantitative research deals with numbers and statistics, while qualitative research deals with words and meanings. Quantitative methods allow you to systematically measure variables and test hypotheses. Qualitative methods allow you to explore concepts and experiences in more detail.
#     
#     
#     
# 

# ## Q. 3. Create a basic data collection that includes some sample records. Have at least one attribute from each of the machine learning data types.

# ## Q. 4. What are the various causes of machine learning data issues? What are the ramifications?
# 
# 
# 1) Understanding Which Processes Need Automation
# 
# It's becoming increasingly difficult to separate fact from fiction in terms of Machine Learning today. Before you decide on which AI platform to use, you need to evaluate which problems you’re seeking to solve. The easiest processes to automate are the ones that are done manually every day with no variable output. Complicated processes require further inspection before automation. While Machine Learning can definitely help automate some processes, not all automation problems need Machine Learning.
# 
# 2) Lack of Quality Data
# 
# The number one problem facing Machine Learning is the lack of good data. While enhancing algorithms often consumes most of the time of developers in AI, data quality is essential for the algorithms to function as intended. Noisy data, dirty data, and incomplete data are the quintessential enemies of ideal Machine Learning. The solution to this conundrum is to take the time to evaluate and scope data with meticulous data governance, data integration, and data exploration until you get clear data. You should do this before you start.
# 
# 4) Implementation
# 
# Organizations often have analytics engines working with them by the time they choose to upgrade to Machine Learning. Integrating newer Machine Learning methodologies into existing methodologies is a complicated task. Maintaining proper interpretation and documentation goes a long way to easing implementation. Partnering with an implementation partner can make the implementation of services like anomaly detection, predictive analysis, and ensemble modeling much easier.
# 
# 5) Lack of Skilled Resources

# 
# ## Q. 5. Demonstrate various approaches to categorical data exploration with appropriate examples.
# Sol: 
# 
# Exploring categorical variables is generally simpler than working with numeric variables because we have fewer options, or at least life is simpler if we only require basic summaries. We’ll work with the year and type variables in storms to illustrate the key ideas.
# 
# 1. Numerical summaries: 
# '
#  When we calculate summaries of categorical variables we are aiming to describe the sample distribution of the variable, just as with numeric variables. The general question we need to address is, ‘what are the relative frequencies of different categories?’ 
# 2. Graphical summaries of categorical variables
# 

# ## Q. 6. How would the learning activity be affected if certain variables have missing values? Having said that, what can be done about it?
# 
# Sol: If there are lots of missing values in the data our ML model can underfit which later on result in the bad or wrong prediction. 
# 
#     Soltions for the missing values:
#     
#         1. If our data is very large and missing values are very Small we can drop thoese missing value.
#         
#         2. We can replace those misssing values with mean. 
# 

# ## Q.7. Describe the various methods for dealing with missing data values in depth.
# Sol . 
# 
# 1. Mean or Median Imputation:
#     
# When data is missing at random, we can use list-wise or pair-wise deletion of the missing observations. However, there can be multiple reasons why this may not be the most feasible option:
# 
# There may not be enough observations with non-missing data to produce a reliable analysis
# In predictive analytics, missing data can prevent the predictions for those observations which have missing data
# External factors may require specific observations to be part of the analysis
# In such cases, we impute values for missing data. A common technique is to use the mean or median of the non-missing observations. This can be useful in cases where the number of missing observations is low. However, for large number of missing values, using mean or median can result in loss of variation in data and it is better to use imputations. Depending upon the nature of the missing data, we use different techniques to impute data that have been described below.
# 
# 2. Multivariate Imputation by Chained Equations (MICE)
# 
# MICE assumes that the missing data are Missing at Random (MAR). It imputes data on a variable-by-variable basis by specifying an imputation model per variable. MICE uses predictive mean matching (PMM) for continuous variables, logistic regressions for binary variables, bayesian polytomous regressions for factor variables, and proportional odds model for ordered variables to impute missing data.
# 
# To set up the data for MICE, it is important to note that the algorithm uses all the variables in the data for predictions. In this case, variables that may not be useful for predictions, like the ID variable, should be removed before implementing this algorithm.
# 
# Copy code snippet
# Copied to ClipboardError: Could not CopyCopied to ClipboardError: Could not CopyCopied to ClipboardError: Could not Copy
# 
# 3. Random Forest
# 
# Random forest is a non-parametric imputation method applicable to various variable types that works well with both data missing at random and not missing at random. Random forest uses multiple decision trees to estimate missing values and outputs OOB (out of bag) imputation error estimates. 
# 

# ## Q. 8. What are the various data pre-processing techniques?
# Sol :
#     Data Cleaning: The data can have many irrelevant and missing parts.
#         
# Data Transformation: This step is taken in order to transform the data in appropriate forms suitable for mining process.
#     
# Data Reduction: Since data mining is a technique that is used to handle huge amount of data.
#     
#    ![Data-Preprocessing.png](attachment:Data-Preprocessing.png)
# 

# ## Q. 9. What is the IQR? What criteria are used to assess it?
# 
# Sol: The interquartile range shows how the data is spread about the median.
# 
#     The interquartile range is calculated in much the same way as the range. All you do to find it is subtract the first quartile from the third quartile:
# ## IQR = Q3 – Q1.

# ## 10. Make brief notes on: Data collected at regular intervals
#     
# Sol: interval data always take numerical values where the distance between two points on the scale is standardised and equal.
# 

# ## Q. 11. Make a comparison between:
# 
# ### 1. Data with nominal and ordinal values:
# 
# Sol :Nominal data is classified without a natural order or rank, whereas ordinal data has a predetermined or natural order
# 
# ### 2 What is the difference between histogram and box plot?
# Image result for Histogram and box plot
# Histograms and box plots are very similar in that they both help to visualize and describe numeric data. Although histograms are better in determining the underlying distribution of the data, box plots allow you to compare multiple data sets better than histograms as they are less detailed and take up less space.
# ### 3. The average and median
# 
# The mean (average) of a data set is found by adding all numbers in the data set and then dividing by the number of values in the set. The median is the middle value when a data set is ordered from least to greatest.
# 

# In[ ]:




