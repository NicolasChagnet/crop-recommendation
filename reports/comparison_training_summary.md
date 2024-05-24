# Mean results per algorithm
| name               |    fit_time |   score_time |   test_score |   train_score |
|:-------------------|------------:|-------------:|-------------:|--------------:|
| RandomForest       | 0.197909    |   0.0171672  |     0.999971 |      1        |
| NaiveBayesGaussian | 0.00368543  |   0.0137006  |     0.999937 |      0.999957 |
| DecisionTree       | 0.00582471  |   0.00901918 |     0.991475 |      1        |
| Dummy              | 0.000681543 |   0.00869675 |     0.5      |      0.5      |

# Iterations
|    |    fit_time |   score_time |   test_score |   train_score | name               | metric               |
|---:|------------:|-------------:|-------------:|--------------:|:-------------------|:---------------------|
|  0 | 0.000648975 |   0.00933385 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  1 | 0.000864506 |   0.0087781  |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  2 | 0.000766277 |   0.00889111 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  3 | 0.0006001   |   0.00824523 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  4 | 0.000527859 |   0.00823545 |     0.5      |      0.5      | Dummy              | roc_auc_ovr_weighted |
|  0 | 0.00595069  |   0.00925183 |     0.992901 |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  1 | 0.00574565  |   0.00950933 |     0.99287  |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  2 | 0.00583148  |   0.00885653 |     0.985803 |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  3 | 0.00613666  |   0.00873971 |     0.985803 |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  4 | 0.00545907  |   0.00873852 |     1        |      1        | DecisionTree       | roc_auc_ovr_weighted |
|  0 | 0.181288    |   0.0143037  |     0.999988 |      1        | RandomForest       | roc_auc_ovr_weighted |
|  1 | 0.20527     |   0.0190055  |     0.99988  |      1        | RandomForest       | roc_auc_ovr_weighted |
|  2 | 0.183202    |   0.0139043  |     0.999988 |      1        | RandomForest       | roc_auc_ovr_weighted |
|  3 | 0.186867    |   0.0194833  |     1        |      1        | RandomForest       | roc_auc_ovr_weighted |
|  4 | 0.232916    |   0.0191391  |     1        |      1        | RandomForest       | roc_auc_ovr_weighted |
|  0 | 0.00327563  |   0.0133879  |     0.999855 |      0.99997  | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  1 | 0.00280261  |   0.0136859  |     0.999928 |      0.999961 | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  2 | 0.00399041  |   0.0143161  |     0.999928 |      0.999964 | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  3 | 0.00387073  |   0.013875   |     1        |      0.999945 | NaiveBayesGaussian | roc_auc_ovr_weighted |
|  4 | 0.00448775  |   0.0132382  |     0.999976 |      0.999947 | NaiveBayesGaussian | roc_auc_ovr_weighted |
