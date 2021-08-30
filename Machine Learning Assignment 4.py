#!/usr/bin/env python
# coding: utf-8
1. What are the key tasks involved in getting ready to work with machine learning modeling?
2. What are the different forms of data used in machine learning? Give a specific example for each of them.
3. Distinguish:

           1. Numeric vs. categorical attributes

            2. Feature selection vs. dimensionality reduction

4. Make quick notes on any two of the following:

            1. The histogram

             2. Use a scatter plot

              3.PCA (Personal Computer Aid)

5. Why is it necessary to investigate data? Is there a discrepancy in how qualitative and quantitative data are explored?

6. What are the various histogram shapes? What exactly are ‘bins'?

7. How do we deal with data outliers?

8. What are the various central inclination measures? Why does mean vary too much from median in certain data sets?

9. Describe how a scatter plot can be used to investigate bivariate relationships. Is it possible to find outliers using a scatter plot?

10. Describe how cross-tabs can be used to figure out how two variables are related.

# Q. 1. What are the key tasks involved in getting ready to work with machine learning modeling?
Sol: 1 - Data Collection.
2 - Data Preparation.
3 - Choose a Model.
4 - Train the Model.
5 - Evaluate the Model.
6 - Parameter Tuning.
7 - Make Predictions.Q. 2. What are the different forms of data used in machine learning? Give a specific example for each of them.

Sol: Almost anything can be turned into DATA. Building a deep understanding of the different data types is a crucial prerequisite for doing Exploratory Data Analysis (EDA) and Feature Engineering for Machine Learning models. You also need to convert data types of some variables in order to make appropriate choices for visual encodings in data visualization and storytelling.
Most data can be categorized into 4 basic types from a Machine Learning perspective: numerical data, categorical data, time-series data, and text.

Numerical Data
Numerical data is any data where data points are exact numbers. Statisticians also might call numerical data, quantitative data. This data has meaning as a measurement such as house prices or as a count, such as a number of residential properties in Los Angeles or how many houses sold in the past year.
Categorical Data:
Categorical data represents characteristics, such as a hockey player’s position, team, hometown. Categorical data can take numerical values. For example, maybe we would use 1 for the colour red and 2 for blue. But these numbers don’t have a mathematical meaning. That is, we can’t add them together or take the average.

Time Series Data
Time series data is a sequence of numbers collected at regular intervals over some period of time. It is very important, especially in particular fields like finance. Time series data has a temporal value attached to it, so this would be something like a date or a timestamp that you can look for trends in time.

Text
Text data is basically just words. A lot of the time the first thing that you do with text is you turn it into numbers using some interesting functions like the bag of words formulation.
3. Distinguish:

           1. Numeric vs. categorical attributes

            
            
Sol: A categorical variable is a category or type. For example, hair color is a categorical value or hometown is a categorical variable. Species, treatment type, and gender are all categorical variables.

A numerical variable is a variable where the measurement or number has a numerical meaning. For example, total rainfall measured in inches is a numerical value, heart rate is a numerical value, number of cheeseburgers consumed in an hour is a numerical value.

A categorical variable can be expressed as a number for the purpose of statistics, but these numbers do not have the same meaning as a numerical value . For example, if I am studying the effects of three different medications on an illness, I may name the three different medicines, medicine 1, medicine 2, and medicine 3. However, medicine three is not greater, or stronger, or faster than medicine one. These numbers are not meaningful.

2. Feature selection vs. dimensionality reduction
Sol: In the  Feature selection  we select the fearutres which are corelated with the our output of the model and in  Dimensionality reduction transforms features into a lower dimension. 


While both methods are used for reducing the number of features in a dataset, there is an important difference. Feature selection is simply selecting and excluding given features without changing them. Dimensionality reduction transforms features into a lower dimension.4. Make quick notes on any two of the following:

            1. The histogram

             2. Use a scatter plot

              3.PCA (Personal Computer Aid)
Sol: The Histogarm: A histogram is a chart that shows frequencies for. intervals of values of a metric variable. Such intervals as known as “bins” and they all have the same widths.

2. Use a scatter plot
The scatter diagram graphs pairs of numerical data, with one variable on each axis, to look for a relationship between them. If the variables are correlated, the points will fall along a line or curve5. Why is it necessary to investigate data? Is there a discrepancy in how qualitative and quantitative data are explored?
Sol :
Data analysis is important in business to understand problems facing an organisation, and to explore data in meaningful ways. Data in itself is merely facts and figures. Data analysis organises, interprets, structures and presents the data into useful information that provides context for the data.''


Is there a discrepancy in how qualitative and quantitative data are explored?
Quantitative data can be counted, measured, and expressed using numbers. Qualitative data is descriptive and conceptual. Qualitative data can be categorized based on traits and characteristics.
6. What are the various histogram shapes? What exactly are ‘bins'?

Sol: 
Bell-shaped: A bell-shaped picture, shown below, usually presents a normal distribution.
Bimodal: A bimodal shape, shown below, has two peaks. ...
Skewed left: Some histograms will show a skewed distribution to the left. .
Sol: A histogram is a chart that plots the distribution of a numeric variable's values as a series of bars. Each bar typically covers a range of numeric values called a bin or class; a bar's height indicates the frequency of data points with a value within the corresponding bin.7. How do we deal with data outliers?
Sol 1. Set up a filter in your testing tool.
2. Remove or change outliers during post-test analysis
3. Change the value of outliers
4. Consider the underlying distribution
5. Consider the value of mild outliers8. What are the various central inclination measures? Why does mean vary too much from median in certain data sets?
Sol: A measure of central tendency is an important aspect of quantitative data. It is an estimate of a “typical” value. Three of the many ways to measure central tendency are the mean, median and mode. There are other measures, such as a trimmed mean, that we do not discuss here.


 The mean is not a robust tool since it is largely influenced by outliers. ... A mean is computed by adding up all the values and dividing that score by the number of values. The Median is the number found at the exact middle of the set of values.9. Describe how a scatter plot can be used to investigate bivariate relationships. Is it possible to find outliers using a scatter plot?

Sol : Yes  Is it possible to find outliers using a scatter plot.10. Describe how cross-tabs can be used to figure out how two variables are related.
 If the two elements are independent, the tabulation is termed insignificant, and the study would be termed as a null hypothesis.

helps identify if the variables of the study are independent or related to each other. 
# In[ ]:




