import praw

reddit = praw.Reddit(user_agent="Comment Extraction (by /u/USERNAME)",
                     client_id="CLIENT_ID", client_secret="CLIENT_SECRET",
                     username="USERNAME", password="PASSWORD")

url = input("Please enter a reddit url: ")
submission = reddit.submission(url=url)

for topComments in submission.comments:
    print(topComments.body)