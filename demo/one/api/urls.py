from django.urls import path
from one.api.views import(
	registration_view,

)

app_name = 'one'

urlpatterns = [
	path('register', registration_view, name="register"),
]
