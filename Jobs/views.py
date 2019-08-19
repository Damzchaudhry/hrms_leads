from django.shortcuts import render
from .models import Jobs,Dept,Status,Job_type
from .forms import Jobs_Form,Dept_Form,Type_Form,Status_Form
from django.http import JsonResponse
from django.forms.models import model_to_dict
from datetime import date
from django.core import serializers



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

def bookadmin_index_view(request):
	if request.method == 'POST':
		if request.is_ajax():
			createbookform = Jobs_Form(request.POST)
			if createbookform.is_valid():
				createbookform.cleaned_data
				createbookform.save()
				latest = Jobs.objects.latest('id').id
				book_object = model_to_dict(Jobs.objects.get(pk=latest))
				return JsonResponse({'error': False, 'data': book_object})
			else:
				print(createbookform.errors)
				return JsonResponse({'error': True, 'data': createbookform.errors})
		else:
			error = {
				'message': 'Error, must be an Ajax call.'
			}
			return JsonResponse(error, content_type="application/json")
	else:
		createbookform = Jobs_Form()
		all_books_object = Jobs.objects.all()
		dept= Dept.objects.all()
		status=Status.objects.all()
		types=Job_type.objects.all()
		data = {
			'createbookform_html': createbookform,
			'quersets': all_books_object,
			"dept":dept,
			"status":status,
			"types":types
		}
		return render(request, template_name='Jobs/jobs.html', context=data)

@csrf_exempt
def edit(request, id):
	if request.method == 'GET':
		if request.is_ajax():
			try:
				data1 = model_to_dict(Jobs.objects.get(id=id))
				title=data1['title']
				dept=data1['dept']
				job_location=data1['job_location']
				vacancy=data1['vacancy']
				exp=data1['exp']
				salary_from=data1['salary_from']
				salary_to=data1['salary_to']
				job_type=data1['job_type']
				status=data1['status']
				
				end_date=data1['end_date']
				desc=data1['desc']
				skill=data1['skill']
				email=data1['email']
				contact=data1['contact']
				

				return JsonResponse({'error': False, 'data1': data1,
					"title":title,
					"job_location":job_location,
					"dept":dept,

					
					"job_type":job_type,
					"dept":dept,
					"vacancy":vacancy,
					"exp":exp,
					"salary_from":salary_from,
					"salary_to":salary_to,
					"status":status,
					"skill":skill,
					
					"end_date":end_date,
					"desc":desc,
					"email":email,
					"contact":contact, 'id': id
				})

			except Jobs.DoesNotExist:
				return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist', 'id': id})
	return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist', 'id': id})


   



def bookadmin_delete_book(request, id):
	if request.method == 'POST' and request.is_ajax():
		try:
			book_object = Jobs.objects.get(id=id)
			book_object.delete()
			return JsonResponse({'status': 'Success', 'message': 'Recoard has been deleted.'})
		except Jobs.DoesNotExist:
			return JsonResponse({'status': 'Fail', 'message': 'Recoard does not exist.'})
	return JsonResponse({'status': 'Fail', 'message': 'Error, must be an Ajax call.'})


def details(request,id):
	querysets=get_object_or_404(Jobs,id = id)
	a=date.today()
	b=querysets.end_date
	c=b-a
	D=c.days

	return render(request,"Jobs/job-details.html",{"querysets":querysets ,"D":D})




def update(request,id):
	if request.method == 'POST':
		
		jobs = Jobs.objects.get(id=id)
		form = Jobs_Form(request.POST or None,instance = jobs)


		if request.is_ajax():

			if form.is_valid():
				print(id)
				form.cleaned_data
				form.save()
				l = Jobs.objects.latest('id').id
				book = model_to_dict(Jobs.objects.get(pk=l))
				return JsonResponse({'error': False, 'data': book})
			else:
				print(form.errors)
		else:
			print(form.errors)
			return JsonResponse({'error': True, 'data': form})
	return HttpResponse("Jobs/error.html")




def add_dept(request):
	if request.method == 'POST':
		if request.is_ajax():
			form = Dept_Form(request.POST)
			if form.is_valid():
				form.cleaned_data
				form.save()

				lst = Jobs.objects.latest('id').id
				obj1 = model_to_dict(Jobs.objects.get(pk=lst))
				return JsonResponse({'error': False, 'data': obj1})
			
		
			else:
				print(form.errors)
				return JsonResponse({'error': True, 'data': form.errors})
		else:
			error = {
				'message': 'Error, must be an Ajax call.'
			}
			return JsonResponse(error, content_type="application/json")
	return HttpResponse("Jobs/errors.html")


def add_status(request):
	if request.method == 'POST':
		if request.is_ajax():
			form = Status_Form(request.POST)
			if form.is_valid():
				form.cleaned_data
				form.save()
				return redirect("Jobs:bookadmin_index_view")
		
		
			else:
				print(form.errors)
				return JsonResponse({'error': True, 'data': form.errors})
		else:
			error = {
				'message': 'Error, must be an Ajax call.'
			}
			return JsonResponse(error, content_type="application/json")
	return HttpResponse("Jobs/errors.html")



def add_job_type(request):
	if request.method == 'POST':
		if request.is_ajax():
			form = Type_Form(request.POST)
			if form.is_valid():
				form.cleaned_data
				form.save()
				return redirect("Jobs:bookadmin_index_view")
			
		
			else:
				print(form.errors)
				return JsonResponse({'error': True, 'data': form.errors})
		else:
			error = {
				'message': 'Error, must be an Ajax call.'
			}
			return JsonResponse(error, content_type="application/json")
	return HttpResponse("Jobs/errors.html")
