#!/usr/bin/env python
# coding: utf-8
1. What does one mean by the term "machine learning"?

2.Can you think of 4 distinct types of issues where it shines?



3.What is a labeled training set, and how does it work?



4.What are the two most important tasks that are supervised?



5.Can you think of four examples of unsupervised tasks?



6.State the machine learning model that would be best to make a robot walk through various unfamiliar terrains?



7.Which algorithm will you use to divide your customers into different groups?



8.Will you consider the problem of spam detection to be a supervised or unsupervised learning problem?



9.What is the concept of an online learning system?



10.What is out-of-core learning, and how does it differ from core learning?



11.What kind of learning algorithm makes predictions using a similarity measure?



12.What's the difference between a model parameter and a hyperparameter in a learning algorithm?



13.What are the criteria that model-based learning algorithms look for? What is the most popular method they use to achieve success? What method do they use to make predictions?



14.Can you name four of the most important Machine Learning challenges?



15.What happens if the model performs well on the training data but fails to generalize the results to new situations? Can you think of three different options?



16.What exactly is a test set, and why would you need one?



17.What is a validation set's purpose?



18.What precisely is the train-dev kit, when will you need it, how do you put it to use?



19.What could go wrong if you use the test set to tune hyperparameters?
1. What does one mean by the term "machine learning"?
Ans:Def 1:  Machine Learning is the science or art  of the programing  computers so that they can learn from the data.
Def 2: Machine Learning is the field of the study that gives computers the abilty to learn without being explicity programed.
# In[1]:


get_ipython().set_next_input('Q. 2.Can you think of 4 distinct types of issues where it shines');get_ipython().run_line_magic('pinfo', 'shines')

Q. 2.Can you think of 4 distinct types of issues where it shines
Ans: 1. Problems for which existing solutions require a lots of fine-tuning or long list of rules. One machine learning code can perform better than the traditional approach.
2. Complex problems for which traditional approach don't gives a good solutions. The best machine learning techniques can perhaps find a solutions.
3. Fluctuating Enviroments: A machine Learning system can adapt to the new data.
4. Getting Insights about the complex problems and large amount of the data.
Q.3.What is a labeled training set, and how does it work?
Ans: Labeled Training set the data in which we want to train our machine learning model and as the name suggest labeled in the  tarining set desired solution is alreay includes. 
or 
You split up the data containing known response variable values into two pieces. The training set is used to train the algorithm, and then you use the trained model on the test set to predict the response variable values that are already known.Q. 4.What are the two most important tasks that are supervised?

Solution:
The two most important supervised tasks are regression and classification. 
Spam filter classification and car price predetion using regrestion. 
Q. 5.Can you think of four examples of unsupervised tasks?
Solution: Common unsupervised tasks include clustering, visualization, dimensionality reduction, and association rule learning.

Q. 6.State the machine learning model that would be best to make a robot walk through various unfamiliar terrains?
Solution : Reinforcement Learning: In this model machine learning model learn by reword(for correct task) and penalities(for wrong task performed, and next time it will not perform that task)


Reinforced Learning
The best Machine Learning algorithm to allow a robot to walk in unknown terrain is Reinforced Learning, where the robot can learn from response of the terrain to optimize itself.Q.  7.Which algorithm will you use to divide your customers into different groups?
Ans: Clustring algorithm.
    
    The goal of cluster analysis in marketing is to accurately segment customers in order to achieve more effective customer marketing via personalization. A common cluster analysis method is a mathematical algorithm known as k-means cluster analysis, sometimes referred to as scientific segmentationQ. 8.Will you consider the problem of spam detection to be a supervised or unsupervised learning problem?
Ans: supervised learning problemQ. 9.What is the concept of an online learning system?
Solution. In the online learning system we tarin the machine learning model in the small batch and there is no need to train the whole traing set again if new data comes. 

def 2: 
In computer science, online machine learning is a method of machine learning in which data becomes available in a sequential order and is used to update the best predictor for future data at each step, as opposed to batch learning techniques which generate the best predictor by learning on the entire training data set at once. Online learning is a common technique used in areas of machine learning where it is computationally infeasible to train over the entire dataset, requiring the need of out-of-core algorithms. It is also used in situations where it is necessary for the algorithm to dynamically adapt to new patterns in the data, or when the data itself is generated as a function of time, e.g., stock price prediction. Online learning algorithms may be prone to catastrophic interference, a problem that can be addressed by incremental learning approaches.

Q. 10.What is out-of-core learning, and how does it differ from core learning?
Sol: The term out-of-core typically refers to processing data that is too large to fit into a computer’s main memory.
It devides the data in the mini batch and use the cocept online learning.

Q. 11.What kind of learning algorithm makes predictions using a similarity measure?
Sol : Learning algorithm that relies on a similarity measure to make predictions is instance-based algorithm.

Q. 12.What's the difference between a model parameter and a hyperparameter in a learning algorithm?
Ans: In summary, model parameters are estimated from data automatically and model hyperparameters are set manually and are used in processes to help estimate model parameters. Model hyperparameters are often referred to as parameters because they are the parts of the machine learning that must be set manually and tuned13.What are the criteria that model-based learning algorithms look for? What is the most popular method they use to achieve success? What method do they use to make predictions?

Sol: Model based learning algorithm search for the optimal value of parameters in a model that will give the best results for the new instances. We often use a cost function or similar to determine what the parameter value has to be in order to minimize the function. The model makes prediction by using the value of the new instance and the parameters in its function.

14.Can you name four of the most important Machine Learning challenges?
Solution: 1. Insufficent Quantity of the Data
    2. NonRepresentataive Training data
    3. Poor Quality Data
    4. Irrelevant Features
    5. Overfitting the data
    6. Underfitting the training DataQ. 15.What happens if the model performs well on the training data but fails to generalize the results to new situations? Can you think of three different options?
Sol: If the model performs poorly to new instances, then it has overfit on the training data. To solve this, we can do any of the following three: get more data, implement a simpler model, or eliminate outliers or noise from the existing data set.

Q. 16.What exactly is a test set, and why would you need one?
Ans: Test set is a set that you test your model (fit using training data) to see how it performs. Test set is necessary so that you can determine how good (or bad) your model performs.

Q. 17.What is a validation set's purpose?
Ans: Validation set is a set used to compare between different training models.


# In[7]:


get_ipython().set_next_input('Q. 18.What precisely is the train-dev kit, when will you need it, how do you put it to use');get_ipython().run_line_magic('pinfo', 'use')

Q. 18.What precisely is the train-dev kit, when will you need it, how do you put it to use
Ans :The goal of dev-set is to rank the models in term of their accuracy and helps us decide which model to proceed further with. Using Dev set we rank all our models in terms of their accuracy and pick the best performing modelQ. 19.What could go wrong if you use the test set to tune hyperparameters?
Ans: Cross-validation is a tool to compare models without needing a separate validation set. It is preferred over validation set because we can save from breaking of part of the training set to create a validation set, as having more data is valuable regardless