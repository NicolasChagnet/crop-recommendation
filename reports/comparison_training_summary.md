# Mean results per algorithm
| name               |   fit_time |   score_time |   test_score |   train_score |
|:-------------------|-----------:|-------------:|-------------:|--------------:|
| RandomForest       | 0.180784   |   0.0152511  |     0.999982 |      1        |
| NaiveBayesGaussian | 0.00245142 |   0.0112256  |     0.999937 |      0.999957 |
| DecisionTree       | 0.00614009 |   0.00991092 |     0.992534 |      1        |
| Dummy              | 0.00056591 |   0.00925832 |     0.5      |      0.5      |

# Iterations
|    |    fit_time |   score_time |   test_score |   train_score | name               | metric               |
|---:|------------:|-------------:|-------------:|--------------:|:-------------------|:---------------------|
|  0 | 0.00066638  |   0.00962234 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  1 | 0.000560045 |   0.00964904 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  2 | 0.00053978  |   0.00897813 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  3 | 0.00053215  |   0.00898361 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  4 | 0.000531197 |   0.00905848 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  0 | 0.0060091   |   0.00973082 |     0.989343 |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  1 | 0.00540113  |   0.00962996 |     0.99287  |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  2 | 0.00565171  |   0.00978494 |     0.992901 |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  3 | 0.00638843  |   0.00968552 |     0.989355 |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  4 | 0.00725007  |   0.0107234  |     0.998201 |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  0 | 0.180931    |   0.0151861  |     0.999982 |      1        | RandomForest       | roc_auc_ovr_weighted |
|  1 | 0.177612    |   0.0148911  |     0.999952 |      1        | RandomForest       | roc_auc_ovr_weighted |
|  2 | 0.180544    |   0.0151596  |     0.999976 |      1        | RandomForest       | roc_auc_ovr_weighted |
|  3 | 0.179871    |   0.0149388  |     1        |      1        | RandomForest       | roc_auc_ovr_weighted |
|  4 | 0.184962    |   0.0160797  |     1        |      1        | RandomForest       | roc_auc_ovr_weighted |
|  0 | 0.00259185  |   0.0115287  |     0.999855 |      0.99997  | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  1 | 0.00241446  |   0.0111444  |     0.999928 |      0.999961 | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  2 | 0.00240588  |   0.0112481  |     0.999928 |      0.999964 | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  3 | 0.00242925  |   0.0111651  |     1        |      0.999945 | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  4 | 0.00241566  |   0.0110416  |     0.999976 |      0.999947 | NaiveBayesGaussian | roc_auc_ovr_weighted |
