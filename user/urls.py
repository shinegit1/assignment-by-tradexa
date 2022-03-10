from django.urls import URLPattern, path
from user import views
urlpatterns = [
    path('',views.home_page,name='home'),
    path('login/',views.login_page,name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('dashboard/',views.dashboard_page,name='dashboard'),
    path('profile/',views.profile_page,name='profile'),
    path('newpost/',views.create_post,name='newpost'),
    path('update/<int:id>',views.update_post,name='update'),
    path('logout/',views.logout_page,name='logout'),
]
