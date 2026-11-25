from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Request, Service
from .forms import RequestForm

def main_view(request):
    return render(request, 'base.html')

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

@login_required
def profile_view(request):
    user_requests = Request.objects.filter(user=request.user)
    return render(request, 'profile.html', {'requests': user_requests})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.status = 0
            req.created_at = timezone.now()
            req.save()
            return redirect('profile')
    else:
        form = RequestForm()
    
    return render(request, 'request_form.html', {'form': form})