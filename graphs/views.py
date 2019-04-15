import random
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse, HttpResponseRedirect, reverse
from django.utils.decorators import method_decorator

# FileResponse - to display files
from django.http import FileResponse, Http404

from django.views.generic import DetailView, ListView, TemplateView, FormView, View

from quiz.models import Quiz, Category, Progress, Sitting, Question
from essay.models import Essay_Question
from users.models import ProfileModel
from graphs.models import EResources
from graphs.forms import PdfResources
# view to display a pdf
# coded by Kibuthi

class homeView( View ):
    template_name = 'charts.html'
    args = {}

    def get( self, request, *args, **kwargs ):
        if request.user.is_authenticated:
        	id=request.user.id
        	obj = Sitting.objects.filter(user_id=id)
        	quelist=[]
        	letter, b = Progress.objects.get_or_create(user_id=id)
        	marks = letter.list_all_cat_scores
        	exams = letter.show_exams()
        	examTitle = []
        	examscores = []
        	for exam in exams:
        		examTitle.append(exam.quiz.title)
        		examscores.append(exam.get_percent_correct)
        	print(examTitle)
        	print (examscores)
        	for ob in obj:
        		quizname=Quiz.objects.filter(id=ob.quiz_id)
        		for q in quizname:
        			print(q)
        			quelist.append(q)
        	quelist = list(quelist)
        		
        	args = {
        	'id':id,
        	'objs':obj,
        	'quiz':quelist,
        	'marks':marks,
        	'examscore':examscores,
        	'examtitle':examTitle

        	}
        	return render( request, self.template_name, args )
        else:
              return redirect( '/users/login/' )

    def post( self, request, *args, **kwargs ):
        pass
# end : homeView
class resourcesView(TemplateView):
    template_name = 'eresources.html'

    def get(self, request,*args,**kwargs):
        if request.user.is_staff:
            resources = EResources.objects.all()
            print(resources)
            args = {
            'resources':resources
            }
        else:
            select = request.user.user.Class
            resources =EResources.objects.filter(Class = select)
            print(resources)
            args = {
            'resources':resources
            }
        
        return render(request, self.template_name, args)
class teacherView(TemplateView):
    template_name = 'teacher.html'

class UploadView(TemplateView):
    template_name = 'fileupload.html'
    def get (self, request, *args, **kwargs):
        uploadform = PdfResources()
        args = {
        'uploadform':uploadform
        }
        return render(request, self.template_name, args)

    def post(self,request, *args, **kwargs):
        uploadform =  PdfResources(request.POST, request.FILES)
        if uploadform.is_valid():
            Class = uploadform.cleaned_data['Class']
            subject = uploadform.cleaned_data['subject']

            uploadform.save()
        return redirect('/graphs/Ematerials')


