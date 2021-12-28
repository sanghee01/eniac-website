from django.views import View
from django.shortcuts import render

# Create your views here.

class ActivityView(View):
    def get(self, request):
        return render(request, "activities/attendance.html")

    def post(self, request):
        pass