from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Lead
from .forms import LeadForm, LeadModelForm
from django.core.exceptions import PermissionDenied


class LeadView(generic.CreateView):
    model = Lead
    template_name = "leads/lead_index.html"
    form_class = LeadModelForm

    def get_context_data(self, **kwargs):
        kwargs['leads'] = Lead.objects.order_by('-updated_at')
        return super(LeadView, self).get_context_data(**kwargs)
    def get_success_url(self):
       return reverse("leads:lead-index")


class LeadUpdateView(generic.UpdateView):
   model = Lead
   template_name = "leads/lead_update.html"
   form_class = LeadModelForm
    
   def get_success_url(self):
     return reverse("leads:lead-index")

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.user.is_superuser:
     lead.delete()
    else:
        raise PermissionDenied("Access forbidden 403. Are you root?")
    return redirect("/leads")
