Assignment 4:
Goal: Introduction to Lucene. Retrieval and scoring using BM25

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has detailed information regarding how to setup, compile and run the programs in the assignment.

The progrms are discussed below in brief:
-- Task1: Introduction to Lucene
		  Download Lucene and do a local setup for the same. Go through the Lucene documentation and the provided code to perform the     following:
			 A. Index the raw documents of Assignment 3 Task1 using "SimpleAnalyzer".
			 B. Perform search operation for the nine queries provided in Task2 and return top 100 results for each query using the default document scoring/ranking function provided by Lucene.
		 
-- Task2: Use the HW3 corpus and implement the BM25 ranking algorithm to provide 
		  a ranked list of documents for a file with one or more queries. Submit the output from this run for the top 100 search results.

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

-- In order to run Task1, perform the following steps:
     A. Make a new project in Java and use the HW4.java file provided as a part of Submission. 
	 B. Add the three following jars into your project's list of referenced libraries:
	    1. lucene-core-VERSION.jar
		2. lucene-queryparser-VERSION.jar
		3. lucene-analyzers-common-VERSION.jar
	C. Put all the corpus files inside the folder named 'corpus'.
	D. Run the java program.
	E. Enter the path of the parent directory of the 'corpus' folder when you see the following prompt -- 'Enter the path of the source_code folder'. The same path also contains the 'query.txt' having the list of queries.
	F. The program will generate the index for the corpus given to it and store the same in the folder named 'lucene_index_files' provided along with the submission. It will read the queries from 'query.txt', perform a search operation for the provided queries and store the search results for top 100 documents in 'doc_score_lucene' folder.
	
-- In order to run Task2, perform the following steps:
	  A. Open Windows PowerShell
	  B. Navigate to the directory having the programs.
	  C. Perform the following steps in order:
	     1. Put all the corpus files inside the folder named 'corpus'. 
		 2. Run Task2.py using the command 'python Task1.py'. 
		 3. It will produce an inverted index first. Next, it will read the queries from 'query.txt' and for each query it will perform search operation and store the search results for top 100 documents in 'doc_score_BM25' folder.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

RESULTS:

-- The programs create the following output  
	1. Task1 after running successfully generates a ranked list of documents in the file 'doc_score_lucene' folder. using the Lucene System.
	2. Task2 after running successfully generates a ranked list of documents in the file 'doc_score_BM25' folder using the BM25.
	
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- https://www.udacity.com/course/intro-to-computer-science--cs101 : Basics of Python Programming and web crawling
-- https://www.crummy.com/software/BeautifulSoup/ : BeautifulSoup has been used for extracting links from web pages
-- https://learnpythonthehardway.org/book/ : Python Programming
-- https://github.com/ : Reference

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

Phone: (+1) 8572729089
E-Mail: das.sa@husky.neu.edu