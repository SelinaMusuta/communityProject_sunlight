from django import forms

# This search bill form will have 3 field objects: bill_number and state. bill_number and bill_name will have a character field type and states will have a choice field type.

class SearchBillForm(forms.Form):
	# how do I connect the api_call to the ChoiceField. api_call = forms.ChoiceField(label="open congress or open states", choices=SUNLIGHT_APIS)
	bill_number = forms.CharField(label="bill number", max_length=10)
	state = forms.CharField(label="state", max_length=5)

class WidgetListForm(forms.Form):
        bill_number = forms.CharField(widget = forms.Textarea, max_length=10)
        bill_name = forms.CharField(widget = forms.Textarea, max_length=200)