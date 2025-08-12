from django.shortcuts import render, redirect
from .models import Post
from .forms import CustomUserCreationForm, ProfileEditForm, PostCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated 
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

#Registeration views for users
class RegisterView(View):
    '''get form from forms.py'''
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request,'blog/register.html', {'form':form} )
    '''save form to database'''
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
        return render(request, 'blog/register.html', {'form': form})

#views to view and edit profile. 
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
            return redirect('profile')
    else:
        form = ProfileEditForm(instance = request.user)
    return render(request, 'blog/profile.html', {'form': form})


# Login & Logout (using Django's built-in views)
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'

# --- POST VIEWS (API CRUD) ---

# ListView to display all blog posts.
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

# DetailView to show individual blog posts.
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

# CreateView to allow authenticated users to create new posts.
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

# UpdateView to enable post authors to edit their posts.
class PostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

# DeleteView to let authors delete their posts.
class PostDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


# --- POST VIEWS (HTML CRUD) ---

# List all posts
class ListPostView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


# View single post details
class DetailPostView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


#create a new post only user is logged in
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')  # Redirect after success

    def form_valid(self, form):
        # Set the author to the logged-in user before saving
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        """Allow only the author to update their post."""
        post = self.get_object()
        return post.author == self.request.user
    
# Delete a post (only author allowed)
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user