# SDS: online quiz platform

A Django web app for running class quizzes, with separate logins for teachers and students. Teachers add questions and schedule tests, and the app emails every student when a test is set. Students take timed, randomised 10-question tests in Data Structures, Java and Software Engineering, and see their score straight away next to the class average. Questions, users and results are stored in SQLite.

Built in 2023. The Django admin calls it the "Student Diagnostic System".

## Features

**Teachers** (`/signupteacher`, `/loginteacher`, `/teacher`)
- Add questions to the bank: subject, topic, four options, the correct answer and a difficulty level (`/addQuestion`).
- Schedule a test for a subject and date (`/setTest`). Every registered student gets an email about it.

**Students** (`/signupstudent`, `/loginstudent`, `/student`)
- See which tests are scheduled for today (`/quiz`) and the full schedule (`/schedule`).
- Take a test (`/DSA`, `/JAVA`, `/SE`): 10 questions drawn at random from that subject's bank, with an on-page timer.
- Get the result immediately: score, correct and wrong counts, percentage, time taken, and the class average for that subject.
- Practise with self-paced quizzes (plain JavaScript, under `static/DSA`, `static/JAVA` and `static/FSE`).

**Question bank:** 82 questions in the database for scheduled tests (21 Data Structures, 31 Java, 30 Software Engineering), plus 110 in the practice sets.

Each sign-up also sends a welcome email.

## Stack

Python, Django 4.1, SQLite, Django auth, Django email (SMTP), HTML/CSS/JavaScript, Bootstrap.

## Run it

```bash
cd hello
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver --insecure
```

Open http://127.0.0.1:8000. `DEBUG` is off in `hello/settings.py`, so `--insecure` is what lets the dev server serve the CSS and images. Sign up as a teacher, add questions or schedule a test, then sign up as a student to take it.

Email settings are read from `hello/info.py`. Mail is sent with `fail_silently=True`, so the app still works without valid SMTP credentials; it just doesn't send email.

## Project structure

```
hello/
├── hello/              settings, URLs, email config (info.py)
├── home/
│   ├── models.py       questions, test (schedule), result, student/teacher profiles, contact
│   └── views.py        sign-up/login, question entry, scheduling, test-taking and scoring
├── templates/          student/ and teacher/ dashboards, test and result pages
└── static/             CSS, images and the JavaScript practice quizzes
```

## Known issue: scoring re-draws the questions

When a test is submitted, the subject view (for example `DSA` in `home/views.py`) draws a new random set of 10 questions and scores the answers against that set instead of the questions the student saw. Answers to questions that weren't re-drawn count as wrong, so scores come out lower than they should. The fix is to grade the submitted questions themselves, by sending each question's id with the form and looking those up on submit.
