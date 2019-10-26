from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.views.generic import TemplateView,ListView, CreateView, UpdateView
from django.http import HttpResponse
from ..models import User,IndividualProfile,InstitutionProfile,City,State,EventModel,FestClubModel,FestImage
from django.urls import reverse_lazy
from ..forms import InstitutionProfileForm,InstitutionSignUpForm,AddEventForm,AddFestClubForm,FestImageForm

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
            return redirect('/')

    else:
        form = InstitutionProfileForm()
    return render(request, "institution/profile.html",{"form":form})

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'individual/city_drop_list.html', {'cities': cities})


def InstitutionDashboardView(request):
    return HttpResponse('<h1>Institution</h1>')


class EventType(TemplateView):
    template_name = 'institution/event_type.html'

# class AddEvent(CreateView):
#     model = EventModel
#     form_class = AddEventForm
#     template_name = 'institution/addevent.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['type'] = self.type
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         event = form.save(commit = False)
#         event.user_id=request.user.id
#         event.type=self.type
#         event.save()
#         return redirect('/institution_dashboard')



def AddEvent(request, type):
    uid=request.user.id
    fe=FestClubModel.objects.filter(user_id=uid)
    print("hiii")
    if request.method == "POST":
        form=AddEventForm(request.POST)
        if form.is_valid() :
            event = form.save(commit = False)
            event.user_id=request.user.id
            event.event_type=type
            event.save()
            return redirect('/institution_dashboard')
        else:
            print(form.errors)
    else:
        form = AddEventForm()
    return render(request, "institution/addevent.html",{"form":form,"type":type,"fest":fe})



def AddFestClubView(request):
    uid=request.user.id
    fest_club=FestClubModel.objects.filter(user_id=uid)
    feimg=FestImage.objects.filter(user_id=uid).distinct()
    if request.method == "POST":
        form=AddFestClubForm(request.POST)
        if form.is_valid() :
            fest = form.save(commit = False)
            fest.user_id=request.user.id
            fest.save()
            request.session['fest_id'] = fest.id
            return redirect('/techei/festimage/')
    else:
        form = AddFestClubForm()
    return render(request, "institution/addfestclub.html",{"form":form, "fecl": fest_club, "fim":feimg})

# class AddFestClubView(CreateView):
#     model = FestClubModel
#     form_class = AddFestClubForm
#     template_name = 'institution/addfestclub.html'
#
#     def form_valid(self, form):
#

        # return redirect('/festimage')


#
def FestImageView(request):
    fid=request.session.get('fest_id')
    fimg = FestImage.objects.filter(fest_id=fid)
    if request.method == "POST":
        form=FestImageForm(request.POST,  request.FILES)
        if form.is_valid() :
            count = FestImage.objects.filter(fest_id=fid).count()
            if count<3:
                festimg = form.save(commit = False)
                festimg.user_id=request.user.id
                festimg.fest_id=request.session.get('fest_id')
                festimg.save()
                return redirect('/techei/festimage/')
            else:
                return redirect('/techei/festimage/')


            # return render((request, 'display_hotel_images.html',
            #          {'hotel_images' : Hotels}))


    else:
        form = FestImageForm()
    return render(request, "institution/fest_image.html",{"form":form,'fest_images' : fimg})
