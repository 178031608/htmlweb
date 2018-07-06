from django.shortcuts import render

# Create your views here.

def loginviews(request):
	print('请求类型是',request.method)
	if request.method == 'GET':
		return render(request,'login.html')