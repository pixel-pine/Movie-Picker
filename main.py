import os
import json
import random

movieDataFile = open('data.json')
data = json.load(movieDataFile)


def movieSelection(genreInput, ratingInput, lengthInput):
    keepTrying="y"
    while keepTrying=="y":

        os.system('clear') #'cls' on windows

        movieList = []

        # make sure some criteria is entered
        if genreInput=='' and ratingInput=='' and lengthInput=='':
            print ("No criteria was entered.")
            input ("Press any key to continue.")
            keepTrying = "n"
        else:
            # checks for/finds the user's selection throughout the list
            count = 0
            for x in data['movies']:
                if ((genreInput == '' or x['genre'] == genreInput) 
                and (ratingInput == '' or x['rating'] == ratingInput) 
                and (lengthInput == '' or x['length'] == lengthInput)):
                    movieList.append (x['movie'])
                    count = count + 1

            if  count == 0:
                print ("Sorry, no movies matched your selection.")
                input ("Press any key to continue.")
                keepTrying = "n"
            else:
                print ("Movie found: ",random.choice(movieList))

                keepTrying = (
                    getValidInput("Would you like to try to find another "+
                    "movie under the same criteria? (y/n)",
                    ['y','n']))


def getValidInput(prompt, validValues):
    userInput=None
    while userInput not in validValues:
        userInput=input(prompt).lower()
        if userInput not in validValues:
            print ("Value entered is incorrect.  Please try again")
    return userInput


def showAllMovies():
    pageNumber = 1
    pageSize = 10
    rowNumber = 0
    totalRows = len(data['movies'])
    totalPages = totalRows/pageSize
    
    inputOption = None
    while inputOption != 'x':

        os.system('clear')

        # show page
        print ("MOVIE NAME")
        
        while rowNumber <  pageNumber * pageSize and rowNumber<totalRows:
            print(data['movies'][rowNumber]['movie'])
            rowNumber = rowNumber+1

        print ("")
        print ("Page No: ",pageNumber)
        print ("")


        # get user input
        validOptions = []
        prompt = "[X] Main Menu"
        validOptions.append('x')

        if (pageNumber>1):
            validOptions.append ('p')
            prompt = prompt + ', [P] Previous page'
        
        if (pageNumber<totalPages):
            validOptions.append ('n')
            prompt = prompt + ', [N] Next page'
        
        inputOption=(getValidInput(prompt+': ',validOptions))
        
        if inputOption=='p':
           pageNumber = pageNumber - 1 
           rowNumber = (pageNumber-1) * pageSize
        if inputOption=='n':
           pageNumber = pageNumber + 1 
           rowNumber = (pageNumber-1) * pageSize


def mainLoop():
    loopVariable = None
    while loopVariable != 'x':
   
        os.system('clear')
        print('MAIN MENU')
        print('')
        print('Please select an option')
        print('[1] Suggest a movie randomly')
        print('[2] See all Movies')
        print('[X] Quit')

        loopVariable=(getValidInput("Please enter your choice: ",['1','2','x']))

        if (loopVariable == '1'):
            # get user input
            genreInput=(
                getValidInput("What genre of movie would you like to watch? "+
                "(type: action, romance, comedy, fantasy, sci-fi, or leave blank): ",
                ['action', 'romance', 'comedy', 'fantasy', 'sci-fi','']))
            ratingInput=(
                getValidInput("What rating would you like to watch? "+
                "(type: g, pg, pg-13, or leave blank): ",
                ['g', 'pg', 'pg-13','']))
            lengthInput=(
                getValidInput("What length of movie would you like to watch? "+
                "(type: short, medium, long, or leave blank): ",
                ['short', 'medium', 'long','']))
            movieSelection(genreInput, ratingInput, lengthInput)
        if (loopVariable == '2'):
            showAllMovies()


mainLoop()    
print ("See you later.")