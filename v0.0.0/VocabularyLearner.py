import SQL
import base

def ShowTheWelcomePage():
    from WelcomePage import ShowTheWelcomePage
    ShowTheWelcomePage()

def SignInOrUp():
    print('0 for sign in and 1 for sign up.')
    SignInOrUpNum=int(input())

def SQLRead():
    textfile=open("SaveFile.txt","r")
    TempSaveArray = []
    TempLen=0
    countType=0
    count = 0
    for line in textfile:
        TempSaveArray.append(line)
        TempLen+=1

    while SQL.TotalLen*3<TempLen:
        SQL.TotalLen+=1
        SQL.Words.append('save')
        SQL.Type.append('0')
        SQL.Meaning.append('占位')
    
    i=0
    while 3*i<TempLen:
        SQL.Words[i]=TempSaveArray[3*i]
        SQL.Type[i]=TempSaveArray[3*i+1]
        SQL.Meaning[i]=TempSaveArray[3*i+2]
        i+=1

    textfile.close()

def SQLWrite():
    #文件操作请查阅
    #https://www.yiibai.com/python/python_files_io.html
    textfile=open("SaveFile.txt","w")
    for i in range(0,SQL.TotalLen):
        textfile.write(SQL.Words[i])
        textfile.write(SQL.Type[i])
        textfile.write(SQL.Meaning[i])
    textfile.close()

def AddWords():
    NewWords = str(input('Add a new Word: '))
    NewWords += '\n'
    NewWordsMeaning = str(input('What\'s it mean: '))
    NewWordsMeaning += '\n'
    SQL.TotalLen+=1
    SQL.Words.append(NewWords)
    SQL.Type.append('0\n')
    SQL.Meaning.append(NewWordsMeaning)

def main():
    ShowTheWelcomePage()
    
    SQLRead()
    #SignInOrUp()
    for i in range(0,SQL.TotalLen):
        print(SQL.Words[i],end='')
    AddWords()
    AddWords()
    SQLWrite()

if __name__ == '__main__':
    main()