from django.contrib import admin
from .models import Candidate,Voter,State,Poll

admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(State)
admin.site.register(Poll)







