from django.shortcuts import render 

from django.http.response import HttpResponse , HttpResponseNotFound ,Http404
# Create your views here.

#  request  : Browser User
def index(request):
    # return HttpResponse("Hello Christiane Soliman ...! ")
    return render(request , 'student.html')
    # pass
  

def my_about(request):
        return HttpResponse("Hello Christiane Soliman About ...! ")


def my_teachre(request):
        return HttpResponse("Hello Christiane Soliman teacher ...! ")


def my_result(request , number1 , number2):
        try:       
            result = number1 + number2
            return HttpResponse(result)
        except:
            result ="Only Number Allow"
            # return HttpResponseNotFound(result)
            raise Http404(404)
    #    raise : بمعنى رفع الخطء 

def my_name(request , fName  , lName):
    result = fName  +  " " +lName
    return HttpResponse(result)


