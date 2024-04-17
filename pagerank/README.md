
The pagerank.py script is a Python implementation of Google's PageRank algorithm. The script takes a corpus of web pages as input, represented as a directory of HTML files, and calculates the PageRank for each page.

The script uses two methods to calculate PageRank: a sampling method and an iterative method. The sampling method simulates a web surfer who randomly clicks on links, while the iterative method calculates PageRank based on the inbound links to each page.

The script begins by crawling the provided directory of HTML files, parsing each file to extract links to other pages. It then uses these links to construct a graph of the web pages and their connections.

The PageRank results from both the sampling and iterative methods are then printed to the console, sorted in alphabetical order by page name. The PageRank values are displayed with a precision of four decimal places.

The script uses a damping factor of 0.85 and a sample size of 10,000 by default, but these values can be adjusted as needed. The script also includes a threshold value of 0.001 to determine when the iterative method has converged on a solution.
