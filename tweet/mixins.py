from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):

    def form_valid(self , form):
        if self.request.user.is_authenticated: #dont put "()" after is_authenticated
            form.instance.user = self.request.user 
            return super(FormUserNeededMixin ,self).form_valid(form)
        else:
            #Must import forms and ErrorList to create that
            form.__errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
            return self.form_invalid(form) #the user can't create tweet if he did'n login

class UserOwnerMixin(object):

    def form_valid(self , form): #for updateveiw
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin ,self).form_valid(form)
        else:
            form.__errors[forms.forms.NON_FIELD_ERRORS] = ErrorList["This user is not allowed to change this data."]
            return self.form_invalid(form)