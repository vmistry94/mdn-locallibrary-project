import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default is 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal is in the past.'))

        # Check date is within 4 weeks
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalidate date - renewal more than the allowed 4 weeks.'))

        # Return the cleaned data
        return data