## 1
   True. Having multiple evaluation metrics means that you have to weigh them up. Instead, you should either focus on one, make a new metric which is the combination of the other ones or formulate goals as constraints.

## 2
   d. The goal is to maximise the accuracy while complying with the conditions of taking max 10 seconds and having a memory size of max 10MB. d fulfills the conditions and has a higher accuracy than a and c.

## 3
   a. As described in 2.

## 4
   b. 250,000 samples in a dev set is plenty. In this case a 60/20/20 split isn't necessary anymore.

## 5 
   False. Training set can be different to the dev/test set. The dev set, however, should come from the same distribution as the test set.

## 6 
   d. As previously mentioned. 

## 7 
   b. 4% is the bias and can sometimes be reduced by increasing the model size. 4% doesn't seem that high to me but it's higher than the variance of .5%

## 8 
   c. The human-level performance is defined as how good a human can be and not how good the average human is. Therefore, I value the opinion of experts higher. I'd take the average of the experts though as without further information I value the opinion of the experts equally and I don't know what the reason for the discrepancy is. E.g. it could be that expert two had more difficult cases or expert 1 "guessed" on some. 

## 9 
   a. Bayes error is the optimal error rate or also the unavoidable bias. 

## 10
   c. The bias is much higher than the variance and training a bigger model is a method to reduce it.
	Increasing the regularisation and getting a bigger training set are methods to reduce the variance and are therefore false.

## 11
   d., b.  The model specialised in evaluating the samples it got. Because of that it is overfit to the dev set and performs worse when evaluating unknown data (test set). Methods to counter this are to use a fresh dev or to use a bigger dev set.  

## 12
   b., d. While the human error rate is chosen because it is close to the Bayes error rate, it is still possible to beat it. It is however not possible to be consistently better than Bayes error rate which means that it is max .05. Avoidable bias is the difference between the optimal bias and the training error. As the training error is already lower than what we assumed to be the optimal error rate, we don't exactly know what the avoidable bias is and process will be slower.

## 13
   c. As initially mentioned it's better to have one metric instead of looking at multiple and it's fine to develop your own metric that is a combination of the other metrics. Although not stated explictly I assume that accuracy still plays an important role and shouldn't be dismissed entirely. 

## 14
   a. The dev/ test set should always be representative of the real world application. Because of this it is vital that images of the new species are included in the dev/test set. Reshuffling would mean that most of the samples in the dev/test set are still not of the new species and therefore not representative. Instead, a good chunk (like half of the new images or perhaps even all 1000 images) should be in the new dev/test set. Not sure if a new evaluation metric is necessary but I suppose it could make sense to weight images with the new species more as they are more present and thus more relevant for the system. 

## 15
   a., c., d. Smaller data sets will lead to faster training times and as per the training curve the improvements of the model get smaller and smaller the bigger the training set becomes and it's most likely other adjustments will have a far greater impact. The bird detector is specifically trained to detect birds and can't be altered to detect cats instead. The time constraint of two weeks means that you either have to limit the speed of one iteration or the number of iterations. So you have to discard certain approaches earlier and limit what you are going to attempt. Faster computers will increase the computational speed. Nevertheless, computational resources are not the only or even the most important factors for the iteration speed. Having the right organisation (e.g. using dev and test sets) will lead to a more efficient process. 
