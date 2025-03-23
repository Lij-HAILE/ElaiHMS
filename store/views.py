from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from .models import Question,Order,Answer,Table
from .forms import QuestionForm,OrderForm
from django.urls import reverse
from django.contrib import messages
import random
import string
# Create your views here.
def home(request):
    return render(request,"store/home.html")

class MyDashboard(LoginRequiredMixin,ListView):
    queryset = Order.objects.filter(table=1)
    model =Order
    template_name ="store/dashboard.html"
    paginate_by = 8
    context_object_name = 'ord'
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["table"] = Table.objects.filter(~Q(id=1))
        context['ques'] =Question.objects.all()
        return context

@login_required
def create_question(request):
    question = Question.objects.all()
    order=Order.objects.all()
    if(request.method == "POST"):
        form = QuestionForm(request.POST)
        if(form.is_valid()):
            ques = form.save(commit=False)
            ques.user = request.user
            ques.save()
            return redirect(reverse('dashboard'))
        return render(request,"store/dashboard.html",{"ques":question,"ord":order,'form':form})
    
@login_required
def create_answer(request):
    question = Question.objects.all()
    order=Order.objects.all()
    if(request.method == "POST"):
        if(request.POST.get('question') and request.POST.get('answer')):
            ques = Question.objects.get(id=int(request.POST.get('question')))
            ques.answer.add(Answer.objects.create(user=request.user,ans=request.POST.get('answer')))
            return redirect(reverse('dashboard'))
        return render(request,"store/dashboard.html",{"ques":question,"ord":order,"error":True})
    
@login_required
def delete_answer(request,id):
    question = Question.objects.all()
    order=Order.objects.all()
    ans = Answer.objects.get(id=int(id))
    if(ans):
        ans.delete()
        return redirect(reverse('dashboard'))
    return render(request,"store/dashboard.html",{"ques":question,"ord":order,"error":True})

@login_required
def delete_question(request,id):
    question = Question.objects.all()
    order=Order.objects.all()
    ques = Question.objects.get(id=int(id))
    if(ques):
        ques.delete()
        return redirect(reverse('dashboard'))
    return render(request,"store/dashboard.html",{"ques":question,"ord":order,"error":True})

@login_required
def create_order(request):
    if(request.method=="POST"):
        form =OrderForm(request.POST)
        if(form.is_valid()):
            ord =form.save(commit=False)
            if(request.POST.get('table')):
                table = Table.objects.get(id=int(request.POST.get('table')))
                ord.table =table
            ord.user = request.user
            ord.save()
            return redirect(reverse('dashboard'))
        return redirect(reverse('dashboard'))
@csrf_exempt
@login_required
def edit_time(request):
    try:
        if(request.method == "POST"):
            print(request.POST)
            item = Order.objects.get(id=int(request.POST.get('id')))
            time =request.POST.get('time')
            if(item.pieces >= int(time)):
                item.complete = int(time)
                item.save()
                return redirect(reverse('dashboard'))
            else:
                messages.add_message(request,messages.ERROR,message="fix problem")
                return redirect(reverse('dashboard'))
    except:
        return redirect(reverse('dashboard'))
    
@login_required
@csrf_exempt
def create_table(request):
    Table.objects.create(name="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)))
    return redirect(reverse('dashboard'))  


@login_required
@csrf_exempt
def delete_order(request,id):
    item = Order.objects.get(id=int(id))
    item.delete()
    return redirect(reverse('dashboard'))    
@login_required
@csrf_exempt
def delete_table(request,id):
    item = Table.objects.get(id=int(id))
    item.delete()
    return redirect(reverse('dashboard'))    

