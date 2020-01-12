from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    likes = models.ManyToManyField(User , related_name='likes' , blank=True)
    technology = models.BooleanField(default=False)
    policy = models.BooleanField(default=False)
    sport = models.BooleanField(default=False)
    jobs = models.BooleanField(default=False)
    cars = models.BooleanField(default=False)
    services = models.BooleanField(default=False)
    culture = models.BooleanField(default=False)
    animals = models.BooleanField(default=False)

    def booleans(self):
        type_list =[self.technology , self.policy , self.sport , self.jobs , self.cars , self.services , self.culture , self.animals] # [True , False , True , False , True , True]
        string_type_list = ['technology' , 'policy' , 'sport' , 'jobs' , 'cars' , 'services' , 'culture' , 'animals']
        empty_list = []
        type_count = -1
        for Boll in type_list:
            type_count = type_count + 1
            if Boll == True:
                list_index = string_type_list[type_count]
                empty_list.append(list_index)
        return empty_list      

    def users_liked(self):
        lists = []
        like_list = self.likes.all()
        for x in like_list:
            lists.append(x)
        return lists
                      
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Announcements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Messages(models.Model):
    to_user = models.ForeignKey(User , related_name='to_user' , on_delete=models.CASCADE)
    from_user = models.ForeignKey(User , related_name='from_user' , on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("user-messages" , kwargs={'pk': self.pk})

    
    def who_sent_message(self , pk):
        user_list = []
        users = User.objects.all()
        user = User.objects.get(pk=pk)
        messages = Messages.objects.filter(to_user=user)
        for message in messages:
            if message.from_user:
                user_list.append(message.from_user)
            else:
                pass
        user_list = list( dict.fromkeys(user_list) ) # ----------> Como Remover duplicados!
        return user_list

class FollowRequest(models.Model):
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name="sender_1")
    receiver = models.ForeignKey(User , on_delete=models.CASCADE ,  related_name="receiver_2")
    timestamp = models.DateTimeField(auto_now_add=True)

    def followers_view(self , pk):
        follow_users =  FollowRequest.objects.filter(receiver=pk)
        follow_users_count = FollowRequest.objects.filter(receiver=pk).count()
        return follow_users_count
    
    def following_view(self , pk):
        following_users = FollowRequest.objects.filter(sender=pk)
        following_users_count = FollowRequest.objects.filter(sender=pk).count()
        return following_users_count

    def __str__(self):
        return "{} is following {}".format(self.sender.username , self.receiver.username)

    

    
    
    

    