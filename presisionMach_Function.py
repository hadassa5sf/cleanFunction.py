import pandas as pd
import numpy as np
import math
import xlsxwriter as xlsw
"""
CHANGING ROW AND COLON AND WORK WITH DATAFRAME - VERY GOOD SITE:
https://www.askpython.com/python-modules/pandas/update-the-value-of-a-row-dataframe

ADDING NEW LIST TO A DATAFRAME

import pandas as pd
info= {"Num":[], "NAME":[], "GRAD":[]}
data = pd.DataFrame()
print("Original Data frame:\n")
print(data)
#SYNTAX: dataframe.at[index,'column-name']='new value'
data.at[0,'NAME']='Safa'
data.at[0,'GRAD']=90
data.at[1,{'NAME','GRAD'}]=50, 'Hadassa'
print("new Data frame:\n")
print(data)

"""

""""
    help function
"""
def is_letter(row):
    """
    check if the all row is only caracters
    :param row:
    :return: true if there are a number
    """
    for n in row:
        if n.isalpha()==False:
            return True
    return False

def list_contains(data, testing):
    """
    check match between two lists
    :param data: line from excel
    :param testing: xRow testing
    :return: the number of same latter in order start to end, not have to be consecutive
    """

    t = 0#index for testing
    count = 0#count how match good latter
    type_g = "A"#each move latter move to the secand latter
    secont = False #for case that we begine fron the secont true number fron the vin excel
    for s in range(len(testing)-1):#find the first letter in the test barcod that is similar to the true vin
        if data[0] == testing[s]:
            t=s#from there continue to check for not have stop in the start of the list
            break
        if data[1] == testing[s+1]:#if we have a mistake in the first latter to start to check from the secend one
            t=s+1#from there continue to check for not have stop in the start of the list
            secont = True
            break

    for i in range(len(data)):#check in the true vin, if there are other same latter if YES Advance the test list also
        #if we begain from the secent number vin
        if secont==True:
            i = 1 # be sure that we begin from the second latter
            secont = False # for do this law only one time

       #if there are a latter in the middel of the vin scip it
        if testing[t].isalpha() == True:
            t = t+1
            i = i+1
            if t == len(testing):
                break
            if i == len(data):
                break
        #if we begane from the first number vin or after update the "secont case"
        if data[i] == testing[t]:
            count = count + 1
            """
            #find the Type
            if t-i==1:
                type_g = 'B'
            elif t-i==2:
                type_g = 'C'
            elif t - i > 2:
                type_g = 'bad'
            """

            t = t+1
            if t == len(testing):
                break
            if i == len(data):
                break
    return count#, type_g

            # Python program to Split string into characters

def split(word):
    return [char for char in word]

def get6final(vincolon,fullVINashdod , trueVIN_6latter):
    """
    get from the Ashdod the kast 6 latter with out space
    :param vincolon:the all data_Excel
    :return: a list of string
    """
    for index, row in vincolon.iterrows():
        a = str(row['שילדה'])
        #print("The full VIN:",a)
        a_vin = []
        count = 6
        #print(type(row['שילדה']) )
        fullVINashdod.append(a)
        for i in range(len(a)-1, -1, -1):
            if count == 0:# we get 6 last vin number
                break
            if a[i] != ' ':
                a_vin.append(a[i])
                count = count - 1
        a_vin.reverse()
        #print(a_vin)
        trueVIN_6latter.append(a_vin)

def smallerList(list):
    """
    if there are no match small the list if it is big then len(list)>7
    :param vincolon:a test list
    :return: a small list
    """
    count = 6
    small_list = []
    for i in range(len(list)-1, -1, -1):
        if count == 0:# we get 6 last vin number
            break

        small_list.append(list[i])
        count = count - 1
    small_list.reverse()
    return small_list

def charExsisted(char, char_list):
    """
    check if a char already exsist in the charlist
    :return: the list
    """
    for c in char_list:
        if c == char:
            return char_list
    char_list.append(char)
    return char_list

def last_8_latter(listfullVin):
    """
    to fine the possible character in place -6 and -7 in the full vin
    :param vincolon:a test list
    :return: a small list
    """
    count = 8
    charList_6 = []
    charList_7 = []
    for row in listfullVin:
        #for not full vin continue
        if len(row)<17:continue
        #save the -6 vin place
        if row[12].isalpha():
            charList_6 = charExsisted(row[12],charList_6)
        # save the -7 vin place
        if row[11].isalpha():
            charList_7 = charExsisted(row[11],charList_7)

    return charList_6, charList_7

def adapted(fullVINashdod , xRow):
    charList_6, charList_7 = last_8_latter(fullVINashdod)
    #chack if the last char are number and the len row is between 14-17 or 3-6
    if xRow[-1].isalpha()!=True:
        if 14<=len(xRow)<17:
            miss = 17-len(xRow)
            for i in range(miss):xRow.append('&')
            print(xRow)
        elif 3<=len(xRow)<6:
            miss = 6 - len(xRow)
            for i in range(miss):xRow.append('&')
            print(xRow)



    #if the first vin is a latter
    if xRow[0].isalpha():
        goodChar = False
        #if she is part of the posible start vin latter
        for char in charList_6:
            if char == xRow[0]:
                goodChar = True
                break
        #if it is not a good start latter, it is a false read
        if goodChar == False:
            y=8
            #change


"""
    work steps
"""
def firstUpdate(ashdodExcel):
    """
    read the ashdod excel and create the data frame resault
    :param ashdodExcel:
    :return: a empty data frame
    """
    fullVINashdod = []
    trueVIN_6latter = []
    dataAshdod = pd.read_excel(ashdodExcel)  # "ashdod_4_3_21.xlsx"
    get6final(dataAshdod ,fullVINashdod , trueVIN_6latter)
    info = {"Camera Name":[], "Test Vin From Image":[], "index from excel":[], "Potential vin from excel":[], "Grade":[], "Type":[]}
    df_resaulte = pd.DataFrame(info)
    return df_resaulte, fullVINashdod, trueVIN_6latter


def AddNewRow(df,df_index,cameraName, vinFromImage, indexExcel, vinFromExcel, Grade , Type):
    """
    function that add a new row to the data frame
    :return: the update data frame and the index for the next row
    """
    # SYNTAX: dataframe.at[index,'column-name']='new value', list of value as to be in a revers order
    df.at[df_index, "Camera Name"] = cameraName
    df.at[df_index, "Test Vin From Image"] = vinFromImage
    df.at[df_index, "index from excel"] = indexExcel
    df.at[df_index, "Potential vin from excel"] = vinFromExcel
    df.at[df_index, "Grade"] = Grade
    df.at[df_index, "Type"] = Type
    #df.at[df_index, {"Camera Name", "Test Vin From Image", "index from excel", "Potential vin from excel", "Grade" , "Type"}] =Type, Grade, vinFromExcel,indexExcel,vinFromImage,cameraName
    df_index = df_index+1
    return df, df_index

def checkTextRow(fullVINashdod, name_cam, trueVIN_6latter, xRow , resaultDataframe, df_index):
    """
    get the row and chack:
        * there are number on it
        * check if this txt row is cut or have a big error
        * did thise txt fixed row are matching to an excel line
        * give a weight to different potencial excel rows with similar grad
    :param xRow:
    :return:resaultDataframe (-update one),df_index(-for continuse write in) , [xRow,best_i_excel,bestVin] (-for save the best resault)
    """

    ###two side range case
    #save the best resault
    bestGrad = 0
    #flage for no vin row
    noVin_row = True

    best_i_excel = None
    bestVin = None

    j = 1
    #for all the true excel compere to single test line from barcod
    for trueL in trueVIN_6latter:
            j = j + 1

            number = list_contains(trueL, xRow)
            #if there are more then 3 samilare from 6 letter - save it as a potencial
            if number>3:
                noVin_row = False
                print(trueL,"number " ,number )#, "type grade:",type_g)
                temp = (number*100)/6
                print("grad:",temp)
                # save the all parameter
                #AddNewRow(resaultDataframe, df_index, name_cam, xRow, j, trueL, temp, 'A')
                df_index = df_index+1


                if temp >= bestGrad:# and Type=='A':
                    bestVin = trueL
                    best_i_excel = j
                    bestGrad = temp

    if noVin_row == True:
        best_i_excel = None
        bestVin = 'No VIN row'

    return resaultDataframe, df_index , [xRow,best_i_excel,bestVin,bestGrad]


def PrecisionMach(fullVINashdod, trueVIN_6latter ,googleText ,resaultDataframe ):
    """
    get a line from the txt file and send it to check vin
    only if it is not start or end, and containe number on it
    :param ashdodlist:
    :param googleText:
    :param resaultDataframe:
    :return:
    """

    run_df_index = 0
    save_best_resault = []

    #open the .txt google file resault
    f = open(googleText, "r") # ("tester.txt", "r")
    for x in f:
        # find the first and end line for each image
        #if x == '\n':
            #print("Finish this image")
            #print("\n-------------------------------------------\n")
            #break

        #scip notusfull lines
        if x == '\n' or x == 'Output:':continue
        if 'Image name:' in x:
            name_cam = x.split(':')[1].split('\n')[0]
            print("start ",name_cam," image:")
            continue
        #if the all text no containe any vin
        if 'Time estimate' in x:
            print("Finish this image")
            print("\n-------------------------------------------\n")
            continue

        xArr = split(x)
        xArr.remove('\n')

        # chack that the row is not cut, if it is cut add the sine &
        adapted(fullVINashdod, xArr)

        # if there are number
        if is_letter(xArr) and len(xArr) > 7:
            xArr = smallerList(xArr)
            resaultDataframe, run_df_index , [xRow,best_i_excel,bestVin,bestGrad] = checkTextRow(fullVINashdod,name_cam, trueVIN_6latter, xArr, resaultDataframe, run_df_index)
            save_best_resault.append([xRow,best_i_excel,bestVin,bestGrad])


    return save_best_resault, resaultDataframe




#read the Excel and creat the dataFrame ans
df_resaulte, fullVINashdod, trueVIN_6latter = firstUpdate('ashdod_4_3_21.xlsx')
save_best_resault, df_resaulte = PrecisionMach(fullVINashdod, trueVIN_6latter , 'run1.txt', df_resaulte)
for ob in save_best_resault:
    print(ob)






