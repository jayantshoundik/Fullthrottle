from django.db import models
from random import choice
from string import ascii_uppercase,digits

class Member(models.Model):
    import pytz
    idgenerator = ''.join(choice(ascii_uppercase + digits) for i in range(9))
    idno = models.CharField(max_length=9,unique=True,default=idgenerator)
    real_name  = models.CharField(max_length=11)
    tz = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=255, default='UTC', choices=tz)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.idno

class ActivityPeriod(models.Model):
    member = models.ForeignKey(Member, related_name='activityperiod',on_delete=models.CASCADE,null=False)
    start_time =  models.DateTimeField()
    end_time =  models.DateTimeField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s : %s' %(self.start_time, self.end_time)


