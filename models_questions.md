Questions on Models (Django)
(answered)

1. What does a model’s field type represent? If I use a CharField versus a TextField, for example, what does that change about how the data is stored?
2. What is the difference between the null and blank field options? What do each of them represent?
3. How do we use the TextChoices field type to display multiple options?
4. What is a primary_key field? If we don’t specify a primary key, what is the default?
5. How do we specify a verbose name? What purpose does it serve?
6. In the documentation under “Many-to-one Relationships”, an example is given of “Manufacturer” and “Car” models. Complete the code by adding at least 2 new fields to each model.
7. In the documentation under “Many-to-Many Relationships”, an example is given of “Pizza” and “Topping” models. Complete the code by adding at least 2 new fields to each model.
8. What is an example of a one-to-one relationship? When would we use a OneToOneField?
9. Sometimes we need to relate a model to one from another app. Give an example of an import line to show how we’d import the other model.
10. What is the class Meta? When would we use it?
11. What is an example of a model method? Suppose we have a class Album. What methods might we want to write for it?
12. Give an example of model inheritance. How does inheritance help us to write better code?

Answers 

1. the model's field type tells the database what kind of data to store. CharField would store a small sized string field while TextField would store a large sized string field.

2. the difference between null is that null will be stored as empty values in the database while blank will be left blank in the database.

3. to display multiple options, create a sequence consisting of two items to use as choices for the field.

4. the primary key field is the primary key for the model. if not defined, Django creates a random default key.

5. how to create: ```Field.verbose_name```. purpose: a human-readable name for the field. random.

6. i'm not sure how to do this one.
7. nor this one.

8. one-to-one example: post to user; a user can have a post and a post is written by a user. you would then use OneToOneField to describe the relationship between the parent and child. (positional argument).

9. 
```from django.urls import path```
```from . import views```

10. Meta class is an inner Django class that provides metadata to the model form class. Works same as the "__init__". We would use it when we want to define or change global objects locally.

11. various models are created for different stages of the site. Album: methods >> (__init__, lists, functions).

12. ```django.db.models.Model```. Inheritance helps us write better code by keeping the organization of files neat and easily accessible from anywhere in the app.