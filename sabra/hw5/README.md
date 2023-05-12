# Answers: 

####  1) Yes 
An algorithum with high accuracy might not be able to run efficiently on a small processor due to 
memory limitations and slow performance. On the other hand, a less accurate algorithum could be better suited for 
running on a small processor , because it is faster and requires less memory, therefore it is very challenging to find a balance between the obsorved metrices and optimize the model for it. It is very important that the team that is working on the problem to prioritze a specific metric and optimize the model for it , while considering other metrices as secondary factors and this approach allows for a faster iteration and decision making.




####  2) Model A  
 Despite the higher accuracy of the second model B, compared to the first model A , it takes longer to 
       run and exceeds the maximum runtime limit specified in the requirements. 
       Although model A has a memory size that is 1 MB larger than that of Model c, it runs 2 seconds faster than model C.
       Additionally , model D has slightly higher accuracy than model A by 1% , but it runs slower than model A . Therefore , 
       model A is ultimately chosen as it runs the fastest and the difference in accuracy compared to the other models is
       not significant. 
       
       
  
####  3) A (Accuracy is an optimizing metric; running time and memory size are a satisficing metrics)
 Based on the city’s requests , it is evident that they have requested an algorithum with a very high 
       accuracy. However , the city has not explicitly specified a requirement for very high run time or very low memory 
       size. Rather, they have set specific thresholds that must be met. This can be interpreted as the city prioritizing the 
       accuracy metric over the other two metrics. 
       
       
       
####  4) D (Train/Dev/Test = 6,000,000/3,000,000/1,000,000)
Typically , a ratio of 60/20/20 is used for the tain/dev/test sets . Therefore , option D appears to be the 
       most suitable choice as it adheres to this ratio and provides a significant amount of data for training and testing the 
       algorithum . Option A is not practical because it allocates more data for testing the algorithm. Option A is not 
       practical because it allocates more data for testing than for dev , which is insufficient for tuning the algorithum. 



####  5) Yes 
The reason for not adding the citizens’ data to the training set is because the distribution of this new 
       data is different from the original data , as stated in the question . if the new data is added to the training set , it may
       casue the algorithum to become biased towards the citizens’ data , leading to poor performance on the dev and 
       testing data 
       
       
####  6) A(The test set no longer reflects the distribution of data of (secrity cameras) you most care about)       

The original training data consists of security camera images , and including the citizens’ data  
       in the test set would alter the distribution and reduce its representativness. This is problematic since the test set 
       should reflect the actual data that the model will encounter in production, which in this case is the distribution of 
       security camera images. 
       
       
####  7) No , because there is insufficient inforamtion to tell.


####  8)  D (the average of all four numbers given)
 if the goal is to have "human-level-performance“ be a proxy for bayes error , then „human-level-
       performance“ can be defined as the average accuracy of the two bird watching experts and the two normal persons
       
      
####  9)  (A learning algorithm’s performance can be better than human-level performance and better than Bayes error)
in some instances , "human-level performance „
       can serve as a subtitute for Bayes error since humans are often believed to excel at tasks that machines struggle with.
       However ,there  are scenarios , where machines can surpass human performance. Hence , it’s feasible for a learning alogrithum to outperform both 
       Human-level performance and Bayes error. 
       
       

####  10)  (a) and (c)


####  11)  (b) and (d)
Trying a bigger dev set can be a promising solution , as the model is too specialized to the dev set and 
       not generalizing to new data , which means that the model is overfitted to the dev set 
       
####  12)  (b) and (d)


####  13)  (b) 
While high accuracy (TP) is crucial , it’s equally essential to consider false negatives as a significant metric during
        the model development process 


####  14)  (c) 


####  15)  (a) and (c)

