import praw
from ColemanLiauIndex import colemanLiauIndex

"""
This function takes in the thread url top comments and sanitizes each comment, removing any trailing newline characters
and '[removed]' comments. 

"""
def sanitizeComments(submission):

    allComments = []

    for topComments in submission.comments:
        try:
            if topComments.body.find("[removed]") == -1:
                allComments.append(topComments.body.replace('\n', ' '))
        except AttributeError:
            print("Did not add the comment")
            continue

    for i in range(len(allComments)):
        print(allComments[i])
        print("Coleman-Liau Index: " + str(colemanLiauIndex(allComments[i])))
        print("\n =========================================== \n")
    
    return allComments


"""
The Main Function

"""
def main():

    
    reddit = praw.Reddit(user_agent="Comment Extraction (by /u/USERNAME)",
                        client_id="CLIENT_ID", client_secret="CLIENT_SECRET",
                        username="USERNAME", password="PASSWORD")

    url = input("Please enter a reddit url: ")
    submission = reddit.submission(url=url)


    sanitizeComments(submission)

main()

