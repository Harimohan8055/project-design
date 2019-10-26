from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import TemplateView,ListView, CreateView, UpdateView
from django.http import HttpResponse
from ..models import User,IndividualProfile,InstitutionProfile,City,State
from django.urls import reverse_lazy
from ..forms import IndividualProfileForm,IndividualSignUpForm


class IndividualSignUpView(CreateView):
    model = User
    form_class = IndividualSignUpForm
    template_name = 'individual/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Individual'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/individual_profile')


def IndividualProfileView(request):
    if request.method == "POST":
        form=IndividualProfileForm(request.POST)
        if form.is_valid() :
            profile = form.save(commit = False)
            profile.user_id=request.user.id
            profile.save()
            return redirect('/')

    else:
        form = IndividualProfileForm()
    return render(request, "individual/profile.html",{"form":form})

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'individual/city_drop_list.html', {'cities': cities})


def IndividualDashboardView(request):
    return render(request,'individual/individual_home.html')
