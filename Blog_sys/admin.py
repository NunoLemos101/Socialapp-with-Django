from django.contrib import admin
from .models import Post , Announcements , Messages , FollowRequest

admin.site.register(Post)
admin.site.register(Announcements)
admin.site.register(Messages)
admin.site.register(FollowRequest)