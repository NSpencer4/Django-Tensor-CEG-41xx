Requested for the Code Freeze Checkpoint

# Group-4110 SeeFood Project

**Team Members Of Group 5:**
Chase Spencer, Alyssa Carpenter, Sam Stevens, Joe Dobrovolc

**File Navigation For The Grader:**
This is a Django project (https://www.djangoproject.com/). We cannot split the code into a server and a client directory
without MAJOR rework of how this platform works. Instead, I have identified the server side and client side below.

**Server-side**
1. seefood/Media/uploads: This is where we store images to be used with TensorFlow.
2. seefood/Media/migrations: This is where our database migrations live.
3. seefood/Media/saved_model: This is where we store the TensorFlow models.
4. seefood/Media/views.py: This is where we make handle data, interact with the database, and call the findfood API.
5. seefood/Media/find_food.py: This is where the findfood API is located.
6. seefood/Media/urls.py: This is where we define our routes for our API.
7. seefood/Media/models.py: This is where we define what needs stored in the database.
8. seefood/manage.py: This is used for running the server, performing migrations and much more.


**Client-side**
1. seefood/Media/static: This is where our css and our npm installed external libraries live.
2. seefood/seefood/templates: This is where you will find out base templates as well as our navigation as well as
registration templates.
3. seefood/Media/templates: This is where you will find all of the templates used for the body of our views.