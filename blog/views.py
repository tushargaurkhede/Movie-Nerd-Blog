from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import BlogPost, Topic, Blogger, Comment

def index(request):
    '''View function for home page of site.'''

    #store all the records in corrosponding variables
    blogposts = BlogPost.objects.all()
    bloggers = Blogger.objects.all()
    topics = Topic.objects.all()
    comments = Comment.objects.all()

    context = {
        'blogposts': blogposts,
        'bloggers': bloggers,
        'topics': topics,
        'comments': comments,
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BlogListView(generic.ListView):
    model = BlogPost
    paginate_by = 10

class BlogDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10

class BloggerDetailView(generic.DetailView):
    model = Blogger

class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 10

class TopicDetailView(generic.DetailView):
    model = Topic

#Show the comments on the blog posts mapped to users
from django.contrib.auth.mixins import LoginRequiredMixin

class CommenterListView(LoginRequiredMixin, generic.ListView):
    '''Generic class-based view to show the comments in the blogposts'''
    model = Comment
    template_name = 'blog/user_comment.html'
    paginate_by = 10

    def get_queryset(self):
        return Comment.objects.all()

#Allow logged-in user to comment on a blogpost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.models import Comment

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['blogpost', 'comment', 'commenter']

    '''def __init__(self, *args, **kwargs):
        super (CommentCreate,self).__init__(*args, **kwargs)
        self.fields['blogpost'].queryset = Comment.objects.filter(blogpost=blogpost) 

    def get_queryset(self):
        return Comment.object.filter(blogpost=self.instance.blogpost)'''    

    def get_success_url(self):     
        return reverse_lazy('blogpost_detail', kwargs = {'pk': self.kwargs['pk']})

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['blogpost', 'comment', 'commenter']

    def get_success_url(self):
        return reverse_lazy('blogpost_detail', kwargs = {'pk': 1})


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('blogpost_detail', kwargs = {'pk': 1})


from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def add_comment_to_post(request, pk, *args, **kwargs):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('blogs'))
                                        
    else:
        form = CommentForm()
        
    context = {
        'form': form,
        'post': post,
    }
        
    return render(request, 'blog/add_comment_to_post.html', context)    
                            
#creating user profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blogs')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})    

