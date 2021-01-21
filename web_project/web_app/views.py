from django.http import httpresponce
from django.views.generic import views, TableView
class MYView(View):
    def get(self,request):
        #<view logic>
        return httpresponce('result')