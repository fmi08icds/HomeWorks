# Homework 5 - Jupyter Notebook

## 1. a) True

Three metrics are more difficult than one (e.g., only accuracy) as one algorithm might not be strictly better than the other in all metrics. With different "winners" in different measures it becomes necessary to find tradeoffs between measures

## 2. d) 98%, 9s, and 9MB

Option b) does not meet the runtime requirement. Out of the three other options (that all meet the two satisficing metrics), option d) achieves the highest accuracy

## 3. a)

Runtime and memory have upper bounds but the city did not tell us to be as fast as possible or have models as small as possible -> satisficing.
Accuracy is an optimizing metric, because the requirement is to be as accurate as possible

## 4. b) 9.5M train / 250k dev / 250k test

Given the large size of the dataset (10M images), we can afford to assign only 5% of the data to dev and test set. Plus, option b) also has equal size for dev and test as discussed in class

## 5. b) False

The dev and test set distributions will not be altered by this (but stay similar), so we can still assume good dev set performance to generalize to good test set performance. Plus, as stated in the question, we expect the data to help our algorithm, for instance by adding new, previously not covered examples of bird pictures to the training data.

## 6. a) [and thereby also d]

This is where the distributions matter. Adding these new, different images would change the test set to be different from the final use case (in security cameras). Plus, by altering the distribution of the test set, the dev and test set now have different distributions and thus d) is also correct.

## 7. d)

There is insufficient information to tell, because we don't have a benchmark error to compare performance against. Without a benchmark error, we can't say if we have high/low bias or variance

## 8. b) 0.3% 

As expert #1 managed to get 0.3% errors, we know that this level of performance is possible and thus a proxy for Bayes error

## 9. a) 

Bayes error is the best possible case so an algorithm's performance cannot be better. An algorithm can, however, outperform humans

## 10. c) 

A bigger model might be able to get the training error closer to the human-level-performance. 
I did not choose a second option, because 
	
1. Regularization should be decreased, not increased (We don't have a variance but a bias problem as training and dev error are quite close but both far away from the human-level); Thus, b) is wrong
2. We don't have a variance problem, so option a) is also incorrect 

## 11. b) and d)

- We have likely overfit to the dev set as its error rate is close to that of the training set but far away from the test set error. 
- By increasing the size of the dev set, we might be able to reduce this overfitting by adding new, differently distributed images

## 12. b) and d)

- If we are confident that the test error is accurate (and not due to irregularities), then Bayes error is <= 0.05%
- Because we can no longer use the human-level-performance as proxy for Bayes error, we no longer have an estimate for it to be used for bias measuring.

## 13. c)

A suitable metric might be F1-score. If we were to only optimize for false negative rate, we would drive up the false positive rate and thus cause more false alarms for birds

## 14. a)

The number of images of the new species is too low to be used in training or for generating enough synthetic data. Instead, use the data in evaluation

## 15. a), c), and d)

The crucial issue is training time as it limits the number of iteration. So anything reducing that time can be valuable. These include:
- Trying fewer datapoints
- Having faster computers

Simply reusing the bird model with identical hyperparameters is not a good idea as the model was trained for a different task.
