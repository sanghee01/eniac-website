from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy



class EmailLoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:project")


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:project")


class LoggedInOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("user:login")