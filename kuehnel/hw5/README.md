# Homework 5

## 1. Problem Statement

Having three evaluation metrics makes it harder for you to quickly choose between two different algorithms, 
and will slow down the speed with which your team can iterate. 
True/False?

True

(Although the amount of time may be insignificant)


 

## 2. After further discussions, the city narrows down its criteria to:

- "We need an algorithm that can let us know a bird is flying over Peacetopia as accurately as possible."

- "We want the trained model to take no more than to classify a new image.”

- “We want the model to fit in 10MB of memory.”

If you had the three following models, which one would you choose? (a, b, c, d)

Answer: d)

    Test Accuracy 	      Runtime     	 Memory size    
         98 %              9 sec 	           9MB




## 3. which one is true?

Answer: a) Accuracy is an optimizing metric; running time and memory size are a satisficing metrics.

## 4. Structuring your data

Answer: b) Train/Dev/Test = 9,500.000 / 250,000 / 250,000

## 5.

b) False

## 6.

d) This would cause the dev and test set distributions to become different. 
This is a bad idea because you’re not aiming where you want to hit.

## 7.

c) No, because this shows your variance is higher than your bias.

## 8.

b) 0.3 % (accuracy of expert #1)

## 9. 

a) A learning algorithm’s performance can be better than human-level 
performance but it can never be better than Bayes error.

## 10.

a) Get a bigger training set to reduce variance.

b) Try increasing regularization.

## 11.

a) You should get a bigger test set.

d) You have overfit to the dev set.

## 12.

b) If the test set is big enough for the 0.05 % error estimate to be accurate, this implies Bayes error is ≤ 0.05

d) It is now harder to measure avoidable bias, thus progress will be slower going forward.

## 13.

d) Pick false negative rate as the new metric, and use this new metric to drive all further development.

## 14.

a) Use the data you have to define a new evaluation metric (using a new dev/test set) taking into account the new species, and use that to drive further progress for your team.

c) Try data augmentation/data synthesis to get more images of the new type of bird.

## 15.

a) If 100,000,000 examples is enough to build a good enough Cat detector, 
you might be better of training with just 10,000,000 examples to gain a≈10x improvement
in how quickly you can run experiments, even if each model performs a bit worse 
because it’s trained on less data.

d) Buying faster computers could speed up your teams’ iteration speed and thus your team’s productivity.
