Assignment 2:
Goal: Link Analysis and	PageRank Implementation

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has detailed information regarding how to setup, compile and run the programs in the assignment.

The progrms are discussed below in brief:
-- Task1: Obtaining directed web graphs: 
	A. Build a graph for the 1000 URLs you crawled in HW1-Task1 by following their links.You may	
modify and re-run your crawler OR extract the links from the articles you downloaded. The graph is in file "G1.txt".
	B. Build a graph for the 1000 URLs that	you would obtain from running a	Depth First Search	
(DFS)-based crawler. The graph is in file "G2.txt".

-- Task2: Implementing and running PageRank: 
	A. Implementation of the PageRank algorithm using the pseudo code provided. The code can be found in 'PageRankImpl.py' file.
	B. Execution of the iterative version of the PageRank algorithms on the two above-mentioned graphs respectively until their 
PageRank values "converge". To test for convergence, calculate the perplexity of the PageRank distribution using the formulae provided. 
	
-- Task3: Qualitative Analysis 
		Examination of the top 10 pages by PageRank and Top 10 by in-link counts for the above-mentioned graphs. Detailed speculation regarding why these pages have high PageRank values.

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
-- Run the program by using the command 'python <File_Name>.py'


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

RESULTS:

-- The program prints in the console the following things in order:
	1. The perplexity values for each iteration
	2. The top 50 pages by their DOC ID and PageRank Score for the graph provided
	3. The top 10 pages as per their in-link counts for the graph provided
	4. Overall statistics for the graph displaying the total number of pages, total number of sinks and total number of sources for 
	the input graph.

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