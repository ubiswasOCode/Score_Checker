
from cgitb import text
from fileinput import filename
from django.shortcuts import render
import readtime
import requests
import spacy
import textacy
from bs4 import BeautifulSoup
import docx2txt
from PyPDF2 import PdfReader
import re
from collections import Counter


def Word_Count(request):
    word=""
    print(word,"--------------word")
    file=""
    context = {"Total_word":0, 'word_length':0 , 'Reading_Time':0, "withoutt_spc":0,'Rep_item':0 ,'longest':0 ,"word":word,"syllable":0,"len_sen":0,"Phrases":0,"verbs":0}


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
        print(context, "fdsfdsf")


    return render(request,"Word_counter.html",{'context':context,"file":file})

def Word_Check(word):
    context = {"Total_word":0, 'word_length':0 ,'Total_word':0 ,'word_length':0 , 'Reading_Time':0, "withoutt_spc":0, "word":word, "syllable":0,"len_sen":0}
    main_word=str(word)
    context['word']=word

    #Calculate Total Word
    context['word_length']=f"{len(main_word)}"

    #Count Total String
    Total_string = main_word.count(" ")+1
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


        #Displays the duplicate word if count is greater than 1
            if(count > 1 and words[i] != "0"):
                context["Rep_item"]=f" {(words[i])}"
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

    context["is_Heading"]=f"yes, it is a Heading"

    #check Longest Word
    longest=max(main_word.split(),default=0, key=len)
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
    context["syllable"]=f"{(syllable_count)}"

    #Calculate Sentenses
    import nltk
    nltk.download('punkt')
    from nltk.tokenize import sent_tokenize

    sentences =main_word
    number_of_sentences = sent_tokenize(sentences)
    context["len_sen"]=f"{(len(number_of_sentences))}"

    ###-----------------P
    nlp = spacy.load("en_core_web_sm")
    Phrases_text=nlp(main_word)
    total_phra=[chunk.text for chunk in Phrases_text.noun_chunks]
    context["Phrases"]=" , " .join(total_phra)
    all_verb=[token.lemma_ for token in Phrases_text if token.pos_ == "VERB"]
    context["verbs"]=" , ".join(all_verb)


    return context


def PdfType(filename):

    reader = PdfReader(filename)
    number_of_pages = len(reader.pages) ##If Check Number Of Pages
    page = reader.pages[0]
    text = page.extract_text()
    # remove=re.sub('\s+',' ',text) ###If Remove Extra Space or line

    return text

def DocxType(filename):

    word_text = docx2txt.process(filename)
    # print(text)
    # remove=re.sub('\s+',' ',text)
    # print(remove)

    return word_text

