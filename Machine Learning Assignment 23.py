#!/usr/bin/env python
# coding: utf-8
1. What are the key reasons for reducing the dimensionality of a dataset? What are the major disadvantages?
2. What is the dimensionality curse?
3. Tell if its possible to reverse the process of reducing the dimensionality of a dataset? If so, how can you go about doing it? If not, what is the reason?

4. Can PCA be utilized to reduce the dimensionality of a nonlinear dataset with a lot of variables?

5. Assume you're running PCA on a 1,000-dimensional dataset with a 95 percent explained variance ratio. What is the number of dimensions that the resulting dataset would have?

6. Will you use vanilla PCA, incremental PCA, randomized PCA, or kernel PCA in which situations?

7. How do you assess a dimensionality reduction algorithm's success on your dataset?

8. Is it logical to use two different dimensionality reduction algorithms in a chain?
Q. 1. What are the key reasons for reducing the dimensionality of a dataset? What are the major disadvantages?
Ans. 1. It helps in data compression, and hence reduced storage space.
2. It reduces computation time.
3. It also helps remove redundant features, if any.
major disadvantages: 1. Loss of information 
2.  It may lead to some amount of data loss.
3. PCA tends to find linear correlations between variables, which is sometimes undesirable.
4. PCA fails in cases where mean and covariance are not enough to define datasets.Q. 2. What is the dimensionality curse?
Sol: The curse of dimensionality basically means that the error increases with the increase in the number of features. It refers to the fact that algorithms are harder to design in high dimensions and often have a running time exponential in the dimensionsQ. 3. Tell if its possible to reverse the process of reducing the dimensionality of a dataset? If so, how can you go about doing it? If not, what is the reason?
Sol: . No, dimensionality reduction is not reversible in general.Q. 4. Can PCA be utilized to reduce the dimensionality of a nonlinear dataset with a lot of variables?
Sol: Depends on dataset. If it is comprised of points that are perfectly aligned, PCA can reduce the dataset down to 1 dimension and preserve 95% of the variance.Q. 5. Assume you're running PCA on a 1,000-dimensional dataset with a 95 percent explained variance ratio. What is the number of dimensions that the resulting dataset would have?
Sol: hard to say, it depends on dataset.

Q. 6. Will you use vanilla PCA, incremental PCA, randomized PCA, or kernel PCA in which situations?
Sol: Vanilla PCA: the dataset fit in memory
Incremental PCA: larget dataset that don't fit in memory, online taks
Randomized PCA: considerably reduce dimensionality and the dataset fit the memory.
kenrl PCA: used for nonlinear PCA
Q.7. How do you assess a dimensionality reduction algorithm's success on your dataset?
Sol: measure the reconstruction error
measure the performance in second Machine Learning algorithm
# In[ ]:


get_ipython().set_next_input('Q. 8. Does it make any sense to chain two different dimensionality algorithms');get_ipython().run_line_magic('pinfo', 'algorithms')

Sol: Yes 

