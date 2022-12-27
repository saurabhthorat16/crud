from django.shortcuts import render, redirect
from .models import Student, Fees
from .forms import StudentForm, FeeForm


# Create your views here.
def studentView(request):
    form = StudentForm()
    template_name = 'CRUD_APP/stuform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studataurl')
    return render(request, template_name, context)

def feeView(request):
    form = FeeForm()
    template_name = 'CRUD_APP/feeform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feesdataurl')
    return render(request, template_name, context)

def showStudentView(request):
    obj = Student.objects.all()
    template_name = 'CRUD_APP/showstu.html'
    context = {'data': obj}
    return render(request, template_name, context)

def showFeeView(request):
    obj = Fees.objects.all()
    template_name = 'CRUD_APP/showfee.html'
    context = {'data': obj}
    return render(request, template_name, context)

def updateStudentView(request, id):
    obj = Student.objects.get(sid=id)
    form = StudentForm(instance=obj)
    template_name = 'CRUD_APP/stuform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('studataurl')
    return render(request, template_name, context)

def updateFeeView(request, id):
    obj = Fees.objects.get(id=id)
    form = FeeForm(instance=obj)
    template_name = 'CRUD_APP/feeform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = FeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('feesdataurl')
    return render(request, template_name, context)

def deleteStudentView(request,id):
    obj = Student.objects.get(sid=id)
    template_name = 'CRUD_APP/confirmation.html'
    context = {'data': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('studataurl')
    return render(request, template_name, context)

def deleteFeeView(request,id):
    obj = Fees.objects.get(id=id)
    template_name = 'CRUD_APP/confirmation2.html'
    context = {'data': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('feesdataurl')
    return render(request, template_name, context)