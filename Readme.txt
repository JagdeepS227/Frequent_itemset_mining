						README


For running Apriori Algorithm: go to directory cs524_ass1 , enter command "python apriori.py" make sure all the datasets
are available in same directory. On starting of program you will see options for selecting different datasets after that you will
be asked for min support value , that must be between 0 to 1 (both excluded). On completion of program all freq itemsets will be displayed
with other information like total time taken and number of frequent itemsets generated.
Similarily for running FP growth algorithm enter command "python fbg.py" and rest is similar to apriori algorithm's execution.
For Eclat algorithm enter "python Eclat_g.py" and rest is similar to apriori algorithm.

For generating dataset enter command "python gen_data.py", it will ask for number of transaction, average width of transaction and upper limit
for value of items(number). It will create a dataset named as "dataset". If it already exists it will overwrite it. For using this dataset in any
algorithm select this as 6th option.
Be patient for apriori algorithm it might take long time for small min support value. :)