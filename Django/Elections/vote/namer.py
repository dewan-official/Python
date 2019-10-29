from django.shortcuts import render
def newuserEntry(request):
	return render(request, 'admin-panal/new_user_entry.html',{})