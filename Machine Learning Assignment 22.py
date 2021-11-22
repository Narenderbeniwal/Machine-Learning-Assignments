#!/usr/bin/env python
# coding: utf-8
1. Is there any way to combine five different models that have all been trained on the same training data and have all achieved 95 percent precision? If so, how can you go about doing it? If not, what is the reason?
2. What's the difference between hard voting classifiers and soft voting classifiers?
3. Is it possible to distribute a bagging ensemble's training through several servers to speed up the process? Pasting ensembles, boosting ensembles, Random Forests, and stacking ensembles are all options.

4. What is the advantage of evaluating out of the bag?

5. What distinguishes Extra-Trees from ordinary Random Forests? What good would this extra randomness do? Is it true that Extra-Tree Random Forests are slower or faster than normal Random Forests?

6. Which hyperparameters and how do you tweak if your AdaBoost ensemble underfits the training data?

7. Should you raise or decrease the learning rate if your Gradient Boosting ensemble overfits the training set?1. Is there any way to combine five different models that have all been trained on the same training data and have all achieved 95 percent precision? If so, how can you go about doing it? If not, what is the reason?
Sol: You can combine these models into a voting ensemble to try to get better results. This works better on models that are very different, and trained on different training instances, but it will still work as long as the models are very different.Q. 2. What's the difference between hard voting classifiers and soft voting classifiers?
Sol: Hard voting classifiers: Counts the votes of each classifier in the ensemble and picks the class that gets the most votes
Soft voting classifier: computes the average estimated class probability for each class and picks the class with the highest probability. Gives high-confidence votes more weight, but only works if every classifier is able to estimate class probabilities.




Q. 3. Is it possible to distribute a bagging ensemble's training through several servers to speed up the process? Pasting ensembles, boosting ensembles, Random Forests, and stacking ensembles are all options.
Sol: It is possible to speed up training of bagging, pasting, and random forests because each predictor is independent of the others.
boosting ensemble predictors are built based on the previous predictor, so you separating training will not help.
For stacking ensembles, all predictors for one layer has to be trained before the next layer.
Q. 4. What is the advantage of evaluating out of the bag?
Sol: Each predictor in a bagging ensemble is evaluated using instances it was not trained on. This creates an unbiased eval of the ensemble without the need for a validation set. You can have more instances for training, and your ensemble can perform slightly better.
Q.5 What makes Extra-Trees more random than regular Random Forests? How can
this extra randomness help? Are Extra-Trees slower or faster than regular Random Forests?

Sol:Extra-trees use random thresholds for each feature, instead of finding the best threshold. The extra randomness acts like a form of regularization and can be used to fix overfitting.
However, this is neither faster nor slower than random forests when making decisions.
Q. 6. Which hyperparameters and how do you tweak if your AdaBoost ensemble underfits the training data?

Sol: Increase estimators
 Increase Learning Rate
 Decrease regularization hyperparameters.
Q. 7. Should you raise or decrease the learning rate if your Gradient Boosting ensemble overfits the training set?

Sol: Try decreasing the learning rate or use early stopping to find the right number of predictors (there are probably too many)

# In[ ]:




