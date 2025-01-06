from django.shortcuts import render,redirect
from myapp.forms import UserCreationForm,UserLoginForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from myapp.models import User
from myapp.decorators import signin_required
from django.utils.decorators import method_decorator

# Create your views here.

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form_instance=UserCreationForm

        return render(request,'myapp/signup_form.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=UserCreationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()

            return redirect('login')
        
        return render(request,'myapp/signup_form.html',{'form':form_instance})
    

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form_instance=UserLoginForm()

        return render(request,'myapp/signin_form.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=UserLoginForm(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            user_obj=authenticate(request,**data)
            if user_obj:
                login(request,user_obj)
                return redirect('index')
            else:
                return render(request,'myapp/signin_form.html',{'form':form_instance})
            
@method_decorator(signin_required,name='dispatch')
class DashboardView(View):
    def get(self,request,*args,**kwargs):
        if request.user.category=='admin':
            data=User.objects.all()

            return render(request,'myapp/index.html',{'data':data})
        
        elif request.user.category=='staff':
            staff=User.objects.get(username=request.user)
            
            return render(request,'myapp/index.html',{'staff':staff})

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)

        return redirect('login')