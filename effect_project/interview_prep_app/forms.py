from django import forms
from interview_prep_app.models import (InterviewAnswer)
# from django.contrib.auth.forms import ReadOnlyPasswordHashField


class InterviewAnswerForm(forms.ModelForm):
    class Meta:
        model = InterviewAnswer
        fields = (
            'user',
            'interviewQA',
            'answer',
        )