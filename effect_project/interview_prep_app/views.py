from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'interview_prep_app/index.html', context_dict)

def questions(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'interview_prep_app/questions.html', context_dict)