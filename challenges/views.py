from django.shortcuts import render

# Create your views here.

class CreateChallengeView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateChallengeForm
    template_name = "projects/challenge_create.html"
    def form_valid(self, form):
        activity = form.save()
        activity.user = self.request.user
        activity.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("activity:activities"))