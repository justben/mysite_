from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import os
from django.utils import timezone
from main import models
from mypro import ifile, ishadow
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
			dbget = write_to_pldb(data, this_Number_id)
			if dbget == 0:
				return HttpResponse('error')
			else:
				Line_data = models.Dmline.objects.filter(num_id=this_Number_id)
				Point_data = models.Point.objects.filter(num_id=this_Number_id)
				num_l = len(Line_data)
				num_p = len(Point_data)

				a = models.Dmline.objects.all().values_list('id')
				print(a)
				
				i = 0
				pl_list = []
				
				while i < num_l:
					p1 = [Line_data[i].y1, Line_data[i].x1]
					p2 = [Line_data[i].y2, Line_data[i].x2]
					j = 0
					while j < num_p:
						p = [Point_data[j].y, Point_data[j].x]
						xy = ishadow.shadow(p, p1, p2)
						if xy == []:
							j+=1
						else:
							point_id = Point_data[j].id
							line_id = Line_data[i].id
							d = ishadow.ptl(p, p1, p2)
							h = Point_data[j].h
							d0 = ishadow.ptp(xy, p1)
							num_id = this_Number_id
							pl_list.append(models.PointLine(point_id=point_id, line_id=line_id,
								d=d, y=xy[0], x=xy[1], h=h, d0=d0, num_id=num_id))
							j+=1
					i+=1
				models.PointLine.objects.bulk_create(pl_list)	
				
					#is or not
					#threshold
					





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

def write_to_pldb(data,this_Number_id):
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
