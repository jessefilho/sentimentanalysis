# REPORT OF SENTIMENT ANALYSIS

	Students: 
		FERREIRA, Jesse.
		TALBI, Samir.

	More details on github: https://github.com/jessefilho/sentimentanalysis


## STEP 1 - Term Frequencies:
	To study the effect of weighting factor in sentiment classifications, we choose to do the ratio of the term by POS. The results are presented at results section.
	- trim each document in trainning corpus (pos and neg) removing all stop words and non-alphanumeric words. The out result files will be to new directories
	- trim train folder:	
		called:
		pos-words: train/pos-words/
		neg-words: train/neg-words/
    - trim test folder:
		pos-words: test/pos-words/
		neg-words: test/neg-words/
	- create folders into corpus/:
		for trainning:
			$ mkdir train/pos-words/
			$ mkdir train/neg-words/
		for test too:
			$ mkdir test/pos-words/ test/neg-words/
	- then to trim, execute the follow command (program python 2.7):
		- do chmod 745 for the file trim.py, then run:
			$ sudo chmod 745 trim.py
		- execute the trim.py:
			- for train dataset:
				- for pos-words:
					$ for f in train/pos/*.txt; do python2.7 ../ressources/scripts/trim.py ../ressources/stopwords.txt <$f >train/pos-words/`basename $f`; done
				- for neg-words:
					$ for f in train/neg/*.txt; do python2.7 ../ressources/scripts/trim.py ../ressources/stopwords.txt <$f >train/neg-words/`basename $f`; done
			- for test dataset:
				- for pos-words:
					$ for f in test/pos/*.txt; do python2.7 ../ressources/scripts/trim.py ../ressources/stopwords.txt <$f >test/pos-words/`basename $f`; done
				- for neg-words:
					$ for f in test/neg/*.txt; do python2.7 ../ressources/scripts/trim.py ../ressources/stopwords.txt <$f >test/neg-words/`basename $f`; done
			- Combine the two classes (pos and neg) of trimmed training corpus to two individual files:
				- for train:
					train/pos-words.txt
					train/neg-words.txt
					$ cat train/pos-words/*.txt >train/pos-words.txt
					$ cat train/neg-words/*.txt >train/neg-words.txt
				- for test:
					test/pos-words.txt
					test/neg-words.txt
				- Combination :
					$ cat test/pos-words/*.txt >test/pos-words.txt
					$ cat test/neg-words/*.txt >test/neg-words.txt
		    - Create the vocabular, using the third(0.45) and fourth(20)
				parameters to regulate the quantity of terms :
				$ python2.7 ../ressources/scripts/vocab.py train/pos-words.txt train/neg-words.txt 0.45 15 > train/v-tagged.txt
		- Get term's frenquence:
			- for train, by ratio. For each term count if it is present, then divise by the total of terms:
				$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train/v-words.txt train/pos-words train/neg-words >train/train-trimmed.arff
			- for test, by ratio:
				$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train/v-words.txt test/pos-words test/neg-words >test/test-trimmed.arff
			
## LibLinear (TRAIN)

	=== Run information ===

	Scheme:       weka.classifiers.functions.LibLINEAR -S 1 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000
	Relation:     movie-review
	Instances:    1600
	Attributes:   9304
	              [list of attributes omitted]
	Test mode:    10-fold cross-validation

	=== Classifier model (full training set) ===

	LibLINEAR wrapper

	Model bias=1.0 nr_class=2 nr_feature=9304 solverType=L2R_L2LOSS_SVC_DUAL

	Time taken to build model: 0.62 seconds

	=== Stratified cross-validation ===
	=== Summary ===

	Correctly Classified Instances        1382               86.375  %
	Incorrectly Classified Instances       218               13.625  %
	Kappa statistic                          0.7275
	Mean absolute error                      0.1363
	Root mean squared error                  0.3691
	Relative absolute error                 27.25   %
	Root relative squared error             73.8241 %
	Total Number of Instances             1600     

	=== Detailed Accuracy By Class ===

	                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	                 0.876    0.149    0.855      0.876    0.865      0.728    0.864     0.811     pos
	                 0.851    0.124    0.873      0.851    0.862      0.728    0.864     0.818     neg
	Weighted Avg.    0.864    0.136    0.864      0.864    0.864      0.728    0.864     0.814     

	=== Confusion Matrix ===

	   a   b   <-- classified as
	 701  99 |   a = pos
	 119 681 |   b = neg
## LibLinear (TEST)

	Time taken to build model: 0.22 seconds

	=== Evaluation on test set ===

	Time taken to test model on supplied test set: 0.22 seconds

	=== Summary ===

	Correctly Classified Instances         175               87.5    %
	Incorrectly Classified Instances        25               12.5    %
	Kappa statistic                          0.75  
	Mean absolute error                      0.125 
	Root mean squared error                  0.3536
	Relative absolute error                 25      %
	Root relative squared error             70.7107 %
	Total Number of Instances              200     

	=== Detailed Accuracy By Class ===

	                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	                 0.880    0.130    0.871      0.880    0.876      0.750    0.875     0.827     pos
	                 0.870    0.120    0.879      0.870    0.874      0.750    0.875     0.830     neg
	Weighted Avg.    0.875    0.125    0.875      0.875    0.875      0.750    0.875     0.828     

	=== Confusion Matrix ===

	  a  b   <-- classified as
	 88 12 |  a = pos
	 13 87 |  b = neg				
## SVM SPegasos (TRAIN):
	=== Run information ===

	Scheme:       weka.classifiers.functions.SPegasos -F 0 -L 1.0E-4 -E 500
	Relation:     movie-review
	Instances:    1600
	Attributes:   9304
	              [list of attributes omitted]
	Test mode:    10-fold cross-validation

	=== Classifier model (full training set) ===

	Loss function: Hinge loss (SVM)
	Time taken to build model: 18.48 seconds

	=== Stratified cross-validation ===
	=== Summary ===

	Correctly Classified Instances        1414               88.375  %
	Incorrectly Classified Instances       186               11.625  %
	Kappa statistic                          0.7675
	Mean absolute error                      0.1163
	Root mean squared error                  0.341 
	Relative absolute error                 23.25   %
	Root relative squared error             68.1909 %
	Total Number of Instances             1600     

	=== Detailed Accuracy By Class ===

	                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	                 0.890    0.123    0.879      0.890    0.884      0.768    0.884     0.837     pos
	                 0.878    0.110    0.889      0.878    0.883      0.768    0.884     0.841     neg
	Weighted Avg.    0.884    0.116    0.884      0.884    0.884      0.768    0.884     0.839     

	=== Confusion Matrix ===

	   a   b   <-- classified as
	 712  88 |   a = pos
	  98 702 |   b = neg
## SVM SPegasos (TEST):
	=== Evaluation on test set ===

	Time taken to test model on supplied test set: 0.34 seconds

	=== Summary ===

	Correctly Classified Instances         176               88      %
	Incorrectly Classified Instances        24               12      %
	Kappa statistic                          0.76  
	Mean absolute error                      0.12  
	Root mean squared error                  0.3464
	Relative absolute error                 24      %
	Root relative squared error             69.282  %
	Total Number of Instances              200     

	=== Detailed Accuracy By Class ===

	             TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	             0.870    0.110    0.888      0.870    0.879      0.760    0.880     0.837     pos
	             0.890    0.130    0.873      0.890    0.881      0.760    0.880     0.832     neg
	Weighted Avg.    0.880    0.120    0.880      0.880    0.880      0.760    0.880     0.834     

	=== Confusion Matrix ===

	a  b   <-- classified as
	87 13 |  a = pos
	11 89 |  b = neg
## RandomForest (TRAIN):

		=== Run information ===

		Scheme:       weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1
		Relation:     movie-review
		Instances:    1600
		Attributes:   9304
		              [list of attributes omitted]
		Test mode:    10-fold cross-validation

		=== Classifier model (full training set) ===

		RandomForest

		Bagging with 100 iterations and base learner

		weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-check-capabilities

		Time taken to build model: 21.65 seconds

		=== Stratified cross-validation ===
		=== Summary ===

		Correctly Classified Instances        1307               81.6875 %
		Incorrectly Classified Instances       293               18.3125 %
		Kappa statistic                          0.6338
		Mean absolute error                      0.4251
		Root mean squared error                  0.4338
		Relative absolute error                 85.01   %
		Root relative squared error             86.7553 %
		Total Number of Instances             1600     

		=== Detailed Accuracy By Class ===

		                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
		                 0.786    0.153    0.838      0.786    0.811      0.635    0.891     0.891     pos
		                 0.848    0.214    0.799      0.848    0.822      0.635    0.891     0.873     neg
		Weighted Avg.    0.817    0.183    0.818      0.817    0.817      0.635    0.891     0.882     

		=== Confusion Matrix ===

		   a   b   <-- classified as
		 629 171 |   a = pos
		 122 678 |   b = neg
## RandomForest (TEST):
					Time taken to build model: 22.79 seconds

					=== Evaluation on test set ===

					Time taken to test model on supplied test set: 0.28 seconds

					=== Summary ===

					Correctly Classified Instances         141               70.5    %
					Incorrectly Classified Instances        59               29.5    %
					Kappa statistic                          0.41  
					Mean absolute error                      0.4424
					Root mean squared error                  0.4519
					Relative absolute error                 88.48   %
					Root relative squared error             90.375  %
					Total Number of Instances              200     

					=== Detailed Accuracy By Class ===

					                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
					                 0.950    0.540    0.638      0.950    0.763      0.470    0.875     0.872     pos
					                 0.460    0.050    0.902      0.460    0.609      0.470    0.875     0.861     neg
					Weighted Avg.    0.705    0.295    0.770      0.705    0.686      0.470    0.875     0.866     

					=== Confusion Matrix ===

					  a  b   <-- classified as
					 95  5 |  a = pos
					 54 46 |  b = neg


## STEP 2 - Term Frequencies (tagged):

					- create folders into corpus/:
							for trainning:
								$ mkdir train-tagged/pos-tagged train-tagged/neg-tagged
								
								
							for test too:
								$ mkdir test-tagged/neg-tagged test-tagged/pos-tagged

					- execute the trim-tagged.py:

						- for train dataset:
							- for pos-tagged:
								$ for f in train-tagged/pos/*.txt; do python2.7 ../ressources/scripts/trim-tagged2.py ../ressources/stopwords.txt <$f >train-tagged/pos-tagged/`basename $f`; done
							- for neg-tagged:
								$ for f in train-tagged/neg/*.txt; do python2.7 ../ressources/scripts/trim-tagged2.py ../ressources/stopwords.txt <$f >train-tagged/neg-tagged/`basename $f`; done

						- for test dataset:
							- for pos-tagged:
								$ for f in test-tagged/pos/*.txt; do python2.7 ../ressources/scripts/trim-tagged2.py ../ressources/stopwords.txt <$f >test-tagged/pos-tagged/`basename $f`; done
							- for neg-tagged:
								$ for f in test-tagged/neg/*.txt; do python2.7 ../ressources/scripts/trim-tagged2.py ../ressources/stopwords.txt <$f >test-tagged/neg-tagged/`basename $f`; done

					- Combine the two classes (train-tagged)
							$ cat train-tagged/pos-tagged/*.txt > train-tagged/pos-tagged.txt 
							$ cat train-tagged/neg-tagged/*.txt > train-tagged/neg-tagged.txt
							
					- Combine the two classes (test-tagged)
							$ cat test-tagged/pos-tagged/*.txt > test-tagged/pos-tagged.txt
							$ cat test-tagged/neg-tagged/*.txt > test-tagged/neg-tagged.txt


					- Generate the dictionary file that contains all vocabulary terms corresponding to the set of
					  all attributes appearing in the vector representation of documents.
					  		- 86% :
					  		$ python2.7 ../ressources/scripts/vocab.py train-tagged/pos-tagged.txt train-tagged/neg-tagged.txt 0.45 15 > train-tagged/v-tagged.txt

					  		$ python2.7 ../ressources/scripts/vocab.py train-tagged/pos-tagged.txt train-tagged/neg-tagged.txt 0.9 5 > train-tagged/v-tagged.txt

					  		python2.7 ../ressources/scripts/vocab.py train-tagged/pos-tagged.txt train-tagged/neg-tagged.txt 0.9 10 > train-tagged/v-tagged.txt


					  		
					- Generate train-2.arff
					  		$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train-tagged/v-tagged.txt train-tagged/pos-tagged/ train-tagged/neg-tagged/ > train-tagged/train-tagged.arff

					  		$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train-tagged/v-tagged.txt test-tagged/pos-tagged/ test-tagged/neg-tagged/ > test-tagged/test-tagged.arff

## RandomForest (TRAIN TAGGED):

			=== Classifier model (full training set) ===

			RandomForest

			Bagging with 100 iterations and base learner

			weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-check-capabilities

			Time taken to build model: 4.97 seconds

			=== Stratified cross-validation ===
			=== Summary ===

			Correctly Classified Instances        1385               86.5625 %
			Incorrectly Classified Instances       215               13.4375 %
			Kappa statistic                          0.7312
			Mean absolute error                      0.3563
			Root mean squared error                  0.3803
			Relative absolute error                 71.265  %
			Root relative squared error             76.0513 %
			Total Number of Instances             1600     

			=== Detailed Accuracy By Class ===

			                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
			                 0.843    0.111    0.883      0.843    0.862      0.732    0.927     0.926     pos
			                 0.889    0.158    0.849      0.889    0.869      0.732    0.927     0.915     neg
			Weighted Avg.    0.866    0.134    0.866      0.866    0.866      0.732    0.927     0.921     

			=== Confusion Matrix ===

			   a   b   <-- classified as
			 674 126 |   a = pos
			  89 711 |   b = neg
## RandomForest (TEST TAGGED):
			=== Classifier model (full training set) ===

			RandomForest

			Bagging with 100 iterations and base learner

			weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-check-capabilities

			Time taken to build model: 4.97 seconds

			=== Evaluation on test set ===

			Time taken to test model on supplied test set: 0.08 seconds

			=== Summary ===

			Correctly Classified Instances         167               83.5    %
			Incorrectly Classified Instances        33               16.5    %
			Kappa statistic                          0.67  
			Mean absolute error                      0.3649
			Root mean squared error                  0.3904
			Relative absolute error                 72.98   %
			Root relative squared error             78.0846 %
			Total Number of Instances              200     

			=== Detailed Accuracy By Class ===

			             TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
			             0.830    0.160    0.838      0.830    0.834      0.670    0.906     0.904     pos
			             0.840    0.170    0.832      0.840    0.836      0.670    0.906     0.878     neg
			Weighted Avg.    0.835    0.165    0.835      0.835    0.835      0.670    0.906     0.891     

			=== Confusion Matrix ===

			a  b   <-- classified as
			83 17 |  a = pos
			16 84 |  b = neg
## LibLinear (TRAIN):
	=== Run information ===

	Scheme:       weka.classifiers.functions.LibLINEAR -S 1 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000
	Relation:     movie-review
	Instances:    1600
	Attributes:   1357
	              [list of attributes omitted]
	Test mode:    10-fold cross-validation

	=== Classifier model (full training set) ===

	LibLINEAR wrapper

	Model bias=1.0 nr_class=2 nr_feature=1357 solverType=L2R_L2LOSS_SVC_DUAL

	=== Stratified cross-validation ===
	=== Summary ===

	Correctly Classified Instances        1281               80.0625 %
	Incorrectly Classified Instances       319               19.9375 %
	Kappa statistic                          0.6013
	Mean absolute error                      0.1994
	Root mean squared error                  0.4465
	Relative absolute error                 39.875  %
	Root relative squared error             89.3029 %
	Total Number of Instances             1600     

	=== Detailed Accuracy By Class ===

	                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	                 0.809    0.208    0.796      0.809    0.802      0.601    0.801     0.739     pos
	                 0.793    0.191    0.806      0.793    0.799      0.601    0.801     0.742     neg
	Weighted Avg.    0.801    0.199    0.801      0.801    0.801      0.601    0.801     0.741     

	=== Confusion Matrix ===

	   a   b   <-- classified as
	 647 153 |   a = pos
	 166 634 |   b = neg
## LibLinear (TEST):
	=== Run information ===

	Scheme:       weka.classifiers.functions.LibLINEAR -S 1 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000
	Relation:     movie-review
	Instances:    1600
	Attributes:   1357
	              [list of attributes omitted]
	Test mode:    user supplied test set:  size unknown (reading incrementally)

	=== Classifier model (full training set) ===

	LibLINEAR wrapper

	Model bias=1.0 nr_class=2 nr_feature=1357 solverType=L2R_L2LOSS_SVC_DUAL

	=== Evaluation on test set ===

	Time taken to test model on supplied test set: 0.04 seconds

	=== Summary ===

	Correctly Classified Instances         153               76.5    %
	Incorrectly Classified Instances        47               23.5    %
	Kappa statistic                          0.53  
	Mean absolute error                      0.235 
	Root mean squared error                  0.4848
	Relative absolute error                 47      %
	Root relative squared error             96.9536 %
	Total Number of Instances              200     

	=== Detailed Accuracy By Class ===

	                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	                 0.760    0.230    0.768      0.760    0.764      0.530    0.765     0.703     pos
	                 0.770    0.240    0.762      0.770    0.766      0.530    0.765     0.702     neg
	Weighted Avg.    0.765    0.235    0.765      0.765    0.765      0.530    0.765     0.703     

	=== Confusion Matrix ===

	  a  b   <-- classified as
	 76 24 |  a = pos
	 23 77 |  b = neg
## SVM SPegasos (TRAIN TAGGED):
	=== Run information ===

	Scheme:       weka.classifiers.functions.SPegasos -F 0 -L 1.0E-4 -E 500
	Relation:     movie-review
	Instances:    1600
	Attributes:   1357
	              [list of attributes omitted]
	Test mode:    10-fold cross-validation

	=== Classifier model (full training set) ===

	Loss function: Hinge loss (SVM)
	=== Stratified cross-validation ===
	=== Summary ===

	Correctly Classified Instances        1362               85.125  %
	Incorrectly Classified Instances       238               14.875  %
	Kappa statistic                          0.7025
	Mean absolute error                      0.1487
	Root mean squared error                  0.3857
	Relative absolute error                 29.75   %
	Root relative squared error             77.1362 %
	Total Number of Instances             1600     

	=== Detailed Accuracy By Class ===

	                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	                 0.853    0.150    0.850      0.853    0.851      0.703    0.851     0.799     pos
	                 0.850    0.148    0.852      0.850    0.851      0.703    0.851     0.799     neg
	Weighted Avg.    0.851    0.149    0.851      0.851    0.851      0.703    0.851     0.799     

	=== Confusion Matrix ===

	   a   b   <-- classified as
	 682 118 |   a = pos
	 120 680 |   b = neg
## SVM SPegasos (TEST TAGGED):
	=== Run information ===

	Scheme:       weka.classifiers.functions.SPegasos -F 0 -L 1.0E-4 -E 500
	Relation:     movie-review
	Instances:    1600
	Attributes:   1357
	              [list of attributes omitted]
	Test mode:    user supplied test set:  size unknown (reading incrementally)

	=== Classifier model (full training set) ===

	Loss function: Hinge loss (SVM)
	=== Evaluation on test set ===

	Time taken to test model on supplied test set: 0.04 seconds

	=== Summary ===

	Correctly Classified Instances         150               75      %
	Incorrectly Classified Instances        50               25      %
	Kappa statistic                          0.5   
	Mean absolute error                      0.25  
	Root mean squared error                  0.5   
	Relative absolute error                 50      %
	Root relative squared error            100      %
	Total Number of Instances              200     

	=== Detailed Accuracy By Class ===

	                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
	                 0.700    0.200    0.778      0.700    0.737      0.503    0.750     0.694     pos
	                 0.800    0.300    0.727      0.800    0.762      0.503    0.750     0.682     neg
	Weighted Avg.    0.750    0.250    0.753      0.750    0.749      0.503    0.750     0.688     

	=== Confusion Matrix ===

	  a  b   <-- classified as
	 70 30 |  a = pos
	 20 80 |  b = neg


## TASK 2 - NGRAM
		Create a folder for the study of ngram:
			$ mkdir train-ngram
			$ mkdir train-ngram/pos-ngram-tagged train-ngram/neg-ngram-tagged

		- Assumption that the token arrive in order concat until ngram quantity:

			$ for f in train-tagged/pos/*.txt; do python2.7 ../ressources/scripts/ngram-tagged.py ../ressources/stopwords.txt <$f >train-ngram/pos-ngram-tagged/`basename $f`; done

			$ for f in train-tagged/neg/*.txt; do python2.7 ../ressources/scripts/ngram-tagged.py ../ressources/stopwords.txt <$f >train-ngram/neg-ngram-tagged/`basename $f`; done


			$ for f in test-tagged/pos/*.txt; do python2.7 ../ressources/scripts/ngram-tagged.py ../ressources/stopwords.txt <$f >test-ngram/pos-ngram-tagged/`basename $f`; done

		- Combine the two classes (train-tagged)
			$ cat train-ngram/pos-ngram-tagged/*.txt > train-ngram/pos-ngram.txt
			$ cat train-ngram/neg-ngram-tagged/*.txt > train-ngram/neg-ngram.txt

		$ python2.7 ../ressources/scripts/vocab-wn.py train-ngram/pos-ngram.txt train-ngram/neg-ngram.txt 0.1 5 > train-ngram/v-tagged.txt

		$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train-ngram/v-tagged.txt train-ngram/pos-ngram-tagged/ train-ngram/neg-ngram-tagged/ > train-ngram/train-ngram.arff




