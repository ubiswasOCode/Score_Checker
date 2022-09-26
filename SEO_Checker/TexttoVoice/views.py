from django.shortcuts import render

# Create your views here.
def TexttoVoice(request):
    if request.method == "POST": 
        word=request.POST.get('word')
        main_str=str(word)
        print(main_str)
    
    return render(request, "voice.html")
