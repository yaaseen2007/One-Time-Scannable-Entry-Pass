from django.shortcuts import render, redirect
from apps.registration.models import Registration
from .utils import generate_qr_code, mail
from .models import EntryPass
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
def approve_registration(request, unique_id):
    user = Registration.objects.filter(unique_id=unique_id).first()

    qr_code = generate_qr_code(unique_id, user) 
    mail(user)

    EntryPass.objects.create(
        name = user,
        event_name = "Gaming",
        qr_code = qr_code,
        unique_id = user.unique_id

    )

    user.status = 'Approved'
    user.save()



    return redirect('pendingusers')

def pass_detail(request, unique_id):
    entry_pass = EntryPass.objects.filter(unique_id=unique_id).first()
    return render(request, 'pass/passdetail.html', {'entry_pass':entry_pass})

@login_required
def validate(request, unique_id):
    entry_pass = EntryPass.objects.filter(unique_id=unique_id).first()

    if entry_pass.is_used:
        return render(request, 'pass/invalid.html')
    else:
        entry_pass.is_used = True
        entry_pass.save()
        return render(request, 'pass/valid.html')