## Homework 5 

1- Having three evaluation metrics makes it harder for you to quickly choose between two different algorithms, and will slow down the speed with which your team can iterate. True/False?

a)True

2- If you had the three following models, which one would you choose?
d)

Based on the information provided, the correct answer is option d). The algorithm in option d) meets the requirements as it has a sufficiently high accuracy, and its runtime and memory size are within the specified limits set by the city.


3-

a)Accuracy is an optimizing metric; running time and memory size are a satisficing metrics.


4-

b)

The specific choice of split depends on various factors, including the size of the dataset, the complexity of the problem, and the available resources. The larger the test set the more confident I can be about the generalization of the model.


5-

False) In this case, adding the citizens' data to the training set can potentially benefit the algorithm. With an additional 1,000,000 labeled images, the citizens' data can significantly increase the size and diversity of the training set. This can help the algorithm learn a better representation of the data and potentially improve its performance.


6-

a) The test set no longer reflects the distribution of data (security cameras) you most care about.


7-

d)
No, because there is insufficient information to tell.

8-

b)
0.3% (accuracy of expert #1)


9-

a) A learning algorithm’s performance can be better human-level performance but it can never be better than Bayes error.

10-

b)Try decreasing regularization.
c)Train a bigger model to try to do better on the training set.

11-

b)You should try to get a bigger dev set.

d)You have overfit to the dev set.

12- 

d)It is now harder to measure avoidable bias, thus progress will be slower going forward.

13-

c)Rethink the appropriate metric for this task, and ask your team to tune to the new metric.

14-

a)Use the data you have to define a new evaluation metric (using a new dev/test set) taking into account the new species, and use that to drive further progress for your team.

15-

a)If 100,000,000 examples is enough to build a good enough Cat detector, you might be better of training with just 10,000,000 examples to gain a ≈10x improvement in how quickly you can run experiments, even if each model performs a bit worse because it’s trained on less data.
d)Buying faster computers could speed up your teams’ iteration speed and thus your team’s productivity.
c)Needing two weeks to train will limit the speed at which you can iterate.