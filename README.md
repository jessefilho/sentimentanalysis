# REPORT OF SENTIMENT ANALYSIS

	Students: 
		FERREIRA, Jesse.
		TALBI, Samir.

	github: 


## STEP 1 - Term Frequencies:
	  To study the effect of weighting factor in sentiment classifications, we choose to do the ratio of the term by all terms. The results are presented at results section.

	 - trim each document in trainning corpus (pos and neg) removing all stop
	words and non-alphanumeric words. The out result files will be to new directories
	called:
		pos-words: train/pos-words/
		neg-words: train/neg-words/

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

		execute the trim.py:
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

					$ cat test/pos-words/*.txt >test/pos-words.txt
					$ cat test/neg-words/*.txt >test/neg-words.txt


		- Get term's frenquence:

			- for train, by ratio. For each term count if it is present, then divise by the total of terms:
				$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train/v-words.txt train/pos-words train/neg-words >train/train-1-fterm.arff
			- for train, by quantity:
				$ python2.7 ../ressources/scripts/arff-freq_by_qty.py train/v-words.txt train/pos-words train/neg-words >train/train-1-by_qty.arff


			- for test, by ratio:
				$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train/v-words.txt test/pos-words test/neg-words >test/test-1-fterm.arff
			- for test, by quantity:
				$ python2.7 ../ressources/scripts/arff-freq_by_qty.py train/v-words.txt test/pos-words test/neg-words >test/test-1-by_qty.arff


# Results:

## WEKA Training Frequence of Terms:
				
## SVM (TRAIN):

					=== Run information ===

					Scheme:       weka.classifiers.functions.LibSVM -S 0 -K 2 -D 3 -G 0.0 -R 0.0 -N 0.5 -M 40.0 -C 1.0 -E 0.001 -P 0.1 -model /Users/jessefilho/Documents/BDMA/M2/NPL/weka -seed 1
					Relation:     movie-review
					Instances:    1600
					Attributes:   9304
					              [list of attributes omitted]
					Test mode:    5-fold cross-validation  

					=== Stratified cross-validation ===
					=== Summary ===

					Correctly Classified Instances         964               60.25   %
					Incorrectly Classified Instances       636               39.75   %
					Kappa statistic                          0.205 
					Mean absolute error                      0.3975
					Root mean squared error                  0.6305
					Relative absolute error                 79.5    %
					Root relative squared error            126.0952 %
					Total Number of Instances             1600     

					=== Detailed Accuracy By Class ===

					                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
					                 0.943    0.738    0.561      0.943    0.703      0.280    0.603     0.558     pos
					                 0.263    0.058    0.820      0.263    0.398      0.280    0.603     0.584     neg
					Weighted Avg.    0.603    0.398    0.691      0.603    0.551      0.280    0.603     0.571     

					=== Confusion Matrix ===

					   a   b   <-- classified as
					 754  46 |   a = pos
					 590 210 |   b = neg


## SVM (TEST):
					=== Run information ===

					Scheme:       weka.classifiers.functions.LibSVM -S 0 -K 2 -D 3 -G 0.0 -R 0.0 -N 0.5 -M 40.0 -C 1.0 -E 0.001 -P 0.1 -model /Users/jessefilho/Documents/BDMA/M2/NPL/weka -seed 1
					Relation:     movie-review
					Instances:    1600
					Attributes:   9304
					              [list of attributes omitted]
					Test mode:    user supplied test set:  size unknown (reading incrementally)

					=== Classifier model (full training set) ===

					LibSVM wrapper, original code by Yasser EL-Manzalawy (= WLSVM)

					Time taken to build model: 7.08 seconds

					=== Evaluation on test set ===

					Time taken to test model on supplied test set: 1.28 seconds

					=== Summary ===

					Correctly Classified Instances         116               58      %
					Incorrectly Classified Instances        84               42      %
					Kappa statistic                          0.16  
					Mean absolute error                      0.42  
					Root mean squared error                  0.6481
					Relative absolute error                 84      %
					Root relative squared error            129.6148 %
					Total Number of Instances              200     

					=== Detailed Accuracy By Class ===

					                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
					                 0.940    0.780    0.547      0.940    0.691      0.231    0.580     0.544     pos
					                 0.220    0.060    0.786      0.220    0.344      0.231    0.580     0.563     neg
					Weighted Avg.    0.580    0.420    0.666      0.580    0.517      0.231    0.580     0.553     

					=== Confusion Matrix ===

					  a  b   <-- classified as
					 94  6 |  a = pos
					 78 22 |  b = neg

## NaiveBayes (TRAIN):

					=== Run information ===

					Scheme:       weka.classifiers.bayes.NaiveBayes 
					Relation:     movie-review
					Instances:    1600
					Attributes:   9304
					              [list of attributes omitted]
					Test mode:    5-fold cross-validation

					=== Stratified cross-validation ===
					=== Summary ===

					Correctly Classified Instances        1231               76.9375 %
					Incorrectly Classified Instances       369               23.0625 %
					Kappa statistic                          0.5388
					Mean absolute error                      0.2306
					Root mean squared error                  0.4798
					Relative absolute error                 46.1216 %
					Root relative squared error             95.9695 %
					Total Number of Instances             1600     

					=== Detailed Accuracy By Class ===

					                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
					                 0.725    0.186    0.796      0.725    0.759      0.541    0.786     0.737     pos
					                 0.814    0.275    0.747      0.814    0.779      0.541    0.784     0.720     neg
					Weighted Avg.    0.769    0.231    0.772      0.769    0.769      0.541    0.785     0.729     

					=== Confusion Matrix ===

					   a   b   <-- classified as
					 580 220 |   a = pos
					 149 651 |   b = neg

## NaiveBayes (TEST):

					=== Run information ===

					Scheme:       weka.classifiers.bayes.NaiveBayes 
					Relation:     movie-review
					Instances:    1600
					Attributes:   9304
					              [list of attributes omitted]
					Test mode:    user supplied test set:  size unknown (reading incrementally)

					=== Evaluation on test set ===

					Time taken to test model on supplied test set: 1.03 seconds

					=== Summary ===

					Correctly Classified Instances         148               74      %
					Incorrectly Classified Instances        52               26      %
					Kappa statistic                          0.48  
					Mean absolute error                      0.26  
					Root mean squared error                  0.5099
					Relative absolute error                 52      %
					Root relative squared error            101.9804 %
					Total Number of Instances              200     

					=== Detailed Accuracy By Class ===

					                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
					                 0.680    0.200    0.773      0.680    0.723      0.483    0.745     0.699     pos
					                 0.800    0.320    0.714      0.800    0.755      0.483    0.756     0.688     neg
					Weighted Avg.    0.740    0.260    0.744      0.740    0.739      0.483    0.751     0.694     

					=== Confusion Matrix ===

					  a  b   <-- classified as
					 68 32 |  a = pos
					 20 80 |  b = neg

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
								$ for f in train-tagged/pos/*.txt; do python2.7 ../ressources/scripts/trim-tagged.py ../ressources/stopwords.txt <$f >train-tagged/pos-tagged/`basename $f`; done
							- for neg-tagged:
								$ for f in train-tagged/neg/*.txt; do python2.7 ../ressources/scripts/trim-tagged.py ../ressources/stopwords.txt <$f >train-tagged/neg-tagged/`basename $f`; done

						- for test dataset:
							- for pos-tagged:
								$ for f in test-tagged/pos/*.txt; do python2.7 ../ressources/scripts/trim-tagged.py ../ressources/stopwords.txt <$f >test-tagged/pos-tagged/`basename $f`; done
							- for neg-tagged:
								$ for f in test-tagged/neg/*.txt; do python2.7 ../ressources/scripts/trim-tagged.py ../ressources/stopwords.txt <$f >test-tagged/neg-tagged/`basename $f`; done

					- Combine the two classes (train-tagged)
							$ cat train-tagged/pos-tagged/*.txt > train-tagged/pos-tagged.txt
							$ cat train-tagged/neg-tagged/*.txt > train-tagged/neg-tagged.txt
					- Combine the two classes (train-tagged)
							$ cat test-tagged/pos-tagged/*.txt > test-tagged/pos-tagged.txt
							$ cat test-tagged/neg-tagged/*.txt > test-tagged/neg-tagged.txt


					- Generate the dictionary file that contains all vocabulary terms corresponding to the set of
					  all attributes appearing in the vector representation of documents.

					  		$ python2.7 ../ressources/scripts/vocab.py train-tagged/pos-tagged.txt train-tagged/neg-tagged.txt 0.1 5 > train-tagged/v-tagged.txt

					  		
					- Generate train-2.arff
					  		$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train-tagged/v-tagged.txt train-tagged/pos-tagged/ train-tagged/neg-tagged/ > train-tagged/train-2.arff

					  		$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train-tagged/v-tagged.txt test-tagged/pos-tagged/ test-tagged/neg-tagged/ > test-tagged/test-2.arff

## RandomForest (TRAIN TAGGED):

			=== Classifier model (full training set) ===

			RandomForest

			Bagging with 100 iterations and base learner

			weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-check-capabilities

			Time taken to build model: 18.8 seconds

			=== Stratified cross-validation ===
			=== Summary ===

			Correctly Classified Instances        1282               80.125  %
			Incorrectly Classified Instances       318               19.875  %
			Kappa statistic                          0.6025
			Mean absolute error                      0.4233
			Root mean squared error                  0.4331
			Relative absolute error                 84.6575 %
			Root relative squared error             86.6186 %
			Total Number of Instances             1600     

			=== Detailed Accuracy By Class ===

			                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
			                 0.766    0.164    0.824      0.766    0.794      0.604    0.881     0.885     pos
			                 0.836    0.234    0.782      0.836    0.808      0.604    0.881     0.863     neg
			Weighted Avg.    0.801    0.199    0.803      0.801    0.801      0.604    0.881     0.874     

			=== Confusion Matrix ===

			   a   b   <-- classified as
			 613 187 |   a = pos
			 131 669 |   b = neg
## RandomForest (TEST TAGGED):
			RandomForest

			Bagging with 100 iterations and base learner

			weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-check-capabilities

			Time taken to build model: 19.41 seconds

			=== Evaluation on test set ===

			Time taken to test model on supplied test set: 0.26 seconds

			=== Summary ===

			Correctly Classified Instances         162               81      %
			Incorrectly Classified Instances        38               19      %
			Kappa statistic                          0.62  
			Mean absolute error                      0.4203
			Root mean squared error                  0.4289
			Relative absolute error                 84.07   %
			Root relative squared error             85.7719 %
			Total Number of Instances              200     

			=== Detailed Accuracy By Class ===

			                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
			                 0.750    0.130    0.852      0.750    0.798      0.625    0.905     0.911     pos
			                 0.870    0.250    0.777      0.870    0.821      0.625    0.905     0.893     neg
			Weighted Avg.    0.810    0.190    0.815      0.810    0.809      0.625    0.905     0.902     

			=== Confusion Matrix ===

			  a  b   <-- classified as
			 75 25 |  a = pos
			 13 87 |  b = neg
## NaiveBayes (TRAIN TAGGED):
			=== Stratified cross-validation ===
			=== Summary ===

			Correctly Classified Instances        1128               70.5    %
			Incorrectly Classified Instances       472               29.5    %
			Kappa statistic                          0.41  
			Mean absolute error                      0.2959
			Root mean squared error                  0.5425
			Relative absolute error                 59.1764 %
			Root relative squared error            108.4928 %
			Total Number of Instances             1600     

			=== Detailed Accuracy By Class ===

			                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
			                 0.750    0.340    0.688      0.750    0.718      0.412    0.733     0.673     pos
			                 0.660    0.250    0.725      0.660    0.691      0.412    0.769     0.728     neg
			Weighted Avg.    0.705    0.295    0.707      0.705    0.704      0.412    0.751     0.700     

			=== Confusion Matrix ===

			   a   b   <-- classified as
			 600 200 |   a = pos
			 272 528 |   b = neg
## NaiveBayes (TEST TAGGED):
			=== Evaluation on test set ===

			Time taken to test model on supplied test set: 1.18 seconds

			=== Summary ===

			Correctly Classified Instances         144               72      %
			Incorrectly Classified Instances        56               28      %
			Kappa statistic                          0.44  
			Mean absolute error                      0.2795
			Root mean squared error                  0.528 
			Relative absolute error                 55.8993 %
			Root relative squared error            105.6084 %
			Total Number of Instances              200     

			=== Detailed Accuracy By Class ===

			                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
			                 0.780    0.340    0.696      0.780    0.736      0.443    0.751     0.693     pos
			                 0.660    0.220    0.750      0.660    0.702      0.443    0.768     0.733     neg
			Weighted Avg.    0.720    0.280    0.723      0.720    0.719      0.443    0.760     0.713     

			=== Confusion Matrix ===

			  a  b   <-- classified as
			 78 22 |  a = pos
			 34 66 |  b = neg
## SVM (TRAIN TAGGED):
			=== Classifier model (full training set) ===

			LibSVM wrapper, original code by Yasser EL-Manzalawy (= WLSVM)

			Time taken to build model: 6.82 seconds

			=== Stratified cross-validation ===
			=== Summary ===

			Correctly Classified Instances         800               50      %
			Incorrectly Classified Instances       800               50      %
			Kappa statistic                          0     
			Mean absolute error                      0.5   
			Root mean squared error                  0.7071
			Relative absolute error                100      %
			Root relative squared error            141.4214 %
			Total Number of Instances             1600     

			=== Detailed Accuracy By Class ===

			                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
			                 0.000    0.000    0.000      0.000    0.000      0.000    0.500     0.500     pos
			                 1.000    1.000    0.500      1.000    0.667      0.000    0.500     0.500     neg
			Weighted Avg.    0.500    0.500    0.250      0.500    0.333      0.000    0.500     0.500     

			=== Confusion Matrix ===

			   a   b   <-- classified as
			   0 800 |   a = pos
			   0 800 |   b = neg
## SVM (TEST TAGGED):
			   === Evaluation on test set ===

				Time taken to test model on supplied test set: 1.02 seconds

				=== Summary ===

				Correctly Classified Instances         101               50.5    %
				Incorrectly Classified Instances        99               49.5    %
				Kappa statistic                          0.01  
				Mean absolute error                      0.495 
				Root mean squared error                  0.7036
				Relative absolute error                 99      %
				Root relative squared error            140.7125 %
				Total Number of Instances              200     

				=== Detailed Accuracy By Class ===

				                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
				                 0.010    0.000    1.000      0.010    0.020      0.071    0.505     0.505     pos
				                 1.000    0.990    0.503      1.000    0.669      0.071    0.505     0.503     neg
				Weighted Avg.    0.505    0.495    0.751      0.505    0.344      0.071    0.505     0.504     

				=== Confusion Matrix ===

				   a   b   <-- classified as
				   1  99 |   a = pos
				   0 100 |   b = neg


## TASK 2 - NGRAM
		Create a folder for the study of ngram:
			$ mkdir train-ngram
			$ mkdir train-ngram/pos-ngram-tagged train-ngram/neg-ngram-tagged

		- Assumption that the token arrive in order concat until ngram quantity:

			$ for f in train-tagged/pos/*.txt; do python2.7 ../ressources/scripts/ngram-tagged.py ../ressources/stopwords.txt <$f >train-ngram/pos-ngram-tagged/`basename $f`; done

			$ for f in train-tagged/pos/*.txt; do python2.7 ../ressources/scripts/ngram-tagged.py ../ressources/stopwords.txt <$f >train-ngram/neg-ngram-tagged/`basename $f`; done


			$ for f in test-tagged/pos/*.txt; do python2.7 ../ressources/scripts/ngram-tagged.py ../ressources/stopwords.txt <$f >test-ngram/pos-ngram-tagged/`basename $f`; done

		- Combine the two classes (train-tagged)
			$ cat train-ngram/pos-ngram-tagged/*.txt > train-ngram/pos-ngram.txt
			$ cat train-ngram/neg-ngram-tagged/*.txt > train-ngram/neg-ngram.txt

		$ python2.7 ../ressources/scripts/vocab.py train-ngram/pos-ngram.txt train-ngram/neg-ngram.txt 0.1 5 > train-ngram/v-tagged.txt

		$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train-ngram/v-tagged.txt train-ngram/pos-ngram-tagged/ train-ngram/neg-ngram-tagged/ > train-ngram/train-ngram.arff




