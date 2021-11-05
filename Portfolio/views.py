from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

from .models import *
# Create your views here.

def index(request):
    services= Services.objects.all()
    abouts= About.objects.all()
    projects= Projects.objects.all()


    context= {
        'services': services,
        'abouts': abouts,
        'projects': projects
    }
    
    return render (request, 'index.html', context)



def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get ('email')
		message= request.POST.get('message')
		
		data = {
			'name': name,
			'email': email,
			'message': message
		}
		message = '''
		New message: {}

		from: {}
		'''.format(data['message'], data['email'])
		send_mail(
			name, #name
			message, #subject
			email, #email
			['donesrom@gmail.com']#To email

		)

		return render(request, 'received.html', {'name': name})
	
		
	else:
		return render(request, 'contact.html', {})


#email received
def received(request):
	return render(request, 'received.html')