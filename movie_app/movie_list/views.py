from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
# Create your views here.

def create(request):
    
    if request.POST: 
        frm=MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
    else:
            frm=MovieForm()       
        #  title=request.POST.get('title')  another method for form fetching
        #  year=request.POST.get('year')
        #  summary=request.POST.get('summary')
        #  movie=MovieInfo(title=title,year=year,summary=summary)
        #  movie.save()
    return render(request, 'create.html',{'frm':frm})

def list(request):

        movie_data =MovieInfo.objects.all()
        return render(request,'list.html',{'movies':movie_data})

def edit(request,pk):
    instance_edited=MovieInfo.objects.get(pk=pk)
    
    if request.POST: 
        frm=MovieForm(request.POST,instance=instance_edited)      
        # if frm.is_valid:
            
        title=request.POST.get('title')
        year=request.POST.get('year')
        summary=request.POST.get('summary')
        instance_edited.title=title
        instance_edited.year=year
        instance_edited.summary=summary
        instance_edited.save()
    else:
        frm=MovieForm(instance=instance_edited) 
    return render(request, 'create.html',{'frm':frm})

def delete(request,pk):
        instance=MovieInfo.objects.get(pk=pk)
        instance.delete()
        movie_data =MovieInfo.objects.all()
        return render(request,'list.html',{'movies':movie_data})
