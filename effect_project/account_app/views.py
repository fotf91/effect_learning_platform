import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from account_app.forms import (GeneralUserCreationForm,
                               AuthenticationForm,
                               AddPositionForm,
                               EditPositionForm,AvatarGUserForm)
from django.contrib.auth.decorators import login_required
from account_app.models import TypeGUser, TypeCUser, Skills, Position, ExpertiseArea
from account_app.forms import (EditTypeCUserForm,
                               EditTypeGUserForm,
                               )
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'account_app/index.html', context_dict)

class personal_profile_view(View):
    # the user wants to see his own profile
    # and edit it

    template_name = 'account_app/personal_profile.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        avatar_path = None

        if current_user.user_type == 1:
            try:
                current_user_detail = TypeGUser.objects.get(user=current_user)
                if current_user_detail.avatar:
                    avatar_path = '/' + current_user_detail.avatar.url
            except TypeGUser.DoesNotExist:
                current_user_detail = None
        elif current_user.user_type == 2:
            try:
                current_user_detail = TypeCUser.objects.get(user=current_user)
                if current_user_detail.avatar:
                    avatar_path = '/'+current_user_detail.avatar.url
            except TypeGUser.DoesNotExist:
                current_user_detail = None
        context_dict = {}

        if current_user.user_type == 1 or current_user.user_type == 2:
            try:
                positions = Position.objects.filter(user=current_user).order_by('-end_date')
            except Position.DoesNotExist:
                positions = []

        print ('>>>>>>>>',avatar_path)

        context_dict = {'current_user': current_user,
                        'current_user_detail': current_user_detail,
                        'positions': positions,
                        'avatar_path': avatar_path,
                        }
        return render(request, 'account_app/personal_profile.html', context_dict)

    @login_required
    def post(self, request, *args, **kwargs):
        current_user = request.user
        current_user_detail = TypeGUser.objects.get(user=current_user)

        if request.method == 'POST':
            input_data = json.loads(request.body)
            form = EditTypeGUserForm(input_data, instance=current_user_detail)
            if form.is_valid():
                print('valid form')
                form.save()
            else:
                print('invalid form')
                print(form.errors)
        return render(request, 'account_app/personal_profile.html', {'form': form}, )

def update_avatar_GType(request):
    current_user = request.user
    try:
        current_user_detail = TypeGUser.objects.get(user=current_user)
        if request.method == 'POST':
            form = AvatarGUserForm(request.POST, request.FILES, instance=current_user_detail)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/account/profile')
            else:
                form = EditTypeGUserForm()
        return render(request, 'account_app/personal_profile.html',{'form':form})
    except TypeGUser.DoesNotExist:
        return HttpResponse('Failure during profile update')


@login_required
def personal_profile(request):
    """
    Connected User Profile
    """
    current_user = request.user # get the currently connected user
    avatar_path = None # initialize empty variable

    if current_user.user_type == 1:
        try:
            current_user_detail = TypeGUser.objects.get(user=current_user)
            if current_user_detail.avatar:
                avatar_path = '/'+current_user_detail.avatar.url
        except TypeGUser.DoesNotExist:
            current_user_detail = None
    elif current_user.user_type == 2:
        try:
            current_user_detail = TypeCUser.objects.get(user=current_user)
            if current_user_detail.avatar:
                avatar_path = '/'+current_user_detail.avatar.url
        except TypeGUser.DoesNotExist:
            current_user_detail = None

    if current_user.user_type == 1 or current_user.user_type == 2:
        try:
            positions = Position.objects.filter(user=current_user).order_by('-end_date')
        except Position.DoesNotExist:
            positions = []

    context_dict = {'current_user': current_user,
                    'current_user_detail': current_user_detail,
                    'positions': positions,
                    'avatar_path':avatar_path,
                    }
    return render(request, 'account_app/personal_profile.html', context_dict)



@login_required
def update_profile_Ctype(request):
    """
    Update the profile of a user type C
    """
    current_user = request.user
    try:
        current_user_detail = TypeCUser.objects.get(user=current_user)
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = EditTypeCUserForm(request.POST, request.FILES, instance=current_user_detail)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/account/profile')
            # if a GET (or any other method) we'll create a blank form
            else:
                # raise invalidFormException()
                form = EditTypeCUserForm()
        return render(request,
                    'account_app/personal_profile.html',
                    {'form':form} # context dictionary
                    )
    except TypeCUser.DoesNotExist:
        return HttpResponse('Failure during profile update')

@login_required
def update_profile_Gtype(request):
    """
    Update the profile of a user type G
    """
    print('>>>>>>>')
    current_user = request.user
    try:
        print('>>>>>>>>>>> try')
        current_user_detail = TypeGUser.objects.get(user=current_user)
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            print('>>>>>>>>> if post')
            form = EditTypeGUserForm(request.POST, instance=current_user_detail)
            if form.is_valid():
                print ('>>>>>>>>>> if valid')
                form.save()
                return HttpResponseRedirect('/account/profile')
            # if a GET (or any other method) we'll create a blank form
            else:
                print('>>>>>>>>>> else not valid')
                print (form.errors)
                form = EditTypeGUserForm()
                # TODO
                # STAY ON THE SAME PAGE, DO NOT GO TO THE FOLLOWING RETURN
                # AND SHOW THE ERROR MESSAGES
        return render(request,
                    'account_app/personal_profile.html',
                    {'form':form} # context dictionary
                    )
    except TypeCUser.DoesNotExist:
        return HttpResponse('Failure during profile update')

def login(request):
    """
    Login view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect('/account/')
                else:
                    return HttpResponse("Your account is disabled.")
            else:
                return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'account_app/login.html', {})


def register(request):
    """
    Registration view
    """
    registered = False
    if request.method == 'POST':
        form = GeneralUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered_user_type = form.cleaned_data['user_type']

            # temporary solution
            if registered_user_type == '1':
                newGUser = TypeGUser(user=user)
                newGUser.user_type = '1'
                newGUser.save()
            else:
                pass
                user.delete()

            # later solution
            # if registered_user_type == '1':
            #     newGUser = TypeGUser(user=user)
            #     newGUser.save()
            # elif registered_user_type == '2':
            #     newCUser = TypeCUser(user=user)
            #     newCUser.save()
            # else:
            #     user.delete()
            registered = True
    else:
        form = GeneralUserCreationForm()
    return render(request,
                  'account_app/connect.html',
                  {'form': form, 'registered': registered})


def logout(request):
    """
    Logout view
    """
    django_logout(request)
    return redirect('/account')

def get_expertise_area_list(request):
    """
    Return a list of expertise area according to the string the user has entered
    """
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['exp_area_query']

    if starts_with != '':
        exp_area_list = ExpertiseArea.objects.filter(name__istartswith=starts_with)
    else:
        exp_area_list = []

    returnData = serializers.serialize('json',exp_area_list)
    return JsonResponse({'areas': returnData})

def get_skill_list(request):
    """
    Return a list of skills according to the string the user has entered
    """
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['skill_query']

    if starts_with != '':
        skill_list = Skills.objects.filter(name__istartswith=starts_with)
    else:
        skill_list = []

    returnData = serializers.serialize("json", skill_list)
    return JsonResponse({'skills': returnData})

# def get_skills_id(request):
#     """
#     Return the id of all the skills that the user has already
#     """
#     if request.method == 'GET':
#         skill = request.GET['skills_owned']
#         query_result = Skills.objects.filter(name=skill)
#     else:
#         skill_data = {}
#     returnData = serializers.serialize('json', query_result)
#     return JsonResponse({'skill': returnData})

def add_position(request):
    """
    Add a past or present position to a user
    """
    print('>>>>>>>>>>')
    # get the number of positions that the current user has
    positions = Position.objects.filter(user=request.user)

    if request.method == 'POST' and positions.count() < 3:
        form = AddPositionForm(data=request.POST)
        if form.is_valid:
            position = form.save()
            positions = Position.objects.filter(user=request.user).order_by('-end_date')
        else:
            form = AddPositionForm()
        returnData = serializers.serialize('json', positions)
        return JsonResponse({'returnedJson': returnData})
    else:
        form = AddPositionForm()
        return render(request, 'account_app/personal_profile.html', {'form': form}, )

# def edit_position(request):
#     """
#     Edit a past or present position to a user
#     """
#     position_id = request.POST.get('id')
#     current_position = Position.objects.get(id=position_id)
#
#     if request.method == 'POST':
#         form = EditPositionForm(request.POST, instance=current_position)
#
#         if form.is_valid:
#             form.save()
#             positions = Position.objects.filter(user=request.user).order_by('end_date')
#         else:
#             form = EditPositionForm()
#         returnData = serializers.serialize('json', positions)
#         return JsonResponse({'returnedJson': returnData})
#     else:
#         form = EditPositionForm()
#         return render(request, 'account_app/personal_profile.html', {'form': form}, )

# def delete_position(request):
#     position_id = request.POST.get('id')
#     current_position = Position.objects.get(id=position_id)
#
#     if request.method == 'POST':
#         current_position.delete()
#         return HttpResponse(json.dumps({'id' : position_id,}))
#     else:
#         return HttpResponse(json.dumps({'id': -1}))
