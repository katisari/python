# in models.py
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    



#in terminal
# 1. Know how to retrieve all users.
User.objects.all()
# 2. Know how to get the last user.
User.objects.last()
# 3. Create a few records in the users
User.objects.create(first_name='Bob', last_name='Smith', email_address='hello@gmail.com', age=13)
User.objects.create(first_name='Hello', last_name='World', email_address='hello_world@gmail.com', age=13)
# 4. Know how to get the first user.
User.objects.first()
# 5. Know how to get the users sorted by their first name (order by first_name DESC)
User.objects.order_by('first_name')
# 6. Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
b=User.objects.get(id=3)
b.last_name="YES"
b.save()
# 7. Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
b = User.objects.get(id=4)
b.delete()
