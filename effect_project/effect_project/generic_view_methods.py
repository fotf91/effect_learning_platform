from django.shortcuts import render

def page_not_found(request):
    return render(request, 'general_use_pages/error_page.html', {})