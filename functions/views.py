from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import os
from django.utils import timezone
from main import models
from mypro import ifile
# Create your views here.

def functions(request):
	return render(request, 'functions.html')

def dm(request):
	this_Number_id = upload_file(request)
	if this_Number_id == 0:
		return HttpResponse('please choice a file')
	else:
		if this_Number_id == -1:
			return HttpResponse('error')
		else:
			this_Number = models.Number.objects.get(id=this_Number_id)
			this_file_path = this_Number.file
			data = ifile.openfile(this_file_path)
			dbget = write_to_db(data, this_Number_id)
			if dbget == 0:
				return HttpResponse('error')
			else:





				response = download_file(this_file_path)
				return response
	#upload_file
	#calculate
	#download_file

def upload_file(request):  
    if request.method == "POST":
        myFile =request.FILES.get("myfile", None) 
        if not myFile:
        	print('hello')
        	return 0	 

        this_time = timezone.localtime(timezone.now()).strftime("%Y%m%d%H%M%S")
        this_user = request.user.username 
        this_path = os.path.join("files/", this_time, this_user, "upload")
        os.makedirs(this_path)

        this_file_path = os.path.join(this_path, myFile.name)

        destination = open(this_file_path,'wb+')# 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()

        models.Number.objects.create(user=this_user, file=this_file_path, time=this_time)
        this_Number = models.Number.objects.get(time=this_time)
        this_Number_id = this_Number.id

        return this_Number_id
    return -1

def download_file(ff):  
    #file=open('file/test.txt','rb')  
    tempf = ff.split("/")[1]
    file = open(ff, 'rb')
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename='+tempf

    return response

def write_to_db(data,this_Number_id):
	num = len(data)
	i = 0
	pl_list = []
	pt_list	= []
	while i < num:
		lenth = len(data[i])
		if lenth == 5:
			pl_list.append(models.Dmline(dmlines=data[i][0], y1=float(data[i][1]), x1=float(data[i][2]), 
				y2=float(data[i][3]), x2=float(data[i][4]), num_id=this_Number_id))
		else:
			if lenth == 4:
				pt_list.append(models.Point(point=data[i][0], y=float(data[i][1]),
				x=float(data[i][2]), h=float(data[i][3]), num_id=this_Number_id))
			else:
				return -1
		i+=1
	models.Dmline.objects.bulk_create(pl_list)
	models.Point.objects.bulk_create(pt_list)

	return 1
