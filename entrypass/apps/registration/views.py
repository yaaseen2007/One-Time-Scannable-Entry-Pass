from django.shortcuts import render, redirect
from .models import Registration
import uuid
# Create your views here.

def register(request):
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        name = request.POST.get('name')
        email = request.POST.get('email')

        Registration.objects.create(
            rollno = rollno,
            name = name,
            email = email,
            unique_id = uuid.uuid4().hex
        )

        return redirect('thankyou')
        
    return render(request, 'registration/register.html')


def thank_you(request):
    return render(request, 'registration/thankyou.html')

def pending_users(request):
    users = Registration.objects.filter(status='Pending')
    return render(request, 'registration/pendingusers.html', {'users':users})