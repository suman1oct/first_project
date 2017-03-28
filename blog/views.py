from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm, EditForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.http import HttpResponse
#from django.http import HttpRequest
"""def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
"""


class PostView(generic.ListView):
	template_name='blog/homepage.html'
	queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').all()

class PostDetailView(generic.DetailView):
	template_name = 'blog/blog_detail.html'
	model = Post
	# users=User.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		context['month_post'] = Post.objects.filter(published_date__month=timezone.now().month).exclude(id=self.kwargs['pk'])
		return context

class LoginView(generic.FormView):
	template_name='blog/login.html'
	form_class=LoginForm
	success_url=reverse_lazy('blog:dashboard')

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect('blog:dashboard')
		return super(LoginView, self).get(*args, **kwargs)

	def form_valid(self,form):
		username =form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		print('dfvdsdsf')
		user=authenticate(username=username,password=password)
		# import pdb
		# pdb.set_trace()
		if user.is_active:
			login(self.request, user)
			return redirect('blog:dashboard')

	
"""def logout_view(request):
	logout(request)
	text="<h3><center>User logout successfully</center></h3>"
	return HttpResponse(text)
"""

class LogoutView(View):
    def get(self, request):
        logout(request)
       	# return HttpResponseRedirect('blog:login')
       	return redirect('blog:login')


class DashboardView(generic.ListView):
	template_name='blog/dashboard.html'

	def get(self, *args, **kwargs):
		if not self.request.user.is_authenticated():
			return redirect('blog:login')
		return super(DashboardView, self).get(*args, **kwargs)

	def get_queryset(self):
		return Post.objects.order_by('published_date')
	#queryset=Post.objects.order_by('published_date').all()ef

class RegistrationView(generic.FormView):
	template_name='blog/registration.html'
	form_class=RegistrationForm
	#success_url=reverse_lazy('blog:post')
	def form_valid(self,form):
		username =form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		email=form.cleaned_data.get('email')
		#if username not in User:
		user=User(username=username,email=email)
		user.set_password(password)
		user.save()
		return redirect('blog:login')

"""def success_view(request):
		return render(HttpResponse,"blog/success.html",{})
"""

class EditView(UpdateView):
	model=Post
	fields=['author','title','text','created_date','published_date','image']
	#success_url = '/admin'
	success_url=reverse_lazy('blog:post')
	#return redirect('blog:success')
	# def form_valid(self, form):
		# return self.render_to_response(self.get_context_data(form=form))
		# return form

class AddView(CreateView):
	model=Post
	fields=['author','title','text','created_date','published_date','image']
	#success_url='/admin'
	success_url=reverse_lazy('blog:post')