from django.shortcuts import render , get_object_or_404 , reverse ,HttpResponseRedirect , Http404 , redirect
from django.http import HttpResponse
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin 
from django.contrib.auth.decorators import login_required , permission_required
from .models import Post , Announcements , Messages , FollowRequest
from users.models import User , Profile
from users.forms import PostUpdateForm , SendMessageForm


def PostHomeView(request):
    posts = Post.objects.all().order_by('-date_posted')
    stuff_for_frontend = {
        'posts' : posts,
    }    

    
    if request.user.id:
        user = User.objects.get(pk=request.user.id)
        following = FollowRequest.objects.filter(sender=user)
        user_list = []
        for following_users in following:
            if following_users.receiver:
                user_list.append(following_users.receiver)
                if following_users.sender not in user_list:
                    user_list.append(following_users.sender)
                else:
                    pass                
            else:
                pass

        post_list = []
        for post in posts:
            if post.author in user_list:
                post_list.append(post)
            else:
                pass    
        

        stuff_for_frontend = {
            'posts' : post_list,
        }

        return render(request , 'blog_sys/home.html' , stuff_for_frontend)
    
    else:

        stuff_for_frontend = {
            'posts' : posts,
        }

        return render(request , 'blog_sys/home.html' , stuff_for_frontend)

def post_detail(request , pk):
    post = Post.objects.get(pk=pk)
    is_liked = False
    if post.likes.filter(pk=request.user.id).exists():
        is_liked=True

    stuff_for_frontend = {
        'post' : post,
        'is_liked': is_liked,
    }
    
    return render(request , 'blog_sys/post_detail.html' , stuff_for_frontend)


def ProfileView(request , pk):
    another_user = User.objects.get(pk=pk)

    if request.user.id:
        followers_number = FollowRequest.objects.filter(receiver=pk).count()
        following_number = FollowRequest.objects.filter(sender=pk).count()
        user_accessing = User.objects.get(pk=request.user.id)
        is_following = False
        if FollowRequest.objects.filter(sender=user_accessing , receiver=another_user):
            is_following = True
        else:
            is_following = False
        
        if FollowRequest.objects.filter(sender=pk , receiver=pk):
            followers_number = followers_number - 1
            following_number = following_number - 1
        
        stuff_for_frontend = {
            'is_following': is_following,
            'another_user': another_user,
            'followers_number' : followers_number,
            'following_number' : following_number,
        }

        return render(request , 'blog_sys/profile_detail.html' , stuff_for_frontend)
    else:
        followers_number = FollowRequest.objects.filter(receiver=pk).count()
        following_number = FollowRequest.objects.filter(sender=pk).count()
        if FollowRequest.objects.filter(sender=pk , receiver=pk):
            followers_number = followers_number - 1
            following_number = following_number - 1

        stuff_for_frontend = {
            'another_user' : another_user,
            'followers_number' : followers_number,
            'following_number' : following_number,
        }
        return render(request , 'blog_sys/profile_detail.html' , stuff_for_frontend)



class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog_sys/post_form.html'

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog_sys/post_form.html'
   
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    success_url ='/'
    template_name = 'blog_sys/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request , 'Blog_sys/about.html' , {'title':'about'})

class MyPostsListView( LoginRequiredMixin , ListView):
    model = Post
    template_name = 'blog_sys/my_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class UserPostListView(ListView):
    model = Post
    template_name = 'blog_sys/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 10
    ordering = '-date_posted'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)


class AnnouncementsListView(ListView):
    model = Announcements
    template_name = 'blog_sys/blog_announcements.html'
    context_object_name = 'announcements'
    ordering = ['-date_posted']

                                                                                            #
#class AllProfilesListView(ListView , LoginRequiredMixin):                                  #
    #model = User                                                                           # Generic Class View
    #template_name = 'blog_sys/all_profiles.html'                                           #
    #context_object_name ='users'                                                           #

@login_required                                                                             #
def AllProfilesListView(request):                                                           # 
    users = User.objects.all()                                                              #
    stuff_for_frontend = {                                                                     # Function Base View
        'users' : users,
    }                                                                                       #
    return render(request , 'blog_sys/all_profiles.html' , stuff_for_frontend)              #

# ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ 
#       ♔                                ♔
#       ♕        Likes Views             ♕
#       ♔                                ♔
# ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ 

@login_required    
def like_post(request):
    post = Post.objects.get(id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())

@login_required
def like_count(request , pk):
    post = Post.objects.get(pk=pk)
    stuff_for_frontend = {
        'post': post
    }
    if request.user == post.author:
        return render(request , 'blog_sys/like_count.html' , stuff_for_frontend)
    else:
        return render(request , 'blog_sys/forbidden.html')

# ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ 
#       ♔                                ♔
#       ♕        Message Views           ♕
#       ♔                                ♔
# ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ 

@login_required
def detail_messages(request , pk):
    user = User.objects.get(pk=request.user.id)
    other_user = User.objects.get(pk=pk)
    message = Messages.objects.filter(to_user=user , from_user=other_user) 
    message = Messages.objects.filter(to_user=user , from_user=other_user).order_by('-date_sent') # Esta é a forma de ordenar objetos com Funçoes normais
  
    message_owner = Messages.objects.filter(to_user=other_user , from_user=user)
    message_owner = Messages.objects.filter(to_user=other_user , from_user=user).order_by('-date_sent')

    if message.exists():
        message_existence = True
    else:
        message_existence = False
    
    if message_owner.exists():
        another_message_existence = True
    else:
        another_message_existence = False
    
    if message_existence == False and another_message_existence == False:
        message = Messages
        form = SendMessageForm()
        user = User.objects.get(pk=request.user.id)
        other_user = User.objects.get(pk=pk)

        if request.method=="POST":
            form = SendMessageForm(request.POST)
            if form.is_valid():
                form.instance.from_user = request.user
                form.instance.to_user = other_user
                form.save()
                return HttpResponseRedirect(message.get_absolute_url(other_user))
           
        stuff_for_frontend = {
            'form': form,
            'other_user': other_user,
        }
    
        return render(request , 'blog_sys/message_form.html' , stuff_for_frontend)
    message_list = []

    for x in message:
        message_list.append(x.pk)
    
    for y in message_owner:
        message_list.append(y.pk)

    message_list.sort()
    message_list.reverse()

    position = -1

    for sms in message_list:
        position = position + 1
        message_count = Messages.objects.get(pk=sms)
        message_list.pop(position)
        message_list.insert(position , message_count)

    vista = Messages.objects.filter(to_user=user , from_user=other_user , viewed=False)
    for any_message in vista:
        any_message.viewed=True
        any_message.save()

    stuff_for_frontend = {
        'other_user': other_user,
        'message_list': message_list,
        'message_owner': message_owner,
    }

    if request.user.id == user.id:
        return render(request , 'blog_sys/messages_detail.html' , stuff_for_frontend)
    else:
        return render(request , 'blog_sys/forbidden.html')
    

@login_required
def user_messages(request):
    user = User.objects.get(pk=request.user.id)
    messages = Messages.objects.filter(to_user=user).order_by('-date_sent')
    another_messages = Messages.objects.filter(from_user = user).order_by('-date_sent')
    
    user_list = []
    for message in messages:
        if message.from_user:
            user_list.append(message.from_user)
        else:
            pass

    for message in another_messages:
        if message.to_user:
            user_list.append(message.to_user)

    user_list = list( dict.fromkeys(user_list))

    stuff_for_frontend = {
        'user_list': user_list,
    }
    
    if request.user.id == user.id:
        return render(request , 'blog_sys/messages_list.html' , stuff_for_frontend)
    else:
        return render(request , 'blog_sys/forbidden.html')

@login_required
def send_message(request , pk):
    message = Messages
    form = SendMessageForm()
    user = User.objects.get(pk=request.user.id)
    other_user = User.objects.get(pk=pk)

    if request.method=="POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.instance.from_user = request.user
            form.instance.to_user = other_user
            form.save()
            return HttpResponseRedirect(message.get_absolute_url(other_user))
           
    stuff_for_frontend = {
        'form': form,
        'other_user': other_user,
    }

    return render(request , 'blog_sys/message_form.html' , stuff_for_frontend)

# ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ 
#       ♔                                ♔
#       ♕      Follow Request Views      ♕
#       ♔                                ♔
# ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ ♔ ♕ 

@login_required
def follow_request(request):
    sender_X = User.objects.get(pk=request.user.id)
    receiver_Y = User.objects.get(pk=request.POST.get('another_user_id'))
    is_following = False

    if request.method == 'POST':   
        if FollowRequest.objects.filter(sender=sender_X.id , receiver=receiver_Y.id).exists():
            is_following = True
            a = FollowRequest.objects.get(sender=sender_X , receiver=receiver_Y)
            a.delete()
            return HttpResponseRedirect(Profile.get_absolute_url(receiver_Y))
        else:
            is_following = False
            FollowRequest.objects.create(sender=sender_X , receiver=receiver_Y)
            return HttpResponseRedirect(Profile.get_absolute_url(receiver_Y))
    else:
        return render(request , 'blog_sys/forbidden.html')    

        
def followers(request , pk):
    another_user = User.objects.get(pk=pk)
    follow_users = FollowRequest.objects.filter(receiver=another_user)
    followers_count = FollowRequest.objects.filter(receiver=another_user).count()
    
    if FollowRequest.objects.filter(sender=another_user , receiver=another_user):
        followers_count = followers_count - 1

    stuff_for_frontend = {
        'follow_users': follow_users,
        'followers_count' : followers_count,
    }
    
    return render(request , 'blog_sys/user_followers.html' , stuff_for_frontend)



def following(request , pk):
    another_user = User.objects.get(pk=pk)
    following_users = FollowRequest.objects.filter(sender=another_user)
    following_users_count = FollowRequest.objects.filter(sender=another_user).count()

    if FollowRequest.objects.filter(sender=another_user , receiver = another_user):
        following_users_count = following_users_count - 1

    stuff_for_frontend = {
        'following_users' : following_users,
        'following_users_count': following_users_count,
    }
    
    return render(request , 'blog_sys/user_following.html' , stuff_for_frontend)
