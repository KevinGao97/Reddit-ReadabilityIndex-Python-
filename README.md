# Reddit-ReadabilityIndex-Python-

This python program computes the Coleman-Liau Index for all the top comments of a reddit thread and generates a report.txt indicating the average Coleman-Liau Index of all top comments, along with, the Coleman-Liau Index of the submission title. The program is able to run on either a single reddit link, multiple reddit links stored in a text file, or finding the top 10 posts of a given subreddit. The program is able to access reddit through the use of PRAW(Python Reddit API Wrapper). 

To learn more about the Coleman-Liau Index:
https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index

To learn more about PRAW:
https://pypi.org/project/praw/

### Dependencies 
```
PRAW
json
```
### Setup
1. Please ensure you are using Python version 3.6.0 or up.
2. To install the necessary dependencies, run the following in CMD or terminal: ```pip install -r requirements.txt ```
3. Please setup praw before running the program through the following link: https://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth
4. Edit the 'credentials.json' file with the necessary information needed by PRAW. 
5. When running the program, it will prompt from the following 3 options: \
 A. Checking the Coleman-Liau Index of all top comments from a given reddit link.\
 B. Checking the Coleman-Liau Index of all top comments through a text file containing reddit links, separated by newline. This file is named 'threads.txt'. \
 C. Finding the Coleman-Liau Index of all top comments from the top 10 submissions of an existing subreddit. \

 

### Features
1. Computes the Coleman-Liau Index for the top comments of any reddit submission.
2. Able to read in a text file of reddit links and computing the Coleman-Liau Index of the top comments of each submission.
3. Finds the Coleman-Liau Index of top comments from the top 10 submissions of an existing subreddit. 
4. Generates a report.txt file at the end of the program with the various information. This is generated for each submission:
   - Title of submission
   - Submission ID
   - Number of upvotes
   - Total number of comments
   - Coleman-Liau Index of the submission title
   - Average Coleman-Liau Index of the top comments
5. Securely stores client information needed for praw locally, in a json file.


### Contributors

Kevin Gao

### License & Copywrite

Licensed under [MIT License](LICENSE)
