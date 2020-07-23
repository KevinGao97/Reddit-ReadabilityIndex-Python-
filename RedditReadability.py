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
    if avgIndexScore < 1 :
        print("Average Coleman-Liau Index: Preschool")
    elif avgIndexScore >= 1 and avgIndexScore <= 12:
        print("Average Coleman-Liau Index: Grade "+ str(avgIndexScore))
    else:
        print("Average Coleman-Liau Index: University level")


    

"""
The Main Function

"""
def main():

    
    reddit = praw.Reddit(user_agent="Comment Extraction (by /u/USERNAME)",
                     client_id="CLIENT_ID", client_secret="CLIENT_SECRET",
                     username="USERNAME", password="PASSWORD")

    url = input("Please enter a reddit url: ")
    submission = reddit.submission(url=url)

    topCommentList = sanitizeComments(submission)
    computeColemanLiauIndex(topCommentList)


main()

