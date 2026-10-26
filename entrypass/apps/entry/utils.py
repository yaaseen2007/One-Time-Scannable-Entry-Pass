import os
import qrcode
from django.conf import settings
from django.core.mail import send_mail

def generate_qr_code(unique_id,user):
    qr_code_dir = os.path.join(settings.MEDIA_ROOT, 'qr_codes')

    if not os.path.exists(qr_code_dir):
        os.makedirs(qr_code_dir)

    file_path = os.path.join(qr_code_dir, f"{unique_id}.png")

    qrcode.make(f"http://127.0.0.1:8000/entry/validate/{user.unique_id}").save(file_path)

    return file_path


def mail(user):
    email_subject = "Your Event Entry Pass Details"
    email_message = (
        f"Hello {user.name}\n\n"
        f"Your Registration has been approved! Here is the link to your pass\n\n"
        f"http://127.0.0.1:8000/entry/pass_detail/{user.unique_id}\n\n"
        f"Thank you for registering for our event!\n\n"
        f"Best regards,\nEvent Team."
    )

    send_mail(
        subject = email_subject,
        message = email_message,
        from_email= settings.DEFAULT_FROM_EMAIL,
        recipient_list= [user.email]


    )




