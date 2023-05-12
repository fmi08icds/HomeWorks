# HW 5 - Bird Recognition

## 1. Problem Statement
Having three evaluation metrics makes it harder for you to quickly choose between two different algorithms, and will slow down the speed with which your team can iterate. True/False?

a) True

## 2.
If you had the three following models, which one would you choose?

d) Test Accuracy 98%, Runtime 9 sec, Memory size 9MB

because: maximum test accuracy with runtime under 10 sec and model fitting in 10MB of memory

## 3. 
Based on the city’s requests, which of the following would you say is true?

a) Accuracy is an optimizing metric; running time and memory size are a satisficing metrics.

## 4. Structuring your data
Before implementing your algorithm, you need to split your data into train/dev/test sets. Which of these do you think is the best choice?

b) Train/Dev/Test = $9,500,000/250,000/250,000$

## 5. 
You should not add the citizens’ data to the training set, because this will cause the training and dev/test set distributions to become different, thus hurting dev and test set performance. True/False?

b) False

because: different training and dev set is ok, but dev and test set need to be the same

## 6.
One member of the City Council knows a little about machine learning, and thinks you should add the $1,000,000$ citizens’ data images to the test set. You object because:

a) The test set no longer reflects the distribution of data (security cameras) you most care about.

d) This would cause the dev and test set distributions to become different. This is a bad idea because you’re not aiming where you want to hit.

## 7.
Do you agree?

d) No, because there is insufficient information to tell.

## 8.
If your goal is to have “human-level performance” be a proxy (or estimate) for Bayes error, how would you define “human-level performance”?

b) $0.3\%$ (accuracy of expert #1)

## 9. 
Which of the following statements do you agree with?

a) A learning algorithm’s performance can be better than human-level performance but it can never be better than Bayes error.

## 10. 
Based on the evidence you have, which two of the following four options seem the most promising to try? (Check two options.)

c) Train a bigger model to try to do better on the training set.

note: there were only the three answers a) b) and c) and not four like the question stated. answers a) and b) do not seem promising for reducing bias so i only chose one answer. but because increasing regularization is not promising, reducing/eliminating regularization is (see Machine Learning Yearning chapter 25).

## 11.
What does this mean? (Check the two best options.)

b) You should try to get a bigger dev set.

d) You have overfit to the dev set. 

## 12.
What can you conclude? (Check all that apply.)

b) If the test set is big enough for the $0.05\%$ error estimate to be accurate, this implies Bayes error is $\leq 0.05$ 

d) It is now harder to measure avoidable bias, thus progress will be slower going forward.

## 13.
What should you do?

c) Rethink the appropriate metric for this task, and ask your team to tune to the new metric. 

## 14.
You have only $1,000$ images of the new species of bird. The city expects a better system from you within the next 3 months. Which of these should you do first?

a) Use the data you have to define a new evaluation metric (using a new dev/test set) taking into account the new species, and use that to drive further progress for your team. 

## 15. 
Which of the statements do you agree with?  (Check all that agree.) 

a) If $100,000,000$ examples is enough to build a good enough Cat detector, you might be better of training with just $10,000,000$ examples to gain a $\approx 10 \times$ improvement in how quickly you can run experiments, even if each model performs a bit worse because it’s trained on less data.

c) Needing two weeks to train will limit the speed at which you can iterate.

d) Buying faster computers could speed up your teams’ iteration speed and thus your team’s productivity. 
