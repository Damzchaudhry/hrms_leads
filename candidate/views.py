from django.shortcuts import render
from .models import Candidate
# from .forms import Jobs_Form
from django.http import JsonResponse
from django.forms.models import model_to_dict
from datetime import date
from django.core import serializers



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

def app_can(request):
	candidate=Candidate.objects.all()
	context={"candidate":candidate}
	return render(request,'candidate/applicants.html',context)


