from django.contrib import admin
from .models import User, Elections, Candidates, Vote

admin.site.register(User)
admin.site.register(Elections)
admin.site.register(Candidates)
admin.site.register(Vote)