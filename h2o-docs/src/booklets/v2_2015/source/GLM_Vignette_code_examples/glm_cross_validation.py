import h2o
from h2o.estimators.glm import H2OGeneralizedLinearEstimator
h2o.init()
path = h2o.system_file("prostate.csv")
h2o_df = h2o.import_file(path)
h2o_df['CAPSULE'] = h2o_df['CAPSULE'].asfactor()
binomial_fit = H2OGeneralizedLinearEstimator(family = "binomial", nfolds=5, fold_assignment="Random")
binomial_fit.train(y = "CAPSULE", x = ["AGE", "RACE", "PSA", "GLEASON"], training_frame = h2o_df)
print "training auc: " + str(binomial_fit.auc(train=True))
print "cross-validation auc: " + str(binomial_fit.auc(xval=True))
