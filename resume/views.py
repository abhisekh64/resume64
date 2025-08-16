from django.shortcuts import render,HttpResponse
from django.views.generic import View


class Home(View):
    template_name = "pages/home.html"
    def get(self, request, *args, **kwargs):
        context = self.context_name()
        return render(request,self.template_name,context)
    
    def context_name(self):
        context = {"home":"active"}
        return context


class Templates(View):
    template_name = "pages/templates.html"
    def get(self, request, *args, **kwargs):
        context = self.context_name()
        return render(request,self.template_name,context)
    
    def context_name(self):
        context = {"templates":"active"}
        return context


class Testing(View):
    template_name = "pages/testing.html"
    def get(self, request, *args, **kwargs):
        context = self.context_name()
        return render(request,self.template_name,context)
    
    def context_name(self):
        context = {"home":"active"}
        return context
