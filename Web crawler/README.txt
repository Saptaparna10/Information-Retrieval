Assignment 1:
Goal: Implementing your	own web	crawler. Performing focused crawling

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has detailed information regarding how to setup, compile and run the programs in the assignment.
The progrms are discussed below in brief:
-- Task1: A web crawler that starts from the following seed URL "https://en.wikipedia.org/wiki/Tropical_cyclone" and crawls 
upto depth 6 or  maximum of 1000 unique URLs. Pages in a shallower depth are more important than deeper ones, also within each
 individual page, hyperlinks appearing earlier on the webpage should be crawled first.
 
-- Task2: The web crawler should be able to consume two arguments: a URL and a keyword to be matched against anchor text or text within a URL.
It starts with the seed URL "https://en.wikipedia.org/wiki/Tropical_cyclone" and crawls to a depth 6 at most using the keyword "rain". (change the word in main function to test for other keywords)
It should return at most 1000 URLs.

	
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

-- The program creates a file named 'crawled_urls' which lists all the URLs that has been crawled.
-- The contents of all webpages that has been crawled are stored in individual files along with their URLs.
-- The files are created in the same directory where we have the program.
-- Reached till depth 2 in Task 1 and depth 3 in Task 2

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