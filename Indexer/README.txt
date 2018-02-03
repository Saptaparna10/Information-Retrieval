Assignment 3:
Goal: Implementing your own inverted indexer. Text processing and corpus	
statistics.	

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has detailed information regarding how to setup, compile and run the programs in the assignment.

The progrms are discussed below in brief:
-- Task1: Generating the corpus:
	The corpus is being generated using the raw wikipedia articles that we downloaded as a part of HW1 Q1. Each text file correponds to one Wikipedia article. The file name is same as that of the article title. The correponding file for the code is Task1.py.

-- Task2: Implementing an inverted indexer and creating inverted indexes: 
	Implementation of an inverted indexer that consumes the corpus in Task 1 and produces an inverted index as output. The file for the code is Task2.py. 
	The indexer generates indexes for unigrams, bigrams and trigrams.  
	
-- Task3: Corpus Statistics.
	For each inverted index in Task2 we generate a term frequency table and document frequency table. We also generate an stop list using the unigram data.


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

GENERAL USAGE NOTES:

-- This file contains instructions about installing softwares and running the programs in Windows Environment.
-- The instructions in the file may not match the installation procedures in other operating systems like Mac OS, Ubuntu OS etc.
-- However, the programs are independent of any operating systems and will run successfully in all platforms once the initial installation has been done. 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTALLATION GUIDE:

-- Download python 2.7.x from https://www.python.org/download/releases/2.7/
-- From Windows Home go to Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables and add two new variables in 'PATH' -> [Home directory of Python]; [Home directory of Python]\Scripts
-- Open Command Prompt and upgrade pip using the following command: 'python -m pip install -U pip'
-- Install BeautifulSoup by using the command 'pip install beautifulsoup4'

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTRUCTIONS TO RUN THE PROGRAM:

-- Open Windows PowerShell
-- Navigate to the directory having the programs
-- Put all the raw text files having the downloaded web pages inside the folder 'articles_hw1'.
-- Run Task1.py using the command 'python Task1.py'. It will generate the corpus after proessing and cleaning the web pages in the folder 'corpus'
-- Run Task2.py using the command 'python Task2.py'. Follow the instructions and it will generate inverted indexes using the files in the folder 'corpus' and store the inverted index table, document frequency tables and term frequency tables in the present directory.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

RESULTS:

-- The programs create the following output  
	1. Task1.py generates the corpus from the web pages in the folder 'articles_hw1' and stores them in the folder 'corpus'
	2. Task2.py generates the index for unigrams, bigrams and trigrams using the files in 'corpus' folder. It prints the inverted index, document frequency table and term frequency table for unigrams, bigrams and trigrams in the present directory. The token count in each document for all the above three n-grams are stored in a data structure (dictionary in python) where the key is the document name and value is the number of tokens. The token count values are printed in the console while the indexer is run. I have used dictionary because it easily maps the the desired key value pair and faster to access
	by the keys.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- https://www.udacity.com/course/intro-to-computer-science--cs101 : Basics of Python Programming and web crawling
-- https://www.crummy.com/software/BeautifulSoup/ : BeautifulSoup has been used for extracting links from web pages
-- https://learnpythonthehardway.org/book/ : Python Programming
-- https://github.com/ : Reference

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

Phone: (+1) 8572729089
E-Mail: das.sa@husky.neu.edu