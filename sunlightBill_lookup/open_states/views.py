from django.template import Context 
from django.shortcuts import render 
import requests
from forms import SearchBillForm, WidgetListForm
from django.http import HttpResponseRedirect, HttpResponse
#import config 

def index(request):
	#Create a variable form for the SearchBillForm function in forms.py 
	form = SearchBillForm()
	# If the form has been submitted in the SearchBIllForm using the Post request method  
	if request.method == 'POST': 
		# Create a form variable that will receive the SearchBillForm post request
		form = SearchBillForm(request.POST)
		#If form is valid.  All validation rules are listed in forms.py 
        if form.is_valid(): 
         # Process the data in form.cleaned_data by creating a bill_id and state variable
         bill_id = form.cleaned_data['bill_number']
         state = form.cleaned_data['state']
         #redirect to the widget view
         return HttpResponseRedirect('/open_states/get_widget_list/%s/%s/' % (bill_id, state)) # Here we have to add the /open_states prefix to get Django to find the right urls.py files
	return render(request, 'open_states/index.html', {'form': form})


# This is a stand alone function that will pull the input field data/parameters: Api_key, bill_id, open_states_url.  
def get_openstates_api(bill_id, state):
	#Create a parameters variable from the openstates api rules including apikey, bill_id, and state
	api_key = "c105eafac75e4f61b208de79bec4803f"
	params = {'apikey': api_key, 'bill_id': bill_id, 'state': state} 
	s = requests.get("http://openstates.org/api/v1/bills/", params=params)
	json_response = s.json()
	return json_response

#This function will pass the state and bill_id api
# We need request, bill_id, and state in the input section on the next line in order to pass variables to the API call
def get_widget_list(request, bill_id, state):
	#Create a variable form for the SearchBillForm function in forms.py 
	form = WidgetListForm()
	# If the form has been submitted in the SearchBIllForm using the Post request method  
	if request.method == 'GET':
		#json_response variable with get_openstates_api function
		json_response = get_openstates_api(bill_id, state)
		# Create a form variable that will receive the WidgetListForm get request
		form = WidgetListForm(request.GET, {'json_response': json_response})
		return render(request, 'open_states/widget_list.html',{'form': form})
