from __future__ import unicode_literals

from django.db import models
from account_app.models import EmailBasedUser

class InterviewQA(models.Model):
    """
    Interview Questions and Answers
    """
    LEVELCHOICE = (
        ('SAV', 'SAVVY'), # SYNEIDHTOPOIHMENOS
        ('PRO', 'PROFICIENT'), # PSAGMENOS
        ('EXP', 'EXPERT'), # PANETOIMOS
    )

    level = models.CharField(max_length=3, choices=LEVELCHOICE)
    question_num = models.IntegerField()
    question_text = models.TextField(max_length=1000)
    evaluated_skills = models.CharField(max_length=255)
    # answer part
    answer_advice = models.TextField(max_length=1000, blank=True)
    answer_pro_tip = models.TextField(max_length=1000, blank=True)
    answer_example = models.TextField(max_length=1000, blank=True)
    # specialist data
    specialist_full_name = models.CharField(max_length=255, blank = True)
    specialist_position = models.CharField(max_length=255, blank = True)
    specialist_company = models.CharField(max_length=255, blank = True)
    specialist_avatar = models.ImageField('specialist_avatar', upload_to='static/media/images/avatars/', null=True, blank=True)

    class Meta:
        unique_together = ('level', 'question_num',)

    def __unicode__(self):
        return self.level + ': --- ' + self.question_text


class InterviewAnswer(models.Model):
    """
    The answers that the user gives for the question
    """
    user = models.ForeignKey(EmailBasedUser, null=True)
    interviewQA = models.ForeignKey(InterviewQA, null=True)
    answer = models.TextField(max_length=1000, blank=True)

    class Meta:
        unique_together = ('user', 'interviewQA')

    def __unicode__(self):
        return self.answer