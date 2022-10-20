
from cgitb import text
from fileinput import filename
from django.shortcuts import render
import readtime
import requests
from bs4 import BeautifulSoup
import docx2txt
from PyPDF2 import PdfReader
import re
from collections import Counter


def Word_Count(request):
    word=""
    file=""
    context = {"Total_word":0, 'word_length':0 , 'Reading_Time':0, "withoutt_spc":0,"word":word,"syllable":0,"len_sen":0}


    if request.method == "POST" :


        word=request.POST.get('word')
        if (word):
            context = Word_Check(word)
        else:
            file=(request.FILES['filename'])
            print(file.name,"--------------file")

            if "pdf" in file.name:
                data = PdfType(file)
                context = Word_Check(data)
            elif "doc"  in file.name or "docx"  in file.name:
                worddata=DocxType(file)
                context= Word_Check(worddata)
            else:
                print("nopppeee")





    return render(request,"Word_counter.html",{'context':context,"word":word,"file":file})

def Word_Check(word):
    context = {"Total_word":0, 'word_length':0 , 'Reading_Time':0, "withoutt_spc":0,"syllable":0,"len_sen":0}
    # print(word, "-------------------------jfsdhjdshfjkh")
    main_word=str(word)
    # print(word,"-----------------Word is")

    context['word']=f"{(word)}"

    #Calculate Total Word
    context['word_length']=f"{len(main_word)}"

    #Count Total String
    Total_string = main_word.count(" ")
    context['Total_word']=f"{(Total_string)}"


    string = main_word.lower()
    #Split the string into words using built-in function
    words = string.split(" ")
    for i in range(0, len(words)):
        count = 1
        for j in range(i+1, len(words)):
            if(words[i] == (words[j])):
                count = count + 1
                #Set words[j] to 0 to avoid printing visited word
                words[j] = "0"

            rep=[]
        #Displays the duplicate word if count is greater than 1
            if(count > 1 and words[i] != "0"):
                context["Rep_item"]=f" {(words[i])} "
            else:
                context["Rep-item"]=f"No Repated item "



    ###Check Read Time
    if len(word)>=100 and len(word)<=200:
        context['Reading_Time']=f"1 Min"
    elif len(word)>=200 and len(word)<=250:
            context['Reading_Time']=f"1 Min 3 Sec"
    elif len(word)>=250 and len(word)<=500:
            context['Reading_Time']=f"2 Min 6 Sec"

    #Calculate SpeakTime
    if len(main_word)>=0 and len(main_word)<=80:
        context['SpeakTime']=f"1 Min"
    elif len(main_word)>=80 and len(main_word)<=160:
            context['SpeakTime']=f"2 Min"
    elif len(main_word)>=160 and len(main_word)<=240:
            context['SpeakTime']=f"3 Min"
    elif len(main_word)>=240 and len(word)<=320:
            context['SpeakTime']=f"4 Min"

    #Counting Heading or Not

    list_con=main_word.split()
    for line in list_con:
        if len(line)<=12:
            pass
    print(line,"----------------it is Heading")
    context["is_Heading"]=f"yes, it is a Heading"

    #check Longest Word
    longest=max(main_word.split(), key=len)
    print(longest,"----------------Longest Word")
    context["longest"]=f"{(longest)}"


    #Total Word With Space
    print(len(main_word))

    # or Without Space
    without_space="".join(main_word.split())
    len_without=len(without_space)
    context["withoutt_spc"]=f"{(len_without)}"


    #Syllables Count
    syllable_count=0
    for w in main_word:
        if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u' or w=='A' or w=='E' or w=='I' or w=='O' or w=='U'):
                syllable_count=syllable_count+1
    print("The number of syllables in the word is: ")
    print(syllable_count)
    context["syllable"]=f"{(syllable_count)}"

    #Calculate Sentenses
    import nltk
    nltk.download('punkt')
    from nltk.tokenize import sent_tokenize

    sentences =main_word
    number_of_sentences = sent_tokenize(sentences)

    print(len(number_of_sentences),"-----total sen")
    context["len_sen"]=f"{(len(number_of_sentences))}"


    return context


def PdfType(filename):

    reader = PdfReader(filename)
    print(reader,"------------read")
    number_of_pages = len(reader.pages) ##If Check Number Of Pages
    print(number_of_pages)
    page = reader.pages[0]
    text = page.extract_text()
    # remove=re.sub('\s+',' ',text) ###If Remove Extra Space or line
    print(text)

    return text

def DocxType(filename):

    word_text = docx2txt.process(filename)
    # print(text)
    # remove=re.sub('\s+',' ',text)
    # print(remove)

    return word_text

