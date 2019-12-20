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


		- Get term frenquence for each term count if it is present, then divise by the total of terms:

			- for train:
				$ python2.7 ../ressources/scripts/arff-frenqueceterm.py train/v-words.txt train/pos-words train/neg-words >train/train-1-fterm.arff
			- for test:
				$ python2.7 ../ressources/scripts/arff-frenqueceterm.py test/v-words.txt test/pos-words test/neg-words >test/test-1-fterm.arff

			#WEKA Training:
				- SVM:
					=== Stratified cross-validation ===
					=== Summary ===

					Correctly Classified Instances         940               58.75   %
					Incorrectly Classified Instances       660               41.25   %
					Kappa statistic                          0.175 
					Mean absolute error                      0.4125
					Root mean squared error                  0.6423
					Relative absolute error                 82.5    %
					Root relative squared error            128.4523 %
					Total Number of Instances             1600     

					=== Detailed Accuracy By Class ===

					                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
					                 0.948    0.773    0.551      0.948    0.697      0.252    0.588     0.548     pos
					                 0.228    0.053    0.813      0.228    0.355      0.252    0.588     0.571     neg
					Weighted Avg.    0.588    0.413    0.682      0.588    0.526      0.252    0.588     0.560     

					=== Confusion Matrix ===

					   a   b   <-- classified as
					 758  42 |   a = pos
					 618 182 |   b = neg

				- Bagging:
					=== Run information ===

					Scheme:       weka.classifiers.meta.Bagging -P 100 -S 1 -num-slots 1 -I 10 -W weka.classifiers.trees.REPTree -- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0
					Relation:     movie-review
					Instances:    1600
					Attributes:   9304
					              [list of attributes omitted]
					Test mode:    10-fold cross-validation

