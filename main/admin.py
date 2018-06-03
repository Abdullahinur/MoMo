from django.contrib import admin

from .models import (Contact, Conversation, User, User_Options, User_Photo,
                     User_Posts)

# Register your models here.
admin.site.register(User)
admin.site.register(User_Photo)
admin.site.register(User_Posts)
admin.site.register(User_Options)
admin.site.register(Contact)
admin.site.register(Conversation)
