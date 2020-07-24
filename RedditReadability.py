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
            if topComments.body.find("[removed]") == -1 and topComments.body.find("[deleted]") == -1 :
                comment = topComments.body.replace('\n', ' ')
                allComments.append(comment)
        except AttributeError:
            print("Did not add the comment")
            continue

    return allComments


"""
Finds the Coleman-Liau index for each comment in the topCommentList list. 
Computes an average Coleman-Liau index of the thread using the topCommentList list

"""
def computeColemanLiauIndex(topCommentList):

    avgColemanLiauIndex = []

    for i in range(len(topCommentList)):
        colemanLiauIndexScore = colemanLiauIndex(topCommentList[i])
        avgColemanLiauIndex.append(colemanLiauIndexScore)
        print(topCommentList[i])
        if colemanLiauIndexScore < 1 :
            print("Coleman-Liau Index: Preschool")
        elif colemanLiauIndexScore >= 1 and colemanLiauIndexScore <= 12:
            print("Coleman-Liau Index: Grade "+ str(colemanLiauIndexScore))
        else:
            print("Coleman-Liau Index: University level")

        print("\n =========================================== \n")
    
    #Prints the average Coleman-Liau Index of the thread 
    avgIndexScore = round(sum(avgColemanLiauIndex)/len(avgColemanLiauIndex))
    
    
    return avgIndexScore

"""
This function prints out all the information needed for the report.txt file which includes:
submission title, submission upvote count, total number of comments in the submission, 
the Coleman-Liau Index of the submission title, the average Coleman-Liau Index of all top comments 

"""

def outputAllInformation(avgIndexScore, submissionTitleIndex, submissionTitle, upvoteCount, numComments):

    print(submissionTitle)
    print("Number of upvotes: " + str(upvoteCount))
    print("Number of comments: " + str(numComments))


    if submissionTitleIndex < 1 :
        print("Coleman-Liau Index of Title: Preschool")
    elif submissionTitleIndex >= 1 and submissionTitleIndex <= 12:
        print("Coleman-Liau Index of Title: Grade "+ str(submissionTitleIndex))
    else:
        print("Coleman-Liau Index of Title: University level")

    if avgIndexScore < 1 :
        print("Average Coleman-Liau Index of top comments: Preschool")
    elif avgIndexScore >= 1 and avgIndexScore <= 12:
        print("Average Coleman-Liau Index of top comments: Grade "+ str(avgIndexScore))
    else:
        print("Average Coleman-Liau Index of top comments: University level")
    

"""
The Main Function

"""
def main():

    
    
    reddit = praw.Reddit(user_agent="Comment Extraction (by /u/USERNAME)",
                     client_id="CLIENT_ID", client_secret="CLIENT_SECRET",
                     username="USERNAME", password="PASSWORD")

    url = input("Please enter a reddit url: ")
    submission = reddit.submission(url=url)


    #Calculate Coleman-Liau index of top comments
    topCommentList = sanitizeComments(submission)
    avgTopCommentScore = computeColemanLiauIndex(topCommentList)

    #Calculate Coleman-Liau index of submission title 
    submissionTitleIndex = colemanLiauIndex(submission.title)

    outputAllInformation(avgTopCommentScore, submissionTitleIndex, submission.title, submission.score, submission.num_comments)
    


if __name__ == "__main__":
    main()

