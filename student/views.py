from django.shortcuts import render

# Create your views here.



def allStudent(request):
    myVar  = {
        "fName":"christiane" ,
        "lName":"SOLIMAN",
        "mylist":[1,2,3,4,5,6,7],
        'mydict':{'python':'django' , 'PHP':'laravel'},
    }
    return render(request , 'student/student.html' ,context=myVar)


def addStudent(request):
    return render(request  , 'student/addStudent.html')


def editStudent(request):
    return render(request  , 'student/editStudent.html')


