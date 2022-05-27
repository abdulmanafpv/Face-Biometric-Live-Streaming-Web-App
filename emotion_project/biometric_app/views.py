from django.shortcuts import render
from django.http import StreamingHttpResponse
from biometric_app.camera import VideoCamera
from biometric_app.camera import unknowncam
from .models import Employee, Detected, unreg, Checking
from .forms import EmployeeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
from biometric_app.data import copy, load_images, get_frame,reload
from biometric_app.my_face_recognition import f_main
from biometric_app.data import loading
from django.db.models import Q
from biometric_app.f_Face_info import get_face_info
import traceback
import numpy as np
from biometric_app.my_face_recognition import f_storage as st
from biometric_app.my_face_recognition import f_main
import cv2
from biometric_app import f_Face_info
import imutils
# Create your views here.


def index(request):
	copy()
	date_formatted = datetime.datetime.today().date()
	date = request.GET.get('search_box', None)
	if date is not None:
		date_formatted = datetime.datetime.strptime(date, "%Y-%m-%d-%s").date()
	det_list = Detected.objects.filter(time_stamp__date=date_formatted).order_by('time_stamp').reverse()
	print(det_list)

	# date_formatted = datetime.datetime.today().date()
	det_list = Detected.objects.filter(time_stamp__date=date_formatted).order_by('time_stamp').reverse()[:6]
	emp_list = Employee.objects.all()
	if request.method == "POST":
		form = EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			emp = form.save()
			print(emp)
			return HttpResponseRedirect(reverse('index'))
	else:
		form = EmployeeForm()
	return render(request,'index.html',{'det_list':det_list,'date': date_formatted,'emp_list': emp_list,'form':form})


def refresh(request):
    return HttpResponseRedirect(reverse('index'))

def search_result(request):
    result = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        result = Detected.objects.all().filter(Q(time_stamp__icontains=Query))

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            emp = form.save()
            print(emp)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = EmployeeForm()
    return render(request,'serch-result.html',{'result':result,'form':form})



def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')





def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')



def capture_video(request):
	return StreamingHttpResponse(gen(unknowncam()), content_type='multipart/x-mixed-replace; boundary=frame')

def unregisterd(request):
	# result = unreg.objects.all().order_by('-id')[:3]
	result = unreg.objects.all().order_by('-id')
	return render(request,'unregisterd.html',{'result':result})


def search_result(request):
	result = None
	Query = None
	if 'q' in request.GET:
		Query = request.GET.get('q')
		result = Detected.objects.all().filter(Q(time_stamp__icontains=Query))

	if request.method == "POST":
		form = EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			emp = form.save()
			print(emp)
			return HttpResponseRedirect(reverse('index'))
	else:
		form = EmployeeForm()
	return render(request,'serch-result.html',{'result':result,'form':form})





def training(request):
	reload()
	# st.load_images_to_database()
	# get_frame()
	# load_images()
	return HttpResponseRedirect(reverse('index'))


def registerd_people(request):
	result = Employee.objects.all().order_by('-id')

	return render(request,'registerd_people.html', {'result':result})


def unknown_search(request):
	if request.method == 'POST':
		name = request.POST.get('q')
		result = unreg.objects.filter(date_time__icontains=name)
		# print(result.count())
	return render(request,'unknown-search.html',{'result':result})

checking_people=['']
def checking_individual(request):
	if request.method == 'POST':
		obj = request.POST.get('q')
		checking_people.append(obj)
		print(obj)
		print(checking_people[-1])
		# for i in checking_people:
		# 	print(i)

	return HttpResponseRedirect(reverse('index'))
	# return render(request, 'checking_people.html')

def check_list():
	name= checking_people[-1]
	# for i in checking_people:
	# 	return i

	return name


def uncheck(request):
	result = Checking.objects.all().order_by('-id')
	return render(request, 'checking_people.html', {'result': result})
