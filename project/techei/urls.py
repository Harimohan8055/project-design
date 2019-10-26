from django.urls import path
from techei.views import register,institution,individual

urlpatterns =[
    path('eventtype', institution.EventType.as_view(), name='event_type'),
    path('addevent/<int:type>/', institution.AddEvent, name='add_event'),
    path('addfest/', institution.AddFestClubView, name='add_fest'),
    path('festimage/',institution.FestImageView, name='add_fest_image'),
]
