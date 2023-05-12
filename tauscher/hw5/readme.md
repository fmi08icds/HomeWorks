## Homework 5

1. Problem Statement

You are a famous researcher in the City of Leipzig. The tourists have a common characteristic: they are afraid of birds. To save them, you have to build an algorithm that will detect any bird flying over Peacetopia and alert the population.


a) What is the evaluation metric?

Since saving the Birds is of main concern, we should use a metric that emphesis on detecting a bird as often as possible. We don't care about the false positives, since they will not harm the birds. Recall does exactly that by measuring the ratio of true positives to all actual positives. (tp/(tp+fn))

b) How do you structure your data into train/dev/test sets?

Given the information that we have 10_000_000 images of the sky above Leipzig we do not know yet how many of the pictures actually have birds in them. If it is only a small subset of 1_000 images there is a high chance of not being able to learn the bird-occurence-pattern from the input signal. Therefore we should explore the data first and then make a informed decision of partitioning the data into train/dev and test sets. 

c) "Has high accuracy" - we should rather convince the city council that we do not want accuracy as it does not depict what we actually want to measure. Imagen there are actually 1_000 images containing birds. By default (with no model whatsoever) predicting "no" in a binary classification would lead to a accuracy of 99.99 %.  

"Runs quickly and takes only a short time to classify a new image."

"Can fit in a small amount of memory, so that it can run in a small processor that the city will attach to many different security cameras."


### Question: Having three evaluation metrics makes it harder for you to quickly choose between two different algorithms, and will slow down the speed with which your team can iterate. 
#### Answer: True. The more complex a evaluation approach the more time is going to be spent on details. But still one needs to be thoughtful of chosing the right evaluation metric.

2. Model Selection

d) as it is within the specified criteria from the city council. But there is a strong argument for iterating on approach a) since it is much faster and smaller, and therefore can be improved upon by using, e.g., another essemble method that is also within the specified criteria, whereas d) is already at 'its limits'.


3. Metric Formulation/Combination
a) Accuracy is an optimizing metric('need'); running time and memory size are a satisficing metrics('want').

4. Structuring Data

Hard to say since I don't know anything about the pictures. But since the amount of data is quite large I would start with (b), the 95/2.5/2.5 split. If the data is enough I would increase the size of the test set. The larger the test set the more confident I can be about the generalization of the model. 

5. Data Enrichment

The 1_000_000 new pictures can be used as a blindtest dataset, that was never used in the training process at all, is not a sample from the same distribuion and therefore can be used to estimate the generalization error of the model. It not going to hurt the performance of the model if the training set would get bigger but the model would probably lose generalization power. So the answer is "True, with regards to generalization and robustness".

6. Objecting the City Council

both Argument a) and c) are solid arguments. 

7. Adressing Bias

There is not enough information. We don't know what the baseline is, and we don't know what exactly the ~4-5% missclassified pictures look like. Are they labelled wrong, are they blurry.. 4% Error is a respectable model performance and performing just 0.5% worse on the dev/test set is not a huge difference. The mode is not underfitting and the variance seems to be low. So I would say that the model is doing a good job. 

8. Human-Level-Performance

To get an idea about what the baseline for the model should be, we can assume that we want it to be better or as good as experts in the field. Since we have 2 Bird-Experts with 0.3% Error and 0.5% Error, we should average their performance to get a good idea about a human-level-baseline, c) = 0.4 .

9. Statements

I agree with a), since the Bayes-Error-Rate is the lowest possible error-rate.

10. a), c) . Regularization only helps to reduce the variance of the model. It does not help to reduce the bias. 

11. d), b) . I should try to get a bigger dev set. The bigger the dev set the more confident I can be about the generalization error of the model and the more the dev error and test error align, the closer I am to the optimal model and set-partitioning.

12. 

d) It is now harder to measure avoidable bias, thus progress will be slower going forward.
b) since the model performance cant be better than the bayes error. 

13. c) Rethink the appropriate metric for this task, and ask your team to tune to the new metric.

14. c) 

15. a), c), somewhat b) [transfare learning, similar problem, similar data, similar approach], finally d) is also not incorrect. Faster computers may lead to more productiviy or the other way arround working with slow and old technology might demotivate and slow the team down.







