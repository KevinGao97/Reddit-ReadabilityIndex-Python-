import praw
from ColemanLiauIndex import colemanLiauIndex
import os.path
import time
import json


"""
This function takes in a text file that contains only reddit links, separated by a new line between each link. 
The links are saved into a list and will be used to compute the Coleman-Liau Index of each link. 

"""
def openThreadsFile():

    fileName = "threads.txt"
    allLinks = []


    if os.path.isfile(fileName):
        with open(fileName, 'r') as fp:
            line = fp.readline()
            while line:
                allLinks.append(line.strip())
                line = fp.readline()
                
        return allLinks
    else:
        print("The file, 'threads.txt' was not found")


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
This function prints out all the information in the terminal and writes to the report.txt file.
The information includes: submission title, the submission id, submission upvote count,
total number of comments in the submission, the Coleman-Liau Index of the submission title,
the average Coleman-Liau Index of all top comments 

"""
def outputAllInformation(avgIndexScore, submissionTitleIndex, submissionTitle, upvoteCount, numComments, submissionId):

    filename = 'report.txt'
    
    with open(filename, 'a') as fp:
        print("Title: " + submissionTitle)
        print("Submission id: "+ submissionId)
        print("Number of upvotes: " + str(upvoteCount))
        print("Number of comments: " + str(numComments))

        fp.write("Title: " + submissionTitle + '\n')
        fp.write("Submission id: "+ submissionId + '\n')
        fp.write("Number of upvotes: " + str(upvoteCount) + '\n')
        fp.write("Number of comments: " + str(numComments) + '\n')

        if submissionTitleIndex < 1 :
            print("Coleman-Liau Index of Title: Preschool")
            fp.write("Coleman-Liau Index of Title: Preschool" + '\n')
        elif submissionTitleIndex >= 1 and submissionTitleIndex <= 12:
            print("Coleman-Liau Index of Title: Grade " + str(submissionTitleIndex))
            fp.write("Coleman-Liau Index of Title: Grade " + str(submissionTitleIndex) + '\n')
        else:
            print("Coleman-Liau Index of Title: University level")
            fp.write("Coleman-Liau Index of Title: University level " + '\n')
            

        if avgIndexScore < 1 :
            print("Average Coleman-Liau Index of all top comments: Preschool")
            fp.write("Average Coleman-Liau Index of all top comments: Preschool" + '\n')
        elif avgIndexScore >= 1 and avgIndexScore <= 12:
            print("Average Coleman-Liau Index of all top comments: Grade "+ str(avgIndexScore))
            fp.write("Average Coleman-Liau Index of all top comments: Grade "+ str(avgIndexScore)+ '\n')
        else:
            print("Average Coleman-Liau Index of all top comments: University level")
            fp.write("Average Coleman-Liau Index of all top comments: University level " + '\n')
        
        fp.write('\n')
        fp.close()


"""
Runs all functions above in computing, outputing, and writing to the report.txt file the Coleman Liau Index 

"""
def runColemanLiauIndex(submission):

    #Calculate Coleman-Liau index of top comments
    topCommentList = sanitizeComments(submission)
    avgTopCommentScore = computeColemanLiauIndex(topCommentList)

    #Calculate Coleman-Liau index of submission title 
    submissionTitleIndex = colemanLiauIndex(submission.title)

    #Outputs all information to terminal and writes to the report.txt file
    outputAllInformation(avgTopCommentScore, submissionTitleIndex, submission.title, submission.score, submission.num_comments, submission.id)



"""
The Main Function

"""
def main():

    #Loading in all the necessary information for praw from the 'credentials.json' file
    with open("credentials.json") as fp:
        params = json.load(fp)

    reddit = praw.Reddit(user_agent="Computing the Coleman-Liau Index of top comments (by /u/" + params['username'] + ")",
                     client_id=params['client_id'], client_secret=params['api_key'],
                     username=params['username'], password=params['password'])

        
    if os.path.isfile("threads.txt"):
        response = input("A threads.txt file is detected. Would you like to find the Coleman-Liau Index score of all links in the file? ")
        if response.lower() in ['y', 'yes', 'n', 'no']:
            if response.lower() in ['y', 'yes']:
                allFileLinks = openThreadsFile()
                for i in range (len(allFileLinks)):
                    submission = reddit.submission(url=allFileLinks[i])
                    
                    runColemanLiauIndex(submission)

                    #Prevents multiple API requests made in less than 1 second 
                    time.sleep(3)
            else:
                url = input("Please enter a reddit url: ")
                submission = reddit.submission(url=url)

                runColemanLiauIndex(submission)

        else:
            print("Please answer with 'y', 'yes', 'n', 'no' ")

    else:
        url = input("Please enter a reddit url: ")
        submission = reddit.submission(url=url)
        
        runColemanLiauIndex(submission)


if __name__ == "__main__":
    main()

