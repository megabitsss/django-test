from django.shortcuts import render,redirect
from django.contrib import messages
from mypage.models import creativereser
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")

def creative(request):
    if request.method == 'POST':
        id_input = request.POST['student-id-form']
        name_input = request.POST['name-form']
        date_input = request.POST['date-form']
        start_input = request.POST['start-date-form']
        end_input = request.POST['end-date-form']

        start_time = datetime.strptime(start_input, '%H:%M').time()
        end_time = datetime.strptime(end_input, '%H:%M').time()

        overlapping_bookings = creativereser.objects.filter(
            event_date=date_input,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists()

        if overlapping_bookings:
            messages.error(request, "The room has been booked during that time. Please enter a different time slot!")
            return redirect("creative.html")

        form = creativereser.objects.create(
            student_id=id_input,
            name=name_input,
            event_date=date_input,
            start_time=start_time,
            end_time=end_time
        )
        form.save()
        return redirect("checkscreative.html")
    else:
        return render(request, "creative.html")

def room(request):
    list_person = creativereser.objects.order_by('event_date') #****************
    # list_person = creativereser.objects.all()
    return render(request,"checkscreative.html",{"list_person":list_person})