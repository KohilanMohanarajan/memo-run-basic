import glob
import random


def file_read():
    file_list = glob.glob('*.txt')
    ind = 1
    file_dict = {}
    while (ind <= len(file_list)):
        file_dict[ind] = file_list[ind - 1]
        ind += 1
    filech = int(input("Choose a file:\n" + str(file_dict) + "\nI choose: "))
    if (filech in file_dict.keys()):
        filehandle = open(file_dict[filech], "r")
        line_list = filehandle.readlines()
        for index in range(0, len(line_list)):
            line_list[index] = line_list[index].strip('\n')
        qulist = line_list
        return qulist


def get_question(qulist):
    lim = len(qulist)
    qchoice = random.randint(1, lim)
    quest = qulist[qchoice - 1]
    quelements = quest.split("///")
    main_question = quelements[0]
    q2elements = quelements[1].split("||")
    answer = q2elements[-1].lstrip()
    options = q2elements[0].split("//")
    finreturn = [main_question, options, answer]
    return finreturn


def play_game(inplist):
    score = 0
    elements = get_question(inplist)
    question = elements[0]
    options = elements[1]
    answer = elements[2]
    qutrue = True
    while (qutrue is True):
        elements = get_question(inplist)
        question = elements[0]
        options = elements[1]
        answer = elements[2]
        print("SCORE: " + str(score))
        if (len(question) > 118):
            numoflines = len(question) // 118
            while(numoflines >= 0):
                par1 = question[:118]
                question = question[118:]
                if (par1[-1] != " " and question[0] != " "):
                    par1 = par1 + "-"
                print(par1)
                numoflines -= 1

        else:
            print(question)
        for index in range(0, len(options)):
            print(options[index])
        usans = input("Your answer: ")
        usans = usans.upper()
        usans = usans.strip()
        if (usans == answer):
            print("CORRECT")
            score += 1
        else:
            print("FALSE")
            print("The Correct Answer was: " + answer)
            qutrue = False
        print("*----------------------------------*")


lister = file_read()
play_game(lister)
