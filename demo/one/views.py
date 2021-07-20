from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from one.forms import RegistrationForm, OneAuthenticationForm, OneUpdateForm

#from blog.models import BlogPost

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			one = authenticate(email=email, password=raw_password)
			login(request, one)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'one/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = OneAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = OneAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "one/login.html", context)


def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = OneUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = OneUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['one_form'] = form

	#blog_posts = BlogPost.objects.filter(author=request.user)
	#context['blog_posts'] = blog_posts

	return render(request, "one/one.html", context)


def must_authenticate_view(request):
	return render(request, 'one/must_authenticate.html', {})



