from django.shortcuts import render
import readtime
import re
from collections import Counter
# Create your views here.

def Word_Count(request):
    context = {"Total_word":0, 'word_length':0 , 'Reading_Time':0, "withoutt_spc":0}
    if request.method == "POST": 
        word=request.POST.get('word')
        main_word=str(word)
        print(word,"-----------------Word is")
        
    
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
        context['Reading_Time']=f" {(reading_time)} "

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
    
    return render(request,"word_count.html",context)