# Some Common Project #2 (SCP #2) - Virtual Queue

## The Idea

Once, I went to the government agency to update my documents, and there were so many people in the queue. If you wanted to enter this queue, you would have to ask some woman who writes down people's names in it. She had just a piece of paper for it.

I think it's more convenient to create a web application for it, so I decided to do it with Django.

My intention is to create this application with Django. I am not going to use front-end frameworks, but, maybe, I will use Celery for some scheduled tasks like notifications about your queue order.

## Something about architecture

I plan to create two main applications:

  - One for the user management
  - One for the queue logic

## What you can do with this app?

There are several points:

  - You can register in the app.
  - You can create a queue.
  - You can enter into the queue.

Future plans:

  - Notifications about your queue order.
  - Notifications about average speed of queue, etc.
