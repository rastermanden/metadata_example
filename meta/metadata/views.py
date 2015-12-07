# views.py
from django.views.generic import ListView, DetailView
from metadata.models import Metadata
from django.utils import timezone

class MetadataList(ListView):
    model = Metadata
    paginate_by = 5
    
    context_object_name = 'metadata_list'
  
    def get_queryset(self):
            if self.request.GET.get("search"):
                search = self.request.GET.get("search")
                return Metadata.objects.filter(search_string__icontains=search) ## http://robots.thoughtbot.com/post/43154885203/class-based-generic-views-in-django     
            else:
                 return Metadata.objects.all()
             
                
    def get_context_data(self, **kwargs):
        context = super(MetadataList, self).get_context_data(**kwargs)
 
        context['search'] =  self.request.GET.get("search")
        return context

class MetadataDetail(DetailView):

    model = Metadata
    context_object_name = 'metadata_detail'
    
    def get_context_data(self, **kwargs):
        context = super(MetadataDetail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context