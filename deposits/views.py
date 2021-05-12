from django.shortcuts import render
from django.views.generic import ListView, View, FormView, DetailView

from deposits.models import Deposit
from deposits.forms import AddDeposit


class DepositList(ListView):
    model = Deposit
    template_name = 'deposit_list.html'


class DepositDetail(DetailView):
    model = Deposit
    template_name = 'deposit_detail.html'


class DepositAdd(FormView):

    form_class = AddDeposit
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self, form):

        form.save()

        response = super().form_valid(form)

        return response
