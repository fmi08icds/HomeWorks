# Homework 5
In this homework we answer the questions proposed in the notebook [here](https://github.com/fmi08icds/Coding/blob/main/notebooks/day5.ipynb).

### 1 

Having three evaluation metrics makes it harder for you to quickly choose between two different algorithms, and will slow down the speed with which your team can iterate. True/False?

>This is false, having three criteria makes it easier to evaluate the algorithms, as we seam to have a better understanding of the problem. More clear criteria can narrow the choices down and leafs less algorithms to be investigated more closely.

### 2
After further discussions, the city narrows down its criteria to: 
    
- We need an algorithm that can let us know a bird is flying over Peacetopia as accurately as possible.
- We want the trained model to take no more than $10sec$ to classify a new image.
- We want the model to fit in 10MB of memory.


If you had the three following models, which one would you choose?,

a)

|     Test Accuracy        |     Runtime     |     Memory size    |
| ---------------- | :------: | ----------------- |
| $97%$| 1 sec| 3MB|

b)

|     Test Accuracy        |     Runtime     |     Memory size    |
| ---------------- | :------: | ----------------- |
| $99%$| 13 sec| 9MB|

c)

|     Test Accuracy        |     Runtime     |     Memory size    |
| ---------------- | :------: | ----------------- |
| $97%$| 3 sec| 2MB|

d)

|     Test Accuracy        |     Runtime     |     Memory size    |
| ---------------- | :------: | ----------------- |
| $98%$| 9 sec| 9MB|

> Model d) is the best Model according tho the requirements.


### 3
Based on the city’s requests, which of the following would you say is true?

a) Accuracy is an optimizing metric; running time and memory size are a satisficing metrics.

b) Accuracy is a satisficing metric; running time and memory size are an optimizing metric.

c) Accuracy, running time and memory size are all optimizing metrics because you want to do well on all three.

d) Accuracy, running time and memory size are all satisficing metrics because you have to do sufficiently well on all three for your system to be acceptable.

> a) is the only correct answer here.

### 4

Before implementing your algorithm, you need to split your data into train/dev/test sets. Which of these do you think is the best choice?

a) Train/Dev/Test = 6,000,000/1,000,000/3,000,000

b) Train/Dev/Test = 9,500,000/250,000/250,000

c) Train/Dev/Test = 3,333,334/3,333,333/3,333,333

d) Train/Dev/Test = 6,000,000/3,000,000/1,000,000

> according to your slides b) is the correct answer

### 5 
You should not add the citizens’ data to the training set, because this will cause the training and dev/test set distributions to become different, thus hurting dev and test set performance. True/False?

> If we add the data then we should add them not only to the train set but also to the dev and test set so that we have an equal distribution. It really depends on the data itself whether it is a good idea to add it or not. If the citizens pictures are labeled correctly and show birds infront of the sky then I see no problem adding them, things like picture quality and scaling factors can be fixed and normalized.

### 6 
One member of the City Council knows a little about machine learning, and thinks you should add the 1,000,000 citizens’ data images to the test set. You object because:

a) the test set no longer reflects the distribution of data (security cameras) you most care about.

b) A bigger test set will slow down the speed of iterating because of the computational expense of evaluating models on the test set.

c) the $1,000,000$ citizens’ data images do not have a consistent $x \rightarrow y$ mapping as the rest of the data.

d) This would cause the dev and test set distributions to become different. This is a bad idea because you’re not aiming where you want to hit.

> a) & d) are both true, if the labeling is not correct in the data then c) is also true.  

### 7

You train a system, and its errors are as follows (error = 100%-Accuracy):

|Training set error| Dev set error|
| ------------ | ---------|
| $4\%$ | $4.5\%$ | 

This suggests that one good avenue for improving performance is to train a bigger network so as to drive down the $4.0\%$ training error. Do you agree?

a) Yes, because having $4.0\%$ training error shows you have high bias.

b) Yes, because this shows your bias is higher than your variance.

c) No, because this shows your variance is higher than your bias.

d) No, because there is insufficient information to tell.

> c)

### 8
You ask a few people to label the dataset so as to find out what is human-level performance. You find the following levels of accuracy:

|Bird watching expert 1| Bird watching expert 2 | Normal Person 1 (not a bird watching expert)| Normal Person 2 (not a bird watching expert)|
| -------- | ----------- | ---------- | -----------| 
| $0.3\%$ error | $0.5\%$ error | $1.0\%$ error | $1.2\%$ error | 

If your goal is to have “human-level performance” be a proxy (or estimate) for Bayes error, how would you define “human-level performance”?

a) $0.0\%$ (because it is impossible to do better than this)

b) $0.3\%$ (accuracy of expert #1) 

c) $0.4\%$ (average of $0.3$ and $0.5$)

d) $0.75\%$ (average of all four numbers above)

> b)

### 9

Which of the following statements do you agree with?

a) A learning algorithm’s performance can be better than human-level performance but it can never be better than Bayes error.

b) A learning algorithm’s performance can never be better than human-level performance but it can be better than Bayes error. 

c) A learning algorithm’s performance can never be better than human-level performance nor better than Bayes error. 

d) A learning algorithm’s performance can be better than human-level performance and better than Bayes error.

> a)

### 10

You find that a team of ornithologists debating and discussing an image gets an even better $0.1\%$ performance, so you define that as “human-level performance.” After working further on your algorithm, you end up with the following: 

| Human-level performance | Training set error | Dev set error | 
| -------------| --------------| ------------ |
| $0.1\%$ | $2.0\%$ | $2.1\%$ | 

Based on the evidence you have, which two of the following four options seem the most promising to try? (Check two options.)

a) Get a bigger training set to reduce variance.

b) Try increasing regularization.

c) Train a bigger model to try to do better on the training set.

> b) & c)

### 11 
You also evaluate your model on the test set, and find the following:

| Human-level performance | Training set error | Dev set error | Test set error |
| -------------| --------------| ------------ | ------------- | 
|$0.1\%$ | $2.0\%$ | $2.1\%$ | $7.0\%$ | 

What does this mean? (Check the two best options.)

a) You should get a bigger test set.

b) You should try to get a bigger dev set.

c) You have underfit to the dev set.

d) You have overfit to the dev set. 

> b) & d)


### 12

After working on this project for a year, you finally achieve: 
| Human-level performance | Training set error |Dev set error | 
|----------|----------| --------- | 
| $0.10\%$ | $0.05\%$ | $0.05\%$ | 

What can you conclude? (Check all that apply.)

a) With only $0.09\%$ further progress to make, you should quickly be able to close the remaining gap to $0\%$

b) If the test set is big enough for the $0.05\%$ error estimate to be accurate, this implies Bayes error is $\leq 0.05$ 

c) This is a statistical anomaly (or must be the result of statistical noise) since it should not be possible to surpass human-level performance. 

d) It is now harder to measure avoidable bias, thus progress will be slower going forward.

> d)

### 13

It turns out Peacetopia has hired one of your competitors to build a system as well. Your system and your competitor both deliver systems with about the same running time and memory size. However, your system has higher accuracy! However, when Peacetopia tries out your and your competitor’s systems, they conclude they actually like your competitor’s system better, because even though you have higher overall accuracy, you have more false negatives (failing to raise an alarm when a bird is in the air). 

What should you do?

a) Look at all the models you’ve developed during the development process and find the one with the lowest false negative error rate. 

b) Ask your team to take into account both accuracy and false negative rate during development.

c) Rethink the appropriate metric for this task, and ask your team to tune to the new metric. 

d) Pick false negative rate as the new metric, and use this new metric to drive all further development. 

> b) & c)

### 14

You’ve handily beaten your competitor, and your system is now deployed in Peacetopia and is protecting the citizens from birds! But over the last few months, a new species of bird has been slowly migrating into the area, so the performance of your system slowly degrades because your data is being tested on a new type of data.

You have only $1,000$ images of the new species of bird. the city expects a better system from you within the next 3 months. Which of these should you do first?

a) Use the data you have to define a new evaluation metric (using a new dev/test set) taking into account the new species, and use that to drive further progress for your team. 

b) Put the $1,000$ images into the training set so as to try to do better on these birds.

c) Try data augmentation/data synthesis to get more images of the new type of bird.

d) Add the $1,000$ images into your dataset and reshuffle into a new train/dev/test split.

> c)

## 15

the City Council thinks that having more Cats in the city would help scare off birds. they are so happy with your work on the Bird detector that they also hire you to build a Cat detector. (Wow Cat detectors are just incredibly useful aren’t they.) Because of years of working on Cat detectors, you have such a huge dataset of $100,000,000$ cat images that training on this data takes about two weeks. 

Which of the statements do you agree with?  (Check all that agree.) 

a) If $100,000,000$ examples is enough to build a good enough Cat detector, you might be better of training with just $10,000,000$ examples to gain a $\approx 10 \times$ improvement in how quickly you can run experiments, even if each model performs a bit worse because it’s trained on less data.

b) Having built a good Bird detector, you should be able to take the same model and hyperparameters and just apply it to the Cat dataset, so there is no need to iterate. 

c) Needing two weeks to train will limit the speed at which you can iterate.

d) Buying faster computers could speed up your teams’ iteration speed and thus your team’s productivity.    

> a) & c) & d)