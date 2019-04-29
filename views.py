from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request, 'WAM_APP_template_2/demo.html')
