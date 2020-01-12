from django.contrib import admin
from django.urls import path
from . import views
from .views import PostCreateView , PostUpdateView , PostDeleteView , MyPostsListView  , UserPostListView , AnnouncementsListView

urlpatterns = [
    path('' , views.PostHomeView , name='blog-home'),    
    path('announcements/' , AnnouncementsListView.as_view() , name='blog-announcements'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('profile/<int:pk>/' , views.ProfileView , name='profile-detail'),
    #path('post/<int:pk>/' , PostDetailView.as_view() , name='post-detail'),
    path('post/<int:pk>/update/' , PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/' , PostDeleteView.as_view() , name='post-delete'),
    path('post/new/' , PostCreateView.as_view() , name='post-create'),
    path('post/myposts/' , MyPostsListView.as_view() , name='post-my_posts'),
    path('all_profiles/' , views.AllProfilesListView , name='all_profiles'),
    path('about/' , views.about , name='blog-about'),
    path('post/<int:pk>/' , views.post_detail , name="post-detail"),
    path('like/' , views.like_post , name="like_post"),
    path('like_count/<int:pk>/' , views.like_count , name="like-count"),
    path('messages/' , views.user_messages , name="list-messages"),
    #path('send_message/<int:pk>/' , SendMessageView.as_view() , name="send-message"),
    path('send_message/<int:pk>/' , views.send_message , name="send-message"),
    path('messages/<int:pk>/' , views.detail_messages , name="user-messages"),
    path('add/' , views.follow_request , name="user-add"),
    path('followers/<int:pk>/' , views.followers , name="followers-list"),
    path('following/<int:pk>/' , views.following , name="following-list"),
]
