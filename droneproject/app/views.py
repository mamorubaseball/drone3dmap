from django.shortcuts import render
from django.views.generic import TemplateView
from drone import test

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    
    def post(self,request):
        if "start_button" in request.POST:
            test.take_off()
        return render(request,"index.html")