def myFileWordCounter():

    myFileInput = input("Write a file name here! :")

    file = open(myFileInput, 'r+')
    #readLines = file.readlines()

    splitWordsInFile = file.read().split()

    # for i in readLines:
    #     print(i)


    print(len(splitWordsInFile))

    # takeAddedText = input("Write what you want to add here! :")

    multipleLines = [ 'Hello! \n', 'See you later! \n', 'Okay. \n' ]

    file.writelines(multipleLines)

    file = open(myFileInput, 'r')
    readLines = file.readlines()

    for i in readLines:
        print(i)

myFileWordCounter()

