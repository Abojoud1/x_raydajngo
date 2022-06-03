from django.shortcuts import render

# Create your views here.
 
def Updates(request):
   return render (request,'GENERAL/Update spe.html')
def Updatem(request):
   return render(request, 'GENERAL/Update material.html')
def Adds(request):
   return render(request, 'GENERAL/Add spe.html')
def Addm(request):
   return render(request, 'GENERAL/Add material.html')
def Removes(request):
   return render(request, 'GENERAL/Remove spe.html')
def Removem(request):
   return render(request, 'GENERAL/Remove material.html')
def spe(request):
   return render(request, 'GENERAL/spe.html')
def mat(request):
   return render(request, 'GENERAL/mat.html')
def general(request):
   return render(request, 'general.html')





