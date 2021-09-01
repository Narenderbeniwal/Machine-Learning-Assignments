#!/usr/bin/env python
# coding: utf-8
	•	Define the Bayesian interpretation of probability.
	•	Define probability of a union of two events with equation.
	•	What is joint probability? What is its formula?
	•	What is chain rule of probability?
	•	What is conditional probability means? What is the formula of it?
	•	What are continuous random variables?
	•	What are Bernoulli distributions? What is the formula of it?
	•	What is binomial distribution? What is the formula?
	•	What is Poisson distribution? What is the formula?
	•	Define covariance.
	•	Define correlation
	•	Define sampling with replacement. Give example.
	•	What is sampling without replacement? Give example.
	•	What is hypothesis? Give example.
Q. 1 Define the Bayesian interpretation of probability.

Sol: Bayesian probability is an interpretation of the concept of probability, in which, instead of frequency or propensity of some phenomenon, probability is interpreted as reasonable expectation representing a state of knowledge or as quantification of a personal beliefQ. 2 Define probability of a union of two events with equation.

Sol:  P(A∪B)=P(A)+P(B)- P ( A ∩ B ) 
# ![joint-probability.webp](attachment:joint-probability.webp)Q. 3 What is joint probability? What is its formula?
#  Sol: A joint probability, in probability theory, refers to the probability that two events will both occur. In other words, joint probability is the likelihood of two events occurring together.
# 
# Where:
# 
# P(A ⋂ B) is the notation for the joint probability of event “A” and “B”.
# 
# 
# P(A) is the probability of event “A” occurring.
# 
# 
# P(B) is the probability of event “B” occurring.
# 
# 
Q.4 What is chain rule of probability?

Sol: Chain rule for conditional probability:
P(A1∩A2∩⋯∩An)=P(A1)P(A2|A1)P(A3|A2,A1)⋯P(An|An−1An−2⋯A1)

In a factory there are 100 units of a certain product, 5 of which are defective. We pick three units from the 100 units at random. What is the probability that none of them are defective?

Solution
Let us define Ai as the event that the ith chosen unit is not defective, for i=1,2,3. We are interested in P(A1∩A2∩A3). Note that
P(A1)=95100.
Given that the first chosen item was good, the second item will be chosen from 94 good units and 5 defective units, thus
P(A2|A1)=9499.
Given that the first and second chosen items were okay, the third item will be chosen from 93 good units and 5 defective units, thus
P(A3|A2,A1)=9398.
Thus, we have

P(A1∩A2∩A3)	=P(A1)P(A2|A1)P(A3|A2,A1)
=9510094999398
=0.8560

As we will see later on, another way to solve this problem is to use counting arguments.
Q.5 What is conditional probability means? What is the formula of it?

Sol: Conditional probability is defined as the likelihood of an event or outcome occurring, based on the occurrence of a previous event or outcome. Conditional probability is calculated by multiplying the probability of the preceding event by the updated probability of the succeeding, or conditional, event.


For example:


Event A is that an individual applying for college will be accepted. There is an 80% chance that this individual will be accepted to college.
Event B is that this individual will be given dormitory housing. Dormitory housing will only be provided for 60% of all of the accepted students.
P (Accepted and dormitory housing) = P (Dormitory Housing | Accepted) P (Accepted) = (0.60)*(0.80) = 0.48.
A conditional probability would look at these two events in relationship with one another, such as the probability that you are both accepted to college, and you are provided with dormitory housing.

P(B|A) = P(A and B) / P(A)
Or:

P(B|A) = P(A∩B) / P(A)
Q. 6.What are continuous random variables?

Sol: A continuous random variable is one which takes an infinite number of possible values. ... The probability of observing any single value is equal to 0, since the number of values which may be assumed by the random variable is infinite
# ![pdf-bernoulli.png](attachment:pdf-bernoulli.png)Q. 7 What are Bernoulli distributions? What is the formula of it?
# 
# Sol: A Bernoulli distribution is a discrete probability distribution for a Bernoulli trial — a random experiment that has only two outcomes (usually called a “Success” or a “Failure”). For example, the probability of getting a heads (a “success”) while flipping a coin is 0.5. The probability of “failure” is 1 – P (1 minus the probability of success, which also equals 0.5 for a coin toss). It is a special case of the binomial distribution for n = 1. In other words, it is a binomial distribution with a single trial (e.g. a single coin toss).
Q.8 What is binomial distribution? What is the formula?


Sol:
The binomial distribution is a common discrete distribution used in statistics, as opposed to a continuous distribution, such as the normal distribution. The binomial distribution, therefore, represents the probability for x successes in n trials, given a success probability p for each trial. The binomial distribution formula is for any random variable X, given by;  P(x:n,p) = nCxx px (1-p)n-x Or P(x:n,p) = nCxx px (q)n-x, where, n is the number of experiments, p is probability of success in a single experiment, q is probability of failure in a single experiment (= 1 – p) and takes values as 0, 1, 2, 3, 4, …, n.Q.9 What is Poisson distribution? What is the formula?
Sol:

In statistics, a Poisson distribution is a probability distribution that is used to show how many times an event is likely to occur over a specified period. ... The Poisson distribution is a discrete function, meaning that the variable can only take specific values in a (potentially infinite) list.

𝑓(𝑥)=𝑃(𝑋=𝑥)=𝑒−𝜆𝜆𝑥𝑥!for x = 0,1,2…. ∞Q. 10. Define covariance.

Sol: Covariance provides insight into how two variables are related to one another. More precisely, covariance refers to the measure of how two random variables in a data set will change together. A positive covariance means that the two variables at hand are positively related, and they move in the same direction.Q. 11 Define corelation

Sol: Correlation means association - more precisely it is a measure of the extent to which two variables are related. ... Therefore, when one variable increases as the other variable increases, or one variable decreases while the other decreases. An example of positive correlation would be height and weight.Q. 12 Define sampling with replacement. Give example.

Sol: Sampling is called with replacement when a unit selected at random from the population is returned to the population and then a second element is selected at random. Whenever a unit is selected, the population contains all the same units, so a unit may be selected more than once.
Q. 13 What is sampling without replacement? Give example.

Sol :in simple random sampling without replacement, a chosen unit is not returned to the population after the drawn is made.
Q. 14 What is hypothesis? Give example.

Sol: let's say you have a bad breakout the morning after eating a lot of greasy food. You may wonder if there is a correlation between eating greasy food and getting pimples. You propose the hypothesis: Eating greasy food causes pimples.