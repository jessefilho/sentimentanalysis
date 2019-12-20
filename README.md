## REPORT OF SENTIMENT ANALYSIS

	Students: 
		FERREIRA, Jesse.
		TALBI, Samir.

	github: 


# STEP 1:
	 binary term-presence values to term frequencies to study the effect of weighting factor in sentiment classifications.

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


##Results:
			#WEKA Training:
				- SVM (TRAIN):
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


				- SVM (TEST):
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

				- NaiveBayes (TRAIN):
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

				- NaiveBayes (TEST):
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

				- RandomForest (TRAIN):
					=== Run information ===

					Scheme:       weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1
					Relation:     movie-review
					Instances:    1600
					Attributes:   9304
					              [list of attributes omitted]
					Test mode:    5-fold cross-validation

				- RandomForest (TEST):
					=== Stratified cross-validation ===
					=== Summary ===

					Correctly Classified Instances        1281               80.0625 %
					Incorrectly Classified Instances       319               19.9375 %
					Kappa statistic                          0.6013
					Mean absolute error                      0.4278
					Root mean squared error                  0.4368
					Relative absolute error                 85.5575 %
					Root relative squared error             87.3681 %
					Total Number of Instances             1600     

					=== Detailed Accuracy By Class ===

					                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
					                 0.778    0.176    0.815      0.778    0.796      0.602    0.876     0.871     pos
					                 0.824    0.223    0.787      0.824    0.805      0.602    0.876     0.860     neg
					Weighted Avg.    0.801    0.199    0.801      0.801    0.801      0.602    0.876     0.865     

					=== Confusion Matrix ===

					   a   b   <-- classified as
					 622 178 |   a = pos
					 141 659 |   b = neg



