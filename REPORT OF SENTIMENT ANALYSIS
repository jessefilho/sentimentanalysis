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
			- for pos-words:
				$ for f in train/pos/*.txt; do python2.7 ../ressources/scripts/trim.py ../ressources/stopwords.txt <$f >train/pos-words/`basename $f`; done
			- for neg-words:
				$ for f in train/neg/*.txt; do python2.7 ../ressources/scripts/trim.py ../ressources/stopwords.txt <$f >train/neg-words/`basename $f`; done

			- Combine the two classes (pos and neg) of trimmed training corpus to two individual files:
				train/pos-words.txt
				train/neg-words.txt

				$ cat train/pos-words/*.txt >train/pos-words.txt
				$ cat train/neg-words/*.txt >train/neg-words.txt



