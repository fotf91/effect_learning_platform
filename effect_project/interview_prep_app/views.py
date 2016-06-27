from django.shortcuts import render, redirect, get_object_or_404
from interview_prep_app.models import InterviewQA, InterviewAnswer
from interview_prep_app.forms import InterviewAnswerForm
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from effect_project.generic_view_methods import page_not_found
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'interview_prep_app/index.html', context_dict)

@login_required
def questions(request, interview_level, question_num):
    """
    render the requested question and data

    :param request:
    :param interview_level: the level of the interview
    :param question_num: the question of the current level of the interview
    :return:
    """
    question_num_int = int(question_num)
    interview_level = interview_level.upper()
    context_dict = None
    interviewQA = None
    interviewAnswer = None

    # POST: save answer for the question
    if request.method == 'POST':
        question_id = request.POST.get('interviewQA')  # the id of the current question
        current_qa = InterviewQA.objects.get(id=question_id)  # the object of the current question, the current object InterviewQA

        # prepare the object to save, an old object or one that already exists
        form = None
        try:
            interviewAnswer = InterviewAnswer.objects.get(user=request.user.id, interviewQA=current_qa.id)
            form = InterviewAnswerForm(request.POST, instance=interviewAnswer)
        except InterviewAnswer.DoesNotExist:
            form = InterviewAnswerForm(request.POST)

        if form.is_valid():
            # create or update the InterviewAnswer object for the given InterviewQA object
            answer = form.save()
        else:
            print (form.errors)
    # get the page according to the URL
    elif interview_level == 'PRO' or interview_level == 'SAV' or interview_level == 'EXP':
        if question_num_int == 1:
            try:
                interviewQA = InterviewQA.objects.get(level=interview_level, question_num=question_num_int)
                interviewAnswer = InterviewAnswer.objects.get(user=request.user.id, interviewQA=interviewQA.id)
            except InterviewQA.DoesNotExist:
                interviewQA = None
            except InterviewAnswer.DoesNotExist:
                interviewAnswer = None
            context_dict = {'interviewQA': interviewQA, 'interviewAnswer': interviewAnswer}
        elif question_num_int > 1 and question_num_int < 11:
            try:
                # if the user has answered the previous question
                previous_question_num_int = question_num_int-1
                previousQA = InterviewQA.objects.get(level=interview_level, question_num=previous_question_num_int)
                try:
                    InterviewAnswer.objects.get(user=request.user.id, interviewQA=previousQA.id)
                except InterviewAnswer.DoesNotExist:
                    return previous_question_error(request)
                    # return redirect('questions', interview_level=interview_level.lower(), question_num=question_num_int)
                # # redirect to the page with the requested question
                interviewQA = InterviewQA.objects.get(level=interview_level, question_num=question_num_int)
                interviewAnswer = InterviewAnswer.objects.get(user=request.user.id, interviewQA=interviewQA.id)
            except InterviewAnswer.DoesNotExist:
                interviewAnswer = None
            context_dict = {'interviewQA': interviewQA, 'interviewAnswer': interviewAnswer}
        else:
            return page_not_found(request)
    return render(request, 'interview_prep_app/questions.html', context_dict)

@login_required
def previous_question_error(request):
    return render(request, 'interview_prep_app/previous_question_error.html', {})

@login_required
def summary(request, interview_level):
    """
    render the summary of the interview page

    :param request:
    :return context_dictionary: with the data of the questions and answers
    """
    interview_level = interview_level.upper()
    user = request.user.id

    if interview_level == 'PRO' or interview_level == 'SAV' or interview_level == 'EXP':
        summary_data = InterviewAnswer.objects.filter(user = request.user.id, interviewQA__level = interview_level)\
            .values('interviewQA__question_text', 'interviewQA__question_num', 'answer')

    context_dict = {'summary_data': summary_data}
    return render(request, 'interview_prep_app/summary.html', context_dict)
