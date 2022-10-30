* Breakdown
All of my codes are in src/pagerank.py

* Description
I first read the input file, then I parsed it to store target pages and source pages in two maps. inlinks_map's key is a page, and its value is an array storing pages that point to it. outlinks_map's kep is a page, and its value is an array storing pages that it points to. In order to find how many inlinks each page has, I sort my inlinks_map using built in sorting in Python in descending order. I then display the first 100 pages in the sorted list and write them to inlinks.txt. Each page rank was calculated using the algorithm in the book and stored in R. I use L2 norm to calculate convergence by calulating the probability difference in the previous page and the page after calculated. This can be achieved by getting the square root of the sum of each page's squared value. I then parse the links and ranks and write them to pagerank.txt. Since the algorithms for the page rank in the book do a nested for loop where it iterates through all the pages twice (line 20-22). Therefore, I took it out and do a two for loops instead to improve time complexity.

* Libraries
I use 'math' to calculate the square root. 'sys' and 'gzip' are for command line handling. 'copy' for copying objects since Objects are assigned by reference.

* Dependencies
I do not include any dependencies in my code.

* Building
On your terminal, run python3 pagerank.py

* Running
On your terminal, run python3 pagerank.py