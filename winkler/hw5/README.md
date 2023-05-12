# Homework 5

This `README` contains the answers to the questions form this [notebook](https://github.com/fmi08icds/Coding/blob/main/notebooks/day5.ipynb).

- **Question 1:** a
- **Question 2:** d
- **Question 3:** a
- **Question 4:** b
  Remark: A "traditional" heuristic is to pick 30 % of the available data for the test/dev set. However, dev/test sets commonly contain about 1000 to 10000 samples which is sufficient for evaluating algorithms and performing error analysis. So 250,000 samples are enough for both sets.
- **Question 5:** b 
- **Question 6:** d
- **Question 7:** d<br>
  Remark: The human-level error is unknown so the bias can't be determined.
- **Question 8:** b (or c)<br>
  Remark: In an optimal scenario we should take the performance of the best expert as the human-level error. Since expert 1 achieved the best result, we can accept 0.3 %. However, we can't tell how these results were determined, so it could be possible that expert 1 was "just lucky" compared to expert 2. A more conservative approach would be to use an average of both experts, i. e., setting the human-level performance to 0.4 %.
- **Question 9:** a
- **Question 10:** c
- **Question 11:** b, d
- **Question 12:** b, d<br>
  Remark: If the test set is big enough, we can conclude that the upper bound of the Bayes error rate is 0.05 % since the Bayes error rate can't be higher than the models error rate. Also, it is harder to measure the avoidable bias because the human-level performance is worse than the model's error rate.
- **Question 13:** c<br>
  Remark: It is important to only consider one metric. However, optimizing for the false-negative rate alone is not good, because it will most likely lead to many false positives, i. e., detecting birds eventhough there are none.
- **Question 14:** a
- **Question 15:** a, c, d