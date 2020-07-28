from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.
class Agent(models.Model):
    agent_name = models.CharField(max_length=100)
    agent_id = models.CharField(max_length=5)
    agent_pass = models.CharField(max_length=256)

    def verifyPass(self, raw_pass):
        return pbkdf2_sha256.verify(raw_pass, self.agent_pass)

    class Meta:
        db_table = 'agent_auth'

class todo(models.Model):
    agent_id = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        db_table = 'agent_todo'