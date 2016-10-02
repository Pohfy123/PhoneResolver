===========================
        REQUIREMENT
===========================

- Python 2.7
- Module
	+ nltk		(FOR n-gram)
	+ sklearn	(FOR TF/TF-IDF)
	+ PyICU		(FOR Thai word parserf)


===========================
         OVERVIEW
===========================
STEP1: Google Crawling
STEP2: Thai Parser (PyICU)
STEP3: N-Gram
STEP4: Extract Feature (TF / TF-IDF)


===========================
        HOW TO RUN
===========================
1.) [NOT_COMPLETE] run "setup.py" script

2.) Run these python script (py2)
	STEP1 	---[numberSearchMain.py]	----> ./raw_data/*.txt
	STEP2 	---[wordParser-PyICU.py]	----> ./split/*.txt 
	STEP3 	---[ngram.py]			----> ./split_out/*.txt 
	STEP4 	---[extract_feature.py]		----> ./result/*.txt 