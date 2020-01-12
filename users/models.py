from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from Blog_sys.models import FollowRequest , Messages
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    friends = models.ManyToManyField(User , related_name="friendship" , blank=True)

    def followers_view(self):
        follow_users =  FollowRequest.objects.filter(receiver=self.user.id)
        follow_users_count = FollowRequest.objects.filter(receiver=self.user.id).count()
        return follow_users_count
    
    def following_view(self):
        following_users = FollowRequest.objects.filter(sender=self.user.id)
        following_users_count = FollowRequest.objects.filter(sender=self.user.id).count()
        return following_users_count

    def isviewed(self):  
        messages = Messages.objects.filter(to_user=self.user , viewed=False)
        return messages

    def last_message(self):
        l_message = Messages.objects.filter(from_user=self.user)
        x_message = Messages.objects.filter(to_user=self.user)
        add_list = []
        for random_message in l_message:
            add_list.append(random_message.pk)
        for random_message_2 in x_message:
            add_list.append(random_message_2.pk)
        add_list.sort()
        add_list.reverse()
        add_list.reverse()
        
        position = -1
        for order_message in add_list:
            position = position + 1
            message_count = Messages.objects.get(pk=order_message)
            add_list.pop(position)
            add_list.insert(position , message_count)
        
        last_message_index = len(add_list)
        pretended_message = add_list[last_message_index - 1]
        return pretended_message

        
                

    def get_absolute_url(self):
        return reverse("profile-detail" , kwargs={'pk': self.pk})
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
    
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)





