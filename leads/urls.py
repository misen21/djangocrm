from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import LeadUpdateView, LeadView, lead_delete

app_name = 'users'

urlpatterns =[
    path('', login_required(LeadView.as_view()), name='lead-index'),
    path('<int:pk>/update/', login_required(LeadUpdateView.as_view()), name='lead-update'),
    path('<int:pk>/delete/', login_required(lead_delete), name='lead-delete'),

]