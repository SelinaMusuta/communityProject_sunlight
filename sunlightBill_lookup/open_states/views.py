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
        	sunlightAPIs = form.cleaned_data['sunlightAPIs']
        	bill_id = form.cleaned_data['bill_number']
         	state = form.cleaned_data['state']
         	if state=="":
         		state="none"

         	# Process the data in form.cleaned_data by creating a bill_id and state variable
         	#redirect to the widget view
         	return HttpResponseRedirect('/open_states/get_widget_list/%s/%s/%s/' % (sunlightAPIs, bill_id, state)) # Here we have to add the /open_states prefix to get Django to find the right urls.py files
	return render(request, 'open_states/index.html', {'form': form})


# This is a stand alone function that will pull the input field data/parameters: Api_key, bill_id, open_states_url. And then return a json_response from the Open Congress API. 
def get_openstates_api(bill_id, state):
	#Create a parameters variable from the openstates api rules including apikey, bill_id, and state

	api_key = "c105eafac75e4f61b208de79bec4803f"
	params = {'apikey': api_key, 'bill_id': bill_id, 'state': state} 
	s = requests.get("http://openstates.org/api/v1/bills/", params=params)
	json_response = s.json()
	return json_response

# This is a stand alone function that will pull the input field data/parameters: Api_key, bill_id, open_states_url. And then return a json_response from the Open Congress API.
def get_opencongress_api(bill_id):
	#Create a parameters variable from the Congress API api rules including apikey, bill_id, and state
	api_key = "c105eafac75e4f61b208de79bec4803f"
	params = {'apikey': api_key, 'bill_id': bill_id} 
	s = requests.get("https://congress.api.sunlightfoundation.com/bills/search/", params=params)
	json_response = s.json()
	return json_response

#This function will pass the state, bill_id, and request 
# We need request, bill_id, and state in the input section on the next line in order to pass variables to the API call
def get_widget_list(request, sunlightAPIs, bill_id, state):
	form = SearchBillForm()
	if request.method == 'POST': 
		form = SearchBillForm(request.POST)
        if form.is_valid(): 
        	sunlightAPIs = form.cleaned_data['sunlightAPIs']
        	bill_id = form.cleaned_data['bill_number']
         	state = form.cleaned_data['state']
         	if state=="":
  				state="none"
         	return HttpResponseRedirect('/open_states/get_widget_list/%s/%s/%s/' % (sunlightAPIs, bill_id, state)) # Here we have to add the /open_states prefix to get Django to find the right urls.py files 
	if request.method == 'GET':
		if sunlightAPIs == "1":
			json_response = get_opencongress_api(bill_id)
			congress_bills = json_response['results']
			state_bills = []
#			try:
#				congress_bills = congress_bills.append(json_response['results'])
#			except:
#				congress_bills = []
		else:
			json_response = get_openstates_api(bill_id, state)
			state_bills = json_response
			congress_bills = []
#			try:
#				state_bills = state_bills.append(json_response)
#			except:
#				state_bills = []
			# Get the slice of bills for the state json object state_bills = json_response[????]
		return render(request, 'open_states/widget_list.html',{'state_bills': state_bills, 'form':form, 'congress_bills':congress_bills})