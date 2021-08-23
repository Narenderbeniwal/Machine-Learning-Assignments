#!/usr/bin/env python
# coding: utf-8
1. What is the concept of human learning? Please give two examples.
2. What different forms of human learning are there? Are there any machine learning equivalents?
3. What is machine learning, and how does it work? What are the key responsibilities of machine learning?
4. Define the terms "penalty" and "reward" in the context of reinforcement learning.
5. Explain the term "learning as a search"?
6. What are the various goals of machine learning? What is the relationship between these and human learning?
7. Illustrate the various elements of machine learning using a real-life illustration.
8. Provide an example of the abstraction method.
9. What is the concept of generalization? What function does it play in the machine learning process?
What is classification, exactly? What are the main distinctions between classification and regression?
11. What is regression, and how does it work? Give an example of a real-world problem that was solved using regression.
12. Describe the clustering mechanism in detail.
13. Make brief observations on two of the following topics:
i. Machine learning algorithms are used
ii. Studying under supervision
iii. Studying without supervision
iv. Reinforcement learning is a form of learning based on positive reinforcement.
Q. 1. What is the concept of human learning? Please give two examples.
Ans: It is the form of learning which requires higher order mental processes like thinking, reasoning, intelligence, etc. we learn different concepts from childhood. For example, when we see a dog and attach the term 'dog', we learn that the word dog refers to a particular animal. 
2. What different forms of human learning are there? Are there any machine learning equivalents?
Ans: There are three main types of learning: classical conditioning, operant conditioning, and observational learning. Both classical and operant conditioning are forms of associative learning, in which associations are made between events that occur together. Observational learning is just as it sounds: learning by observing others.

---Humans acquire knowledge through experience either directly or shared by others. Machines acquire knowledge through experience shared in the form of past data. We have the terms, Knowledge, Skill, and Memory being used to define intelligence. Just because you have good memory, that does not mean you are intelligent. And just because you are intelligent, it does not mean you should have a good memory. However, there are exceptions to these rules. Humans begin learning by memorizing. After few years, he realizes that mere capability to memorize is not intelligence. Then he practices on transforming the data stored in memory to knowledge and applies them to develop skills to solve problems faced in real life. A person with good memory and more knowledge without the required skills cannot be considered intelligent. Search engines replaces human memory and these days the focus is on acquiring intelligence by making use of data available on the web. In humans, learning speed depends on individuals and in machines, learning speed depends on the algorithm selected and the volume of examples exposed to it.
--

--In ML, Transfer Learning is a technique that reuses a model that was created by machine learning experts and that has already been trained on a large dataset. Transfer learning leverages information extracted from one set of distributions. In humans, transfer of knowledge to students is often done by teachers and tuition providers. This may not make the students intelligent. But in the case of machine learning, transfer learning makes the transferee as intelligent as the transferor. In the case of humans, transfer learning only transfers the knowledge and it depends on the inherent intelligence of the transferee to enhance his/her problem solving skills.
--Q. 3. What is machine learning, and how does it work? What are the key responsibilities of machine learning?
Ans: Machine learning is the art of the computer progarming so that they can learn from the data. To work any machine learning model 1st we should train the model,  then we can perform the specified task on the trained model.
 --machine learning is a subset of AI (artificial intelligence) and enables machines to step into a mode of self-learning without being programmed explicitly. Machine learning-enabled programs are able to learn, grow, and change by themselves when exposed to new data. With the help of this technology, computers can find valuable information without being programmed about where to look for specific piece information. Instead, they achieve it by utilizing algorithms which iteratively learn from data.--
---key responsibilities of machine learning engineer?--

1. Designing ML systems.
2. Researching and implementing ML algorithms and tools.
3. Selecting appropriate data sets.
4. Picking appropriate data representation methods.
5. Identifying differences in data distribution that affects model performance.
6. Verifying data quality.
7. Transforming and converting data science prototypes.
8. Performing statistical analysis.
9. Running machine learning tests.
10. Using results to improve models.
11. Training and retraining systems when needed.
12.Extending machine learning libraries.
13. Developing machine learning apps according to client requirements.


# Q. 4. Define the terms "penalty" and "reward" in the context of reinforcement learning.
# Ans: "penalty" in the  reinforcement learning is defined as when the machine perform any task wrong or incorrect. 
#     "reward" in the  reinforcement learning is defined as when the machine perform any task right or correct. 
# 
Q. 5.  Explain the term "learning as a search"?
This conceptualization of developing learning systems as a search problem helps to make clear many related concerns in applied machine learning.
# Q. 6. What are the various goals of machine learning? What is the relationship between these and human learning?
Sol: Its goal and usage is to build new and/or leverage existing algorithms to learn from data, in order to build generalizable models that give accurate predictions, or to find patterns, particularly with new and unseen similar data.

----Humans acquire knowledge through experience either directly or shared by others. Machines acquire knowledge through experience shared in the form of past data. We have the terms, Knowledge, Skill, and Memory being used to define intelligence. Just because you have good memory, that does not mean you are intelligent. And just because you are intelligent, it does not mean you should have a good memory. However, there are exceptions to these rules. Humans begin learning by memorizing. After few years, he realizes that mere capability to memorize is not intelligence. Then he practices on transforming the data stored in memory to knowledge and applies them to develop skills to solve problems faced in real life. A person with good memory and more knowledge without the required skills cannot be considered intelligent. Search engines replaces human memory and these days the focus is on acquiring intelligence by making use of data available on the web. In humans, learning speed depends on individuals and in machines, learning speed depends on the algorithm selected and the volume of examples exposed to it.
--

--In ML, Transfer Learning is a technique that reuses a model that was created by machine learning experts and that has already been trained on a large dataset. Transfer learning leverages information extracted from one set of distributions. In humans, transfer of knowledge to students is often done by teachers and tuition providers. This may not make the students intelligent. But in the case of machine learning, transfer learning makes the transferee as intelligent as the transferor. In the case of humans, transfer learning only transfers the knowledge and it depends on the inherent intelligence of the transferee to enhance his/her problem solving skills.
--
# ## Q.7. Illustrate the various elements of machine learning using a real-life illustration.
# 
# ![machinelearning.jpeg](attachment:machinelearning.jpeg)
# 
Q. 8. Provide an example of the abstraction method.
Ans :Abstraction is a technique of hiding unnecessary details from the user. The user is only given access to the details that are relevant. Vehicle operations or ATM operations are classic examples of abstractions in the real world. ... While interfaces provide 100 % abstraction, abstract classes provide partial abstraction.Q. 9. What is the concept of generalization? What function does it play in the machine learning process?
Ans: Generalization refers to your model's ability to adapt properly to new, previously unseen data, drawn from the same distribution as the one used to create the model.

--In machine learning, generalization is a definition to demonstrate how well is a trained model to classify or forecast unseen data. Training a generalized machine learning model means, in general, it works for all subset of unseen data. An example is when we train a model to classify between dogs and cats. If the model is provided with dogs images dataset with only two breeds, it may obtain a good performance. But, it possibly gets a low classification score when it is tested by other breeds of dogs as well. This issue can result to classify an actual dog image as a cat from the unseen dataset. Therefore, data diversity is very important factor in order to make a good prediction. In the sample above, the model may obtain 85% performance score when it is tested by only two dog breeds and gains 70% if trained by all breeds. However, the first possibly gets a very low score (e.g. 45%) if it is evaluated by an unseen dataset with all breed dogs. This for the latter can be unchanged given than it has been trained by high data diversity including all possible breeds.

It should be taken into account that data diversity is not the only point to care in order to have a generalized model. It can be resulted by nature of a machine learning algorithm, or by poor hyper-parameter configuration. In this post we explain all determinant factors. There are some methods (regularization) to apply during model training to ensure about generalization. But before, we explain bias and variance as well as underfitting and overfitting.

--
# In[ ]:




Q. 10 What is classification, exactly? What are the main distinctions between classification and regression?
---Grouping of things with similar properties is called classification. We can classify different things based on whether they are living or non living, metals or non-metals. It is also possible to classify objects based on their size, solubility in water etc. By classifying things/objects we can make our work easy.

=-=--=
1. In Regression, the output variable must be of continuous nature or real value.	
1. In Classification, the output variable must be a discrete value.
2. The task of the regression algorithm is to map the input value (x) with the continuous output variable(y).	
2. The task of the classification algorithm is to map the input value(x) with the discrete output variable(y).
3. Regression Algorithms are used with continuous data.	
3. Classification Algorithms are used with discrete data.
4. In Regression, we try to find the best fit line, which can predict the output more accurately.	
4. In Classification, we try to find the decision boundary, which can divide the dataset into different classes.
5. Regression algorithms can be used to solve the regression problems such as Weather Prediction, House price prediction, etc.	
5. Classification Algorithms can be used to solve classification problems such as Identification of spam emails, Speech Recognition, Identification of cancer cells, etc.Q. 11. What is regression, and how does it work? Give an example of a real-world problem that was solved using regression.
Ans: Regression is a statistical method used in finance, investing, and other disciplines that attempts to determine the strength and character of the relationship between one dependent variable (usually denoted by Y) and a series of other variables (known as independent variables).
--- Medical researchers often use linear regression to understand the relationship between drug dosage and blood pressure of patients.-Q. 12. Describe the clustering mechanism in detail.
Clustering is the task of dividing the population or data points into a number of groups such that data points in the same groups are more similar to other data points in the same group than those in other groups. In simple words, the aim is to segregate groups with similar traits and assign them into clusters.

Let’s understand this with an example. Suppose, you are the head of a rental store and wish to understand preferences of your costumers to scale up your business. Is it possible for you to look at details of each costumer and devise a unique business strategy for each one of them? Definitely not. But, what you can do is to cluster all of your costumers into say 10 groups based on their purchasing habits and use a separate strategy for costumers in each of these 10 groups. And this is what we call clustering.13. Make brief observations on two of the following topics:
i. Machine learning algorithms are used
ii. Studying under supervision
iii. Studying without supervision
iv. Reinforcement learning is a form of learning based on positive reinforcement.
Ans: 
