# What is Ditlevsen range?

when calculating the reliability of a system, it is easy to calculate reliability of each component, but
it is not easy to calculate the overall reliability. Hence, we simply calculate a range for the proabability 
of failure. In cases when the correlation is bi-modal rather than uni-modal, using Ditlevsen range is more
prominent.

## The lower bound

The following is the formula for calculating the lower bound, consider that P(E1) is the highest probability.

$$P(E_1) + \sum_{i=2}^k \max \left( P(E_i) - \sum_{j=1}^{i-1} P(E_i \cap E_j), \; 0 \right)$$

## The upper bound

The following is the formula for the upper bound of Ditlevsen method

$$\sum_{i=1}^k P(E_i) - \sum_{i=2}^k \max_{j < i} P(E_i \cap E_j)$$

the python file is also placed in this folder.

