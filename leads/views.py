from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Lead
from .forms import LeadForm, LeadModelForm
from django.core.exceptions import PermissionDenied


class LeadView(generic.View):
    def get(self, request):
        allleads = Lead.objects.order_by('-updated_at')
        form = LeadForm
        context = {
            'leads': allleads,
            'form': form
        }
        return  render(request, "leads/lead_index.html", context)

    def post(self, request, *args, **kwargs):
      if request.method=="POST":
        lead_ids=request.POST.getlist('id[]')
        for id in lead_ids:
            lead = Lead.objects.get(pk=id)
            lead.delete()
        return redirect("/leads")

class LeadCreateView(generic.CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

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
