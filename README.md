# One-Time Scannable Entry Pass Generator

A Django web application that generates QR-code entry passes for event registrations. Each pass can be scanned and validated at the event entrance.

## Features
- User registration for events
- Registration approval
- QR-code pass generation
- Unique ID for each entry pass
- Pass validation through scanning
- Prevents reuse of an already-used pass
- Email notification with pass details

## Technologies Used
- Python
- Django
- SQLite
- HTML
- Bootstrap
- QR Code Generation
- SMTP Email

## How It Works
1. A user registers for an event.
2. The administrator approves the registration.
3. An entry pass with a unique QR code is generated.
4. The QR code is scanned to validate the pass.
5. Once used, the pass cannot be used again.

## Run Locally
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Note
This project was built for learning Django, database operations, QR-code generation, and email integration.

