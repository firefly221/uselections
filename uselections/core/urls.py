from django.urls import path
from core.views import IndexView
from core.views import CandidatesView
from core import views

urlpatterns = [
    path('index',IndexView.as_view(),name='index'),
    path('candidates',CandidatesView.as_view(),name='candidates'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('votefor/<int:id>',views.CandidateDetailView.as_view(),name='votefor'),
    path('states',views.stateView,name='states'),
    path('states_detail/<str:state_name>',views.StateDetailView.as_view(),name='states_detail'),
    path('polls',views.PollsView.as_view(),name='polls'),
]












