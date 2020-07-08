from django.shortcuts import render,redirect
from complain.models import *

# student_list=[]
# member_list=[]
# Create your views here.
def add_complain(request):
    if request.method=="POST":
        cat = request.POST.get("category_selection")
        sub_cat = request.POST.get("sub_category_selection")
        sub = request.POST.get("subject")
        comp = request.POST.get("complain_field")

        user=Complaint(category=cat,sub_category=sub_cat,subject=sub,complain_1=comp)
        user.save()
        return render(request, "done.html")
    else:
        return render(request, "addcomplain.html")

def done(request):
    if request.method=="POST":
        msg = request.POST.get("msg_from_member")
        s = Membermsg(membmsg=msg)
        s.save()
        member_list = Membermsg.objects.order_by('date')
        student_list = Studentmsg.objects.order_by('date')
        length = len(member_list)
        list1 = []
        for i in range (length):
            list1.append(i)

        global oc
        oc = request.POST.get("openclose")
        if oc=="open":
            return render(request, "student_msg.html", {'msg' : member_list, "oc" : oc, 'student': student_list, 'len': list1} )
        else:
            return render(request, "student_msg.html", {"msg": member_list, 'student': student_list, 'len': length})
    else:
        return render(request, "done.html")

def member_msg(request):
    # if member has kept choice open then student can reply. i student dont want to
     # reply den he can keep the messsage blank.
    if request.method=="POST":
        if oc=="open":
            msg = request.POST.get("msgfromstudent")
            l = Studentmsg(studmsg=msg)
            l.save()
            student_list = Studentmsg.objects.order_by('date')
            member_list = Member_msg.objects.order_by('date')
            return render(request, "done.html", {"message": student_list, 'member': member_list, 'len': length})
        else:
            pass
    else:
        return render(request, "student_msg.html")
