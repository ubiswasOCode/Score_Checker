from django.shortcuts import render

# Create your views here.
def ChangeCase(request):
    context=dict()
    
    if request.method == "POST": 
        word=request.POST.get('word')
        main_str=str(word)
        print(main_str)

        lower=main_str.lower()
        print(lower,"Lower")
        context["lower_word"]=f"{(lower)}"
        
        upper=main_str.upper()
        print(upper,"Upper ")
        context["upper_word"]=f"{(upper)}"
        
        togle=main_str.swapcase()
        print(togle,"Toggle")
        context["togle_word"]=f"{(togle)}"
        
        capyl=main_str.capitalize()
        print(capyl,"Captialize")
        context["captl_word"]=f"{(capyl)}"
        
        up_and_down_list = [main_str[i].upper() if i%2==0 else main_str[i].lower() for i in range(len(main_str))]
        my_new_str = ''.join(up_and_down_list)
        alternte=my_new_str
        print(alternte,"Alternate")
        context["up_down_word"]=f"{(alternte)}"
        
    return render(request, "change.html")