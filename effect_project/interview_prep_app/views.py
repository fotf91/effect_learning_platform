from django.shortcuts import render, redirect, get_object_or_404
from interview_prep_app.models import InterviewQA, InterviewAnswer
from interview_prep_app.forms import InterviewAnswerForm
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from effect_project.generic_view_methods import page_not_found


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'interview_prep_app/index.html', context_dict)

def questions(request, interview_level):
    question_num_int = None
    context_dict = None
    interview_level = interview_level.upper()

    try:
        if request.method == 'POST': # POST : add new answer to a question
            question_id = request.POST.get('interviewQA') # the id of the current question
            current_qa = InterviewQA.objects.get(id=question_id) # the object of the current question, the current object InterviewQA
            form = InterviewAnswerForm(data=request.POST)

            if form.is_valid():
                answer = form.save()

                # check the number of the last answered question
                if current_qa.question_num < 10:
                    # get the number of the next question
                    new_question_num = current_qa.question_num+1
                elif current_qa.question_num == 10:
                    # TODO return final page - the page that sums everything else
                    print '>>>>>>>>>>>>> 10'
                else:
                    return page_not_found(request)

                query_result = InterviewQA.objects.filter(level=current_qa.level, question_num=new_question_num)
                returnedData = serializers.serialize('json', query_result)

                return JsonResponse({'returnedJson': returnedData,})
            else:
                answer = InterviewAnswer()
                return JsonResponse({'returnedJson': 'Invalid Form'})
        else:
            if interview_level == 'PRO' or interview_level == 'SAV' or interview_level == 'EXP':
                if question_num_int is None:
                    question_num_int = 1
                interviewQA = InterviewQA.objects.get(level=interview_level, question_num=question_num_int)

                try:
                    interviewAnswer = InterviewAnswer.objects.filter(user=request.user.id, interviewQA=interviewQA.id)
                except interviewAnswer.DoesNotExist:
                    interviewAnswer = None
                context_dict = {'interviewQA': interviewQA, 'interviewAnswer': interviewAnswer}
            else:
                raise ValueError('Message here....')
        return render(request, 'interview_prep_app/questions.html', context_dict)
    except:
        return page_not_found(request)