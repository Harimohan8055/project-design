from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import TemplateView,ListView, CreateView, UpdateView
from django.http import HttpResponse
from ..models import User,IndividualProfile,InstitutionProfile,City,State
from django.urls import reverse_lazy
from ..forms import IndividualProfileForm,IndividualSignUpForm

# Create your views here.


# class IndividualSignUpView:

# def IndividualSignUpView(request):
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)
#     if request.method == "POST":
#         form=IndividualSignUpForm(request.POST)
#         profile_form = IndividualProfileForm(request.POST)
#         if form.is_valid() and profile_form.is_valid():
#             user=form.save()
#             profile = profile_form.save(commit = False)
#             profile.user=user
#             profile.save()
#             user.save()
#
#     else:
#         form = IndividualSignUpForm()
#         profile_form = IndividualProfileForm()
#     return render(request, "individual\signup_form.html",{"form":form,"profile_form":profile_form})


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
        return redirect('/profile')


# class IndividualProfileView(CreateView):
#     model = IndividualProfile
#     form_class = IndividualProfileForm(initial={'song_list': song.song_list}, user=request.user)
#     template_name = 'individual/profile.html'
#
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'Individual'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         profile = form.save()

def IndividualProfileView(request):
    if request.method == "POST":
        form=IndividualProfileForm(request.POST)
        if form.is_valid() :
            profile = form.save(commit = False)
            profile.user_id=request.user.id
            profile.save()

    else:
        form = IndividualProfileForm()
    return render(request, "individual\profile.html",{"form":form})

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'individual/city_drop_list.html', {'cities': cities})
