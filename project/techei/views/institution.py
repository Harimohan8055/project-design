from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.views.generic import TemplateView,ListView, CreateView, UpdateView
from django.http import HttpResponse
from ..models import User,IndividualProfile,InstitutionProfile,City,State
from django.urls import reverse_lazy
from ..forms import InstitutionProfileForm,InstitutionSignUpForm

# Create your views here.

class InstitutionSignUpView(CreateView):
    model = User
    form_class = InstitutionSignUpForm
    template_name = 'institution/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Institution'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/institution_profile')


def InstitutionProfileView(request):
    if request.method == "POST":
        form=InstitutionProfileForm(request.POST)
        if form.is_valid() :
            profile = form.save(commit = False)
            profile.user_id=request.user.id
            profile.save()
            return redirect('/institution_dashboard')

    else:
        form = InstitutionProfileForm()
    return render(request, "institution/profile.html",{"form":form})

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'individual/city_drop_list.html', {'cities': cities})


def InstitutionDashboardView(request):
    return HttpResponse('<h1>Institution</h1>')
