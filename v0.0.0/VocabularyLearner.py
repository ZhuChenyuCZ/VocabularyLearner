import SQL
import base
import random
import math

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

    while SQL.TotalLen*5<TempLen:
        SQL.TotalLen+=1
        SQL.Words.append('save')
        SQL.Type.append(0)
        SQL.Meaning.append('占位')
        SQL.WrongTime.append(0)
        SQL.Weight.append(1)
        SQL.Hash.append(0)
    
    i=0
    while 5*i<TempLen:
        SQL.Words[i]=TempSaveArray[5*i]
        SQL.Type[i]=int(TempSaveArray[5*i+1])
        SQL.Meaning[i]=TempSaveArray[5*i+2]
        SQL.WrongTime[i]=int(TempSaveArray[5*i+3])
        SQL.Weight[i]=int(TempSaveArray[5*i+4])
        i+=1

    textfile.close()

def SQLWrite():
    #文件操作请查阅
    #https://www.yiibai.com/python/python_files_io.html
    textfile=open("SaveFile.txt","w")
    for i in range(0,SQL.TotalLen):
        textfile.write(SQL.Words[i])
        textfile.write('%s\n' %str(SQL.Type[i]))
        textfile.write(SQL.Meaning[i])
        textfile.write('%s\n' % str(SQL.WrongTime[i]))
        textfile.write('%s\n' % str(SQL.Weight[i]))
    textfile.close()

def AddWords():
    NewWords = str(input('Add a new Word(write No to exit): '))
    if NewWords == 'no' or NewWords == 'No' or NewWords == 'NO':
        base.ModeType = 0
        return
    NewWords += '\n'
    NewWordsMeaning = str(input('What\'s it mean: '))
    NewWordsMeaning += '\n'
    SQL.TotalLen+=1
    SQL.Words.append(NewWords)
    SQL.Type.append(0)
    SQL.Meaning.append(NewWordsMeaning)
    SQL.WrongTime.append(0)
    SQL.Weight.append(1)
    SQL.Hash.append(0)

def ChooseMode():
    print('添加新单词输入1 ， 测试以往单词输入2 ,测试单词无限模式输入3，退出请输入 0')
    base.ModeType = int(input('Mode:'))
    if base.ModeType<1 or base.ModeType>3:
        base.ModeType = -1

def InfiniteTestMode():
    print('进入无尽模式')
    i=0
    while i<SQL.TotalLen:
        NowID = math.floor(random.random()*SQL.TotalLen-0.0001)
        while SQL.Hash[NowID] == 1:
            NowID = math.floor(random.random()*SQL.TotalLen-0.001)
        print('NowID:%d' % NowID)
        print('请问这个单词是什么意思: %s' % SQL.Words[NowID] , end = '')
        TempStr = str(input('输入任何字符查看解释'))
        print(SQL.Meaning[NowID])
        TempStr = str(input('下一个单词输入回车，保留这个单词输入r，退出输入e:'))
        if TempStr == 'e':
            break
        elif TempStr == 'r':
            SQL.Hash[NowID] = 0
        else:
            SQL.Hash[NowID] = 1
            i += 1
        print('next')
    print('退出无尽模式')
    base.ModeType = 0

def main():
    ShowTheWelcomePage()
    
    SQLRead()
    #SignInOrUp()
    """for i in range(0,SQL.TotalLen):
        print(SQL.Words[i],end='')
    AddWords()
    AddWords()
    SQLWrite()"""

    running = True

    while running:
        SQLWrite()
        if base.ModeType == -1:
            running = False
            break
        elif base.ModeType == 0:
            ChooseMode()
            continue
        elif base.ModeType == 1:
            #添加新单词模式
            AddWords()
            #base.ModeType = 0
        elif base.ModeType == 2:
            #测试单词模式
            TestNum = int(input('想要测试多少个单词：'))
            for i in range(0,TestNum):
                NowWords = math.floor(random.random()*SQL.TotalLen - 0.001)
                print('       %s' % SQL.Words[NowWords] , end='')
                TempStr = str(input('输入任何字符查看解释'))
                print('       %s' % SQL.Meaning[NowWords])
                TempStr = str(input('输入任何字符测试下一个'))
            base.ModeType = 0
        elif base.ModeType == 3:
            InfiniteTestMode()
                

if __name__ == '__main__':
    main()