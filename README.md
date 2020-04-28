Project Details:

In this project, you are going to implement and experiment with several algorithms for Maximum 0-1
Knapsack and SAT. In particular, you must implement the following:

1. The O(nW) dynamic programming algorithm that we discussed in CS305.
2. The O(n·v(amax)) dynamic programming algorithm from the textbook based on the MinCost version
of the problem.
3. The greedy 2-approximation from the textbook.
4. The FPTAS based on scaling with the optimal dynamic programming algorithm from (2) above.
5. The DPLL algorithm.
6. GSAT
7. The simple randomized 7/8 approximation algorithm for MAX3SAT.

After implementing the algorithms, run the following experiments:

1. Generate 100 large random instances of Maximum Knapsack and compare the results of each the
Knapsack algorithms above on these instances.
2. Generate 100 large random instances of 3SAT and compare the results of DPLL, GSAT and randomized
MAX3SAT on these instances.

Include in your emailed submission:

• your code as a zipped attachment, written in the language of your choice.

• a report (as a pdf) that provides details of your experiments including the average, median, minimum
and maximum quality of the solutions returned for Maximum Knapsack and 3SAT as well as the
average, median, minimum, and maximum running times for both the Maximum Knapsack instances
and the 3SAT instances. This report should be well written, with an introduction and conclusion.
