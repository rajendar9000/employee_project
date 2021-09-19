from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile(request):
    return render(request, 'profile.html')


def age(request):
    return render(request, 'age.html')

def logout_view(request):
    return render(request, 'logout.html')