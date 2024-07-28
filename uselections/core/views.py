from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .forms import VoterForm
from .models import Voter,Candidate,STATES,State,Poll
from django.contrib.auth.hashers import make_password,check_password
from django import forms
from django.views.generic import DetailView
from .functions import update_electoral_votes,generate_poll
from core.statedata import *




class IndexView(View):
    def get(self,request):
        update_electoral_votes()
        logged_in = request.session.get('logged_in')
        user_email = request.session.get('email')
        num = 0
        for voter in Voter.objects.all():
            if voter.voted:
                num+=1
        
        votes_rep = Candidate.objects.get(name='Donald Trump').votes
        votes_dem = Candidate.objects.get(name='Kamala Harris').votes
        votes_ind = Candidate.objects.get(name='Robert Kennedy').votes
        
        percent_rep = int(votes_rep/535*100)
        percent_dem = int(votes_dem/535*100)
        percent_ind = int(votes_ind/535*100)
        context ={'number' : num, 'logged_in' : logged_in, 'user_email' : user_email,'votes_rep' : votes_rep,'votes_dem' : votes_dem,
                  'votes_ind' : votes_ind, 'percent_dem' : percent_dem,'percent_rep' : percent_rep,'percent_ind' :percent_ind}  
        return render(request,'core/index.html',context)
    
class CandidatesView(View):
    def get(self,request):
        voted = False
        my_email = request.session.get('email','None')
        if my_email != 'None':
            voter = Voter.objects.get(email=my_email)
            voted = voter.voted
        candidates = Candidate.objects.all()
        logged_in = request.session.get('logged_in',False)
        return render(request,'core/candidates.html',{'logged_in' : logged_in,'candidates' : candidates,'voted' : voted})
    


def register(request):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])
            state = form.cleaned_data['state']
            gender = form.cleaned_data['gender']
            education = form.cleaned_data['education']
            voter = Voter(name=name,email=email,password=password,state = state,gender = gender,education = education)
            voter.save()
            request.session['logged_in'] = True
            request.session['email'] = email
            return redirect('index')
    else:
        if request.session.get('logged_in') == True:
            return redirect('index')
        form = VoterForm()
    context = {'form' : form}
    return render(request,'core/register.html',context)

def login(request):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        
        email = request.POST['email']
        password = request.POST['password']
        encoded_password = Voter.objects.filter(email=email)
        
        if not encoded_password or len(encoded_password) > 1:
            return HttpResponse("Coś poszło nie tak")
        if check_password(password,encoded_password[0].password):
            request.session['logged_in'] = True
            request.session['email'] = email
            return redirect('index')
        else:
            return HttpResponse('ZLE HASLO LUB LOGIN')
    else:
        if request.session.get('logged_in') == True:
            return redirect('index')
        form = VoterForm()
    context ={'form' : form}
    return render(request,'core/login.html',context)

def logout(request):
    try:
        del request.session['logged_in']
        del request.session['email']
    except KeyError:
        pass
    return redirect('index')



class CandidateDetailView(View):
    def get(self,request,id):
        candidate = Candidate.objects.get(id=id)
        if request.session.get('logged_in',False) == False:
            return redirect('index')
        my_email = request.session.get('email',False)
        voter = Voter.objects.get(email=my_email)
        if voter.voted:
            return redirect('candidates')
        else:
            return render(request,'core/votefor.html',{'candidate' : candidate})

    def post(self,request,id):
        my_email = request.session.get('email')
        obj = Voter.objects.get(email = my_email)
        obj.voted = True
        candidate = Candidate.objects.get(id=id)
        candidate.votes+=1
        state = State.objects.get(name=obj.state.name)
        if candidate.party == 'Republican':
            state.votes_rep+=1
        elif candidate.party == 'Democrat':
            state.votes_dem+=1
        else:
            state.votes_ind+=1
        obj.party = candidate.party
        update_electoral_votes()
        state.save()
        candidate.save()
        obj.save()
        return redirect('index')
    

    
def stateView(request):
    sorting_method = request.GET.get('sort','')
    looks = {}
    percent_dem = {}
    percent_rep = {}
    percent_ind = {}
    states = []

    states_objects = State.objects.all()
    if sorting_method != '' and sorting_method != 'None':
        states_objects = states_objects.order_by(sorting_method)

    for state in states_objects:
        MAX = max(state.votes_dem,state.votes_ind,state.votes_rep)
        TOTAL = max(1,state.votes_dem + state.votes_ind +state.votes_rep)
        percent_dem[state.name] = int(100*(state.votes_dem/TOTAL))
        percent_rep[state.name] = int(100*(state.votes_rep/TOTAL))
        percent_ind[state.name] = int(100*(state.votes_ind/TOTAL))
        
        states.append({'percent_dem' : percent_dem[state.name],'percent_rep' : percent_rep[state.name], 'percent_ind' : percent_ind[state.name],
                       'name' : state.name})
    logged_in = request.session.get('logged_in',False)
    context = {'states' : states,'logged_in' : logged_in}
    return render(request,'core/states.html',context)

class StateDetailView(View):
    def get(self,request,state_name):
        if state_name not in STATES.values():
            return redirect('states')
        else:
            state = State.objects.get(name=state_name)
        state_data = []
        YEAR = 1960
        for election in STATE_DATA:
            for st in election['votes']:
                if STATES[st] == state_name:
                    #print(election['votes'][st])
                    republican_votes = election['votes'][st]['electoral']['republican']
                    democrat_votes = election['votes'][st]['electoral']['democrat']
                    if republican_votes > democrat_votes:
                        color = 'danger'
                    else:
                        color = 'info'
                    state_data.append({'year' : YEAR,'republican_votes' : republican_votes,'democrat_votes' : democrat_votes,'color' : color})
                    YEAR+=4

        people = Voter.objects.filter(state=state)
        logged_in = request.session.get('logged_in',False)
        context = {'state' : state,'people' : people,'state_data' : state_data[::-1],'logged_in' : logged_in}
        return render(request,'core/states_detail.html',context)

class PollsView(View):
    def get(self,request):
        polls = Poll.objects.all()
        logged_in = request.session.get('logged_in',False)
        return render(request,'core/polls.html',{'polls':polls,'logged_in' : logged_in})
    def post(self,request):
        generate_poll()
        return redirect('polls')


