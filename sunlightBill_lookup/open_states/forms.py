from django import forms
from localflavor.us.forms import USStateField

# This search bill form will have 3 field objects: bill_number and state. bill_number and bill_name will have a character field type and states will have a choice field type.
'''
#creating a function for my choicefield as an alternative
def get_my_sunlightAPIs():
	sunlightAPIs = (
        ('1', 'Congress'),
        ('2', 'States'),
		)
	return sunlightAPIs
'''

class SearchBillForm(forms.Form):
	sunlightAPIs = forms.ChoiceField(choices=((1, 'Congress'),(2, 'States')))
	bill_number = forms.CharField(label="bill number", max_length=10)
	state = forms.CharField(label="state", max_length=5, required= False)
	#states = USStateField()
	#states_choices = forms.CharField(widget=USStateField())


class WidgetListForm(forms.Form):
        bill_number = forms.CharField(widget = forms.Textarea, max_length=10)
        bill_name = forms.CharField(widget = forms.Textarea, max_length=200)