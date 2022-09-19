from django.shortcuts import render
import readtime
from collections import Counter
# Create your views here.

def Word_Count(request):
   
    word=request.GET.get('word')
    main_word=str(word)
    print(word)
    context = dict()
   
    #Calculate Total Word
    context['word_length']=f"total Length is {len(main_word)}"
    
    #Count Total String
    Total_string = main_word.count(" ")+1
    context['Total_word']=f"total word is {(Total_string)}"
    
    
    list_1 = main_word.split()
    print(list_1)
    #Calculate Frequencies
    l1=[]
    for i in list_1:
        if i not in l1:
            l1.append(i)
        else:
            print(i,end=' ')
    print(l1,"--------------------list li")
    print(i,"______-item is")
    print(len(i),"----------------length")
   
    #Calculate Readtime
    read_time=readtime.of_text(word)
    reading_time=read_time.seconds
    print(reading_time,"-------------seconds")
    context['Reading_Time']=f"Word reading time {(reading_time)}"
    text_time=word.text
    print(text_time,"---------text time")
    context['text_time']=f"Word Time {(text_time)}"
    
    
    
    
   
        
    
    return render(request,"word_count.html",context)