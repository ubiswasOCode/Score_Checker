from django.shortcuts import render
import readtime
import re
from collections import Counter
# Create your views here.

def Word_Count(request):
   
    word=request.GET.get('word')
    main_word=str(word)
    print(word,"-----------------Word is")
    context = dict()
   
    #Calculate Total Word
    context['word_length']=f"total Length is {len(main_word)}"
    
    #Count Total String
    Total_string = main_word.count(" ")+1
    context['Total_word']=f"total word is {(Total_string)}"
    
    
    string = word.lower();  
    #Split the string into words using built-in function  
    words = string.split(" ")
    for i in range(0, len(words)):  
        count = 1
        for j in range(i+1, len(words)):
            if(words[i] == (words[j])):
                count = count + 1 
                #Set words[j] to 0 to avoid printing visited word  
                words[j] = "0";  
                
        #Displays the duplicate word if count is greater than 1  
        if(count > 1 and words[i] != "0"):  
            print(words[i],"-----Repeat item")
            con_list=words[i]
            context["Rep_item"]=f"Repeated item is {(con_list)}"
        else:
            print("Not Repeated Element in the word")
            context["not_rep"]=f"There are not repeated element "
    
    #Calculate Readtime
    read_time=readtime.of_text(word)
    reading_time=read_time.seconds
    print(reading_time,"-------------seconds")
    context['Reading_Time']=f"Word reading time {(reading_time)} Seconds "

    #Counting Heading or Not
    line_count = 0
    list_con=word.split()
    for line in list_con:
        if len(line)<=12:
            pass
    print(line,"----------------it is Heading")
    context["is_Heading"]=f"yes, it is a Heading"
    
    #check Longest Word
    longest=max(word.split(), key=len)
    print(longest,"----------------Longest Word")
   
        
    
    return render(request,"word_count.html",context)