from django.shortcuts import render , redirect
from .models import User, Elections, Candidates, Vote
from django.core.files.storage import FileSystemStorage
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cdid = request.POST['submit']
            eleid = request.POST['eleid']
            xxx = Candidates.objects.get(electionId=int(eleid),candidateId=int(cdid))
            xxy = xxx.candidateVOte
            xxx.candidateVOte = int(xxy)+1
            xyz = Vote(userID=request.user.id,electionId=eleid,status=True)
            xyz.save()
            xxx.save()
            return redirect('/logout/')
        else:
            a = Elections.objects.filter(electionStatus=True)
            c = ''
            b = {}
            xxxx = 0
            for id in a:
                b = Candidates.objects.filter(electionId=id.electionID)
                if cheak(request.user.id, id.electionID) == True:
                    xxxx = id.electionID
                    c += '<div class="container-fluid p-3 bg-light" style="text-align: center;"><h3 class="mb-4">' + id.electionTitle + '</h3><div class="d-flex col-md-12 justify-content-center">'
                    for xx in b:
                        c += '<button class ="mr-3" data-toggle="modal" data-target="#x_' + str(
                            xx.candidateId) + '"><img src="../media/' + xx.candidateSign + '" style="width: 150px; height: 150px" /></button>'
                    c += '</div></div>'
                else:
                    c = '<h4 class="alert alert-warning text-center m-4">Election End Or No Election Created.</h4>'

            context = {"values": c,
                       "id": b,
                       "electionId":xxxx}
            return render(request, 'vote/index.html', context)
    else:
        return redirect('login/', {"error":"Login First"})

def cheak(x , y):
    xx = Vote.objects.filter(userID=x,electionId=y)
    for xy in xx:
        if xy.status == True:
            return False
        else:
            return True
    return True


def homeX(request):
    return redirect("../")


def userList(request):
    all_User = User.objects.all()
    context = {
        'all_User': all_User,
    }
    return render(request, 'admin-panal/user_card.html', context)


def newUserEntry(request):
    return render(request, 'admin-panal/new_user_entry.html', {})


def entrySubmission(request):
    name = request.POST['user_name']
    DOB = request.POST['dob']
    Gender = request.POST['user_gender']
    BloodGroup = request.POST['user_blood_group']
    Phone = request.POST['user_phone']
    Email = request.POST['user_email']
    Image = request.FILES['user_image']
    fs = FileSystemStorage()
    fs.save(Image.name, Image)

    a = User(userName=name, userDOB=DOB, userGender=Gender, userBloodGroup=BloodGroup, userPhone=Phone, userEmail=Email,
             userImage=Image)
    a.save()
    return render(request, 'admin-panal/index.html', {})


def voteCreation(request):
    return render(request, 'admin-panal/new_vote.html', {})
def voteCreationData(request,amount):
    if(request.method == 'POST'):
        electionTitle = request.POST['v_title']
        electionStatus = False
        a = Elections(electionTitle=electionTitle, electionStatus = electionStatus)
        a.save()
        fs = FileSystemStorage()
        j = 1
        while j<=amount:
            i = str(j)
            candiateID = request.POST['cadidate_id_'+i]
            candiateImage = request.FILES['candidate_s_'+i]
            xx = User.objects.get(id=int(candiateID))
            cdname = xx.userName
            cdphone = xx.userPhone
            cdemail = xx.userEmail
            cdimage = xx.userImage
            fs.save(candiateImage.name, candiateImage)
            b = Candidates(electionId=Elections.objects.last(),candidateId = candiateID,candidateVOte=0, candidateSign = candiateImage,candidateName=cdname,candidatePhone=cdphone,candidateEmail=cdemail,candidateImage=cdimage)
            b.save()
            j = j+1
        redirect(voteCreation)
        return render(request, 'admin-panal/vote_list.html',{})
    else:
        return render(request,'admin-panal/new_vote.html',{})




def voteList(request):
    if request.user.is_authenticated:
        a = Elections.objects.all()
        c = ''
        for id in a:
            b= Candidates.objects.filter(electionId=id.electionID)
            c += '<div class="container-fluid p-3 bg-light position-relative" style="text-align: center; border: 1px solid #000"><h3 class="mb-4">'+id.electionTitle+'</h3><div class="d-flex col-md-12 justify-content-center">'
            for xx in b:
                c += '<button class ="candidate_btn mr-3 position-relative overflow-hidden"><div class="hover">'+xx.candidateVOte+'</div><img src="../media/'+xx.candidateSign+'" style="width: 150px; height: 150px" /></button>'
            c+='<button class="btm btn-success" data-toggle="modal" data-target="#x_'+str(id.electionID)+'">'+str(id.electionStatus)+'</button></div></div>'

        context = {"values": c,
                   "id": a}
        if request.method == 'POST':
            val = request.POST['submit']
            bol = Elections.objects.get(electionID=val)
            if bol.electionStatus == True:
                bol.electionStatus = False
                bol.save()
                return redirect('../vote-list/')
            else:
                bol.electionStatus = True
                bol.save()
                return redirect('../vote-list/')

        else:
            return render(request, 'admin-panal/vote_list.html', context)
    else:
        return redirect('../admin-login/')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            userphone = request.POST['userPhone']
            useremail = request.POST['userEmail']
            userdob = request.POST['dob']
            data = User.objects.all()
            p = False
            e = False
            d = False
            for i in data:
                if i.userPhone == userphone:
                    p = True
                    if i.userEmail == useremail:
                        e = True
                        if i.userDOB == userdob:
                            d = True
                            xx = User.objects.get(id = i.id)
                            xx.userid = username
                            xx.save()
                            form.save()
                            messages.success(request, f'Account Successfully Created')
                            return redirect('../login/')
            if p == False:
                messages.error(request, f'User Phone Number Don\'t Exsist')
                return redirect('../register/')
            if e == False:
                messages.error(request, f'User Email Don\'t Exsist')
                return redirect('../register/')
            if d == False:
                messages.error(request, f'User Date of Birth is invalid')
                return redirect('../register/')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':RegisterForm()})




def logins(request):
    if request.user.is_authenticated:
        return redirect('../home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                context = {
                    "error": "Success"
                }
                return redirect('../', {"error": "successfull"})
            else:
                context = {
                    "erorr": "An Error occur.."
                }
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html', {})

def userlogout(request):
    logout(request)
    return redirect('../login/',{"error":"logout"})

def adminlogout(request):
    logout(request)
    return redirect('../admin-login/', {"error": "logout"})


def adminLogin(request):
    if request.user.is_authenticated:
        return redirect('../vote-list/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                return redirect('/vote-list/')
            else:
                return render(request, 'admin.html', {"error": "Enter valid username and password"})
        else:
            return render(request, 'admin.html', {})



def profile(request):
    if request.user.is_authenticated:
        x = request.user.username
        xx = {}
        print(x)
        try:
            xx = User.objects.get(userid=x)
        except:
            print("Error occurs")
        context = {
            "id": xx
        }
        print(xx)
        return render(request, 'vote/userprofile.html', context)
    else:
        return redirect('../login/')