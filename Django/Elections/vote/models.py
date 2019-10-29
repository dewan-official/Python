from django.db import models

class User(models.Model):
	userid = models.CharField(max_length=20)
	userName = models.CharField(max_length=50)
	userDOB = models.CharField(max_length=10)
	userGender = models.CharField(max_length=6)
	userBloodGroup = models.CharField(max_length=3)
	userPhone = models.CharField(max_length=20, unique= True)
	userEmail = models.EmailField(max_length=100, unique=True)
	userAddress = models.CharField(max_length=500)
	userImage = models.CharField(max_length=500)
	userStatus = models.CharField(max_length=10)
class Elections(models.Model):
	electionID = models.IntegerField(primary_key=True,auto_created=True,unique=True)
	electionTitle = models.CharField(max_length = 200)
	electionWinner = models.CharField(max_length=20)
	electionStatus = models.BooleanField(default=False)
	def __int__(self):
		return self.electionID
class Candidates(models.Model):
	electionId = models.ForeignKey(Elections, on_delete=models.IntegerField)
	candidateId = models.CharField(max_length=20)
	candidateVOte = models.CharField(max_length=20)
	candidateSign = models.CharField(max_length=200)
	candidateName = models.CharField(max_length=50)
	candidatePhone = models.CharField(max_length=20)
	candidateEmail = models.CharField(max_length=200)
	candidateImage = models.CharField(max_length=500)

class Vote(models.Model):
	userID = models.IntegerField()
	electionId = models.IntegerField()
	status = models.BooleanField(default=False)