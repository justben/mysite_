from django.db import models

# Create your models here.
class Number(models.Model):
	#numid = models.IntegerField()
	user = models.CharField(max_length=10) 
	file = models.CharField(max_length=50)
	time = models.CharField(max_length=14)

class Dmline(models.Model):
	dmlines = models.CharField(max_length=10)
	#dmid = models.IntegerField()
	y1 = models.FloatField()
	x1 = models.FloatField()
	y2 = models.FloatField()
	x2 = models.FloatField()
	num = models.ForeignKey(Number, on_delete=models.CASCADE, )

class Point(models.Model):
	point = models.CharField(max_length=10)
	#pid = models.IntegerField()
	y = models.FloatField()
	x = models.FloatField()
	h = models.FloatField()
	num = models.ForeignKey(Number, on_delete=models.CASCADE, )

class PointLine(models.Model):
	point_id = models.IntegerField()
	line_id = models.IntegerField()
	d = models.FloatField()
	y = models.FloatField()
	x = models.FloatField()
	h = models.FloatField()
	d0 = models.FloatField()
	num = models.ForeignKey(Number, on_delete=models.CASCADE, )

class LinePoint(models.Model):
	line_id = models.IntegerField()
	point_id = models.IntegerField()
	d1 = models.FloatField()
	h = models.FloatField()
	num = models.ForeignKey(Number, on_delete=models.CASCADE, )



