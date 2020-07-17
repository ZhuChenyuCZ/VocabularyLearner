def ShowTheWelcomePage():
    #print('                             VocabularyLearner v0.0.1 Demo')
    textfile=open("WelcomeWords.txt","r")
    for line in textfile:
        print(line,end='')
    textfile.close()