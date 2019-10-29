from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home'),
	path('home/', views.homeX, name='homeX'),
	path('new_user_entry/', views.newUserEntry, name='new_user_entry'),
	path('new_user_entry/submit/', views.entrySubmission, name='new_user_entry'),
	path('user_list/', views.userList, name='userList'),
	path('create-new-vote/', views.voteCreation, name='voteCreation'),
	path('create-new-vote/<int:amount>', views.voteCreationData, name='voteCreationData'),
	path('vote-list/', views.voteList, name='voteList'),
	path('register/', views.register, name='register'),
	path('login/', views.logins, name='login'),
	path('logout/', views.userlogout, name='logout'),
	path('admin-logout/', views.adminlogout, name='adminlogout'),
	path('admin-login/', views.adminLogin, name='adminLogin'),
    path('profile/', views.profile, name='profile'),
]