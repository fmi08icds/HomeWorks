# Home work 5

Ralf König, 12.05.2023

## 1. Problem Statement

a) True

Reason: 

Advice "8 Establish a single-number evaluation metric for your team to optimize"

Page 20: "If you really care about [multiple metrics], I recommend using one of the standard ways to combine them into a single number."

Page 21: "Having a single-number evaluation metric speeds up your ability to make a decision when you are selecting among a large number of classifiers. It gives a clear preference ranking among all of them, and therefore a clear direction for progress."

"Taking an average or weighted average is one of the most common ways to 
combine multiple metrics into one."

Mix of:
* accuracy => between 0 an 100 percent
* classification runtime per image => e.g. in seconds
* memory footprint => e.g. in MB

Hard due to different scales and units.

## 2. 

d)

Relates to page 22: "9 Optimizing and satisficing metrics"

Optimizing metrics:
	Accuracy.

Satisficing metrics: 
	classification runtime per image
	memory footprint

* 97% *, 1 sec ***, 3 MB **  <-- low accuracy
* 97% *, 3 sec **, 2 MB ***  <-- low accuracy
* 98% ***, 9 sec *, 9 MB *   <-- PICK THIS ONE!
* 99% ***, 13 sec, 9 MB ==> 13 seconds is over 10 seconds, out.

## 3. 

a)

See 2.

## 4. Structuring your data

10,000,000 images

Accuracy in the range of 97, 98, 99%.
We need to differentiate 1% oder 0,1% Accuracy.

Page 19: "7 How large do the dev/test sets need to be?"

Train/Dev/Test Set Size
9.500.000, 250.000, 250.000 <== PICK THIS ONE

On 250.000 images, 1% (2000) and 0,1% (250) are easy to make a difference.

"How about the size of the test set? It should be large enough to give high confidence in the overall performance of your system. One popular heuristic had been to use 30% of your data for your test set. This works well when you have a modest number of examples—say 100 to 10,000 examples. But in the era of big data where we now have machine learning problems 
with sometimes more than a billion examples, the fraction of data allocated to dev/test sets has been shrinking, even as the absolute number of examples in the dev/test sets has been growing. There is no need to have excessively large dev/test sets beyond what is needed to evaluate the performance of your algorithms."

## 5. 

* Further 1 Mio labeled images from citizens
* different from the distribution of the City Council

**Question:** "You should not add the citizens’ data to the training set, because this will cause the training and 
dev/test set distributions to become different, thus hurting dev and test set performance. True/False?"

b) FALSE

In the end, accuracy on the  City Council images counts.

The citizen images in the training set will **not** cause the dev and test set distributions to become different.

They may however improve or degrade the training.

Page 17
"6 Your dev and test sets should come from the same distribution"
=> is fulfilled. Dev and Test are on City Coucil images.

"12 Takeaways: Setting up development and test sets "

Choose dev and test sets from a distribution that reflects what data you expect to get in 
the future and want to do well on. This may not be the same as your training data’s 
distribution.  ==> FULFILLED

Choose dev and test sets from the same distribution if possible. ==> FULFILLED

## 6. 

a) The test set no longer reflects the distribution of data (security cameras) you most care about.
=> CORRECT. 250.000 von Security Cameras des City Council, und 1.000.000 von Bürgern.
Das verstößt gegen: "Choose dev and test sets from a distribution that reflects what data you expect to get in the future and want to do well on."
Man will in Zukunft gegen Bilder von Security Cameras gut sein, nicht auf Bürgerbildern, deren Verteilung davon abweicht.

b) A bigger test set will slow down the speed of iterating because of the computational expense of evaluating models on the test set.
=> WRONG. Das Test set wird in den iterations nicht verwendet. Sondern nur das Dev Set.

c) The citizens’ data images do not have a consistent mapping as the rest of the data.
=> MAY BE / UNDECIDABLE. Es ist keine Aussage zur consistency des Mappings der Bürgerbilder oder City Council Bilder in 
der 
Aufgabenstellung enthalten.

d) This would cause the dev and test set distributions to become different. This is a bad idea because you’re not aiming where you want to hit.
=> CORRECT, weil "These images (citizens' data) are different from the distribution of images the City Council had 
originally given you".

## 7. 

training set error: 4%
dev set error: 4.5%

Page 42: "Your dev/test set performance is usually worse than your training set performance."

informal estimations: (see Page 42)
* bias: 4%
* variance: 0,5%   (dev set error minus training set error)

"This suggests that one good avenue for improving performance is to train a bigger network so as to drive down the 4.0% training error. Do you agree?"

=> this bigger network will have less bias, but more variance

What is missing: => Comparison with Human Performance, which have labeled the images in the training set, 
Dev set, Test set.

Page 42: "20 Bias and Variance: The two big sources of error "
Page 44: "21 Examples of Bias and Variance"

a) Yes, because having 4.0% training error shows you have high bias.
=> No way to tell, if 4% avoidable bias or not.

b) Yes, because this shows your bias is higher than your variance.
=> CORRECT. 4% is much higher than 0,5%.  Modell is undercomplex (underfitting). 
It could get more complex to better adapt to the data.

c) No, because this shows your variance is higher than your bias.
=> WRONG.

d) No, because there is insufficient information to tell.
=> CORRECT. Lack of Comparison with Human Performance.

## 8. 

"34 How to define human-level performance  "
Page 68

Dort auch ein Beispiel. Bestes menschliches Ergebnis (Gruppe von Doktoren) wurde genommen.

a) 0,0% (because it is impossible to do better than this)
=> WRONG

b) 0,3%  (accuracy of expert #1)
=> CORRECT. Choose best expert.

c) 0,4% (average of 0.3 and 0.5 %)
=> WRONG. Experts of varying qualification, experience, concentration or motivation.

d) 0,75% (average of all four numbers above)
=> WRONG


## 9. 

"22 Comparing to the optimal error rate "
Page 46

"35 Surpassing human-level performance"
Page 69


Which of the following statements do you agree with?

a) A learning algorithm’s performance 
OK	can be better than human-level performance but it 
OK	can never be better than Bayes error.
=> CORRECT.

b) A learning algorithm’s performance 
X	can never be better than human-level performance but it 
X	can be better than Bayes error.
=> WRONG.

c) A learning algorithm’s performance 
X	can never be better than human-level performance 
OK	nor better than Bayes error.
=> WRONG.

d) A learning algorithm’s performance 
OK	can be better than human-level performance 
X	and better than Bayes error.
=> WRONG.

## 10. 

"22 Comparing to the optimal error rate"

You find that a team of ornithologists debating and discussing an image gets an even better 0.1% performance, so you define that as “human-level performance.” After working further on your algorithm, you end up with the following:

* Human-level performance 0.1% , 
* Training set error 2.0% , 
* Dev set error 2.1%

Bias = 2% = 0.1% unavoidable (Human Level) + 1.9% avoidable bias
Variance = 0.1%

Based on the evidence you have, which two of the following four options seem the most promising to try? (Check two options.)

a) Get a bigger training set to reduce variance.
=> WRONG.  Variance is already low.

b) Try increasing regularization.
=> WRONG. Would further constrain the model.

c) Train a bigger model to try to do better on the training set.
=> CORRECT.

d) Try decreasing regularization.
=> CORRECT. More Freedom to the model to better adapt and get bias down.

## 11. 

You also evaluate your model on the test set, and find the following:

* Human-level performance	0,1%
* Training set error	2,0%
* Dev set error		2,1%
* Test set error		7,0%


What does this mean? (Check the two best options.)

a) You should get a bigger *test* set.
=> WRONG.

b) You should try to get a bigger *dev* set.
=> CORRRECT.

c) You have underfit to the *dev* set.
=> WRONG.

d) You have overfit to the *dev* set.
=> CORRECT.


## 12. 

After working on this project for a year, you finally achieve: 

* Human-level performance 0.10% (group of onthologists)
* Training set error 0.05%
* Dev set error 0.05%

What can you conclude? (Check all that apply.)

a) With only 0.09% further progress to make, you should quickly be able to close the remaining gap to 0%.
=> WRONG.

b) If the test set is big enough for the 0.05% error estimate to be accurate, this implies Bayes error is <=0.05%.
=> IF big enough and Accuracy reliable: CORRECT.

c) This is a statistical anomaly (or must be the result of statistical noise) since it should not be possible to surpass human-level performance.
=> WRONG.

d) It is now harder to measure avoidable bias, thus progress will be slower going forward.
=> CORRECT.


## 13. 

It turns out Peacetopia has hired one of your competitors to build a system as well. Your system and your competitor both deliver systems with about the same running time and memory size. However, your system has higher accuracy! However, when Peacetopia tries out your and your competitor’s systems, they conclude they actually like your competitor’s system better, because even though you have higher overall accuracy, you have more false negatives (failing to raise an alarm when a bird is in the air).

What should you do?

a) Look at all the models you’ve developed during the development process and find the one with the lowest false negative error rate.
=> WRONG. Only a one-time consideration. But what is actually needed, is a new improvement loop towards new objective.

b) Ask your team to take into account both accuracy and false negative rate during development.
=> WRONG. Two Metrics. That makes it hard, Better use one metric.

c) Rethink the appropriate metric for this task, and ask your team to tune to the new metric.
=> CORRECT. Find new metric that combines "False Negatives" and "Accuracy".

d) Pick false negative rate as the new metric, and use this new metric to drive all further development.
=> Would be single-objective on the new metric like FN. This is not what is need, but a combined metric.

## 14. 

You’ve handily beaten your competitor, and your system is now deployed in Peacetopia and is protecting the citizens from birds! But over the last few months, a new species of bird has been slowly migrating into the area, so the performance of your system slowly degrades because your data is being tested on a new type of data.

You have only 1000 images of the new species of bird. The city expects a better system from you within the next 3 months. Which of these should you do first?

a) Use the data you have to define a new evaluation metric (using a new dev/test set) taking into account the new species (images), and use that to drive further progress for your team.
=> CORRECT, die neue Art muss unbedingt in DEV und TEST rein. Nur dann entwickelt man auch gegen diesen reale Fall.
Vielleicht erkennt der aktuelle Ansatz das ja schon ganz gut?
Tauben sind ja sehr ähnlich wie andere Vögel.

b) Put the 1000 images into the training set so as to try to do better on these birds.
=> WRONG. Dann würde man ja auf allen trainieren. Aber nicht drauf validieren oder testen.

c) Try data augmentation/data synthesis to get more images of the new type of bird.
=> COULD BE USEFUL, as 1000 images are really very few in comparison to other
bird species.

d) Add the 1000 images into your dataset and reshuffle into a new train/dev/test split.
=> COULD BE USEFUL. But 1000 images is already low. 

## 15. 

The City Council thinks that having more Cats in the city would help scare off birds. They are so happy with your work on the Bird detector that they also hire you to build a Cat detector. (Wow Cat detectors are just incredibly useful aren’t they.) Because of years of working on Cat detectors, you have such a huge dataset of 100,000,000 cat images that training on this data takes about two weeks.

Which of the statements do you agree with? (Check all that agree.)

a) If 100 Mio examples is enough to build a good enough Cat detector, you might be better of training with just 10 Mio examples to gain a 10x improvement in how quickly you can run experiments, even if each model performs a bit worse because it’s trained on less data.
=> CORRECT

b) Having built a good Bird detector, you should be able to take the same model and hyperparameters and just apply it to the Cat dataset, so there is no need to iterate.
=> WRONG

c) Needing two weeks to train will limit the speed at which you can iterate.
=> CORRECT

d) Buying faster computers could speed up your teams’ iteration speed and thus your team’s productivity.
=> CAN BE DONE, DOES NOT HAVE TO. Is an expensive, likely unclever way to deal with the problem.
