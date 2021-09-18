from django.urls import path
from .views import signup, my_profile, profile_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('profile/', my_profile, name='my-profile'),
    path('<slug:username>/',profile_view,name="profile-view"),
]