import datetime

from django.db import models


# Create your models here.
'''
User class
'''


class User(models.Model):

    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)

    def generate_chat_thread(self):
        counter = 0
        if self.contact_set.all():
            for contact in self.contact_set.all():
                if contact.conversation_set.all():
                    print()
                    print(contact.conversation_set.all().count())
                    counter += contact.conversation_set.all().count()
        return counter

    def generate_contact_thread(self):
        return self.contact_set.all()

    def __str__(self):
        return self.user_name

    def __str__(self):
        return self.user_password

    def __str__(self):
        return self.user_email


'''
User Options things like bio and locale
'''


class User_Options(models.Model):

    user_reference = models.ForeignKey(User, on_delete=models.CASCADE)
    about_bio = models.CharField(max_length=2000)
    about_location = models.CharField(max_length=100)

    def __str__(self):
        return self.about_bio

    def __str__(self):
        return self.about_location

    def __str__(self):
        return self.about_post
