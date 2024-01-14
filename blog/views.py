from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/users_post.html', context)

class PostListView(ListView):
    model=Post
    template_name='blog/users_post.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']


class PostDetailView(DetailView):
    model=Post


class PostCreateView(CreateView):
    model=Post
    fields=['title','content']

# associate post with author
    def form_valid(self,form):
        form.instance.author=self.request.user

        return super().form_valid(form)