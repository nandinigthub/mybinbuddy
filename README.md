# mybinbuddy

This is an automated waste management system that allowed users to request waste pickup and follow the status of their requests. 

Demo video: https://drive.google.com/file/d/1PF-W8_ltKSfzdtUSast_l8aC1BGrutPA/view?usp=sharing (recommended speed: 1.5x)

Tech stack: Django , GSAP

Process:As we had only 48 hours to complete the project we started working separately on the backend and frontend. On the first day, we decided the structure of the website and divided the tasks. I started working on the backend in which we integrated a message system using Twilio, which will be sent to the registered number. Through Django, we made an authentication system. Frontend was built using HTML, CSS, bootstrap and javascript.

Features includes:
1. login/register
2. create pickup request
3. collection of waste
4. track your request

To run server use following commands:

1. Create a fork
2. git clone https://github.com/nandinigthub/mybinbuddy
3. cd mybinbuddy/wastem
4. python manage.py runserver
