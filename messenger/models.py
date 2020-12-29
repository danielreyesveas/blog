from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.utils.dateformat import format

class ThreadManager(models.Manager):
    def find(self, user1, user2):
        # self = Thread.objects.all()
        queryset = self.filter(users=user1).filter(users=user2)
        
        if len(queryset) > 0:
            return queryset[0]

        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)

        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
            
        return thread

    def last_thread(self, user):
        try:
            return user.threads.latest('updated_at')           
        except Thread.DoesNotExist:
            return None

    def thread_last_update(self, user):
        last_thread = self.last_thread(user)
        if last_thread:
            return format(last_thread.updated_at, 'U')
        else:
            return 0


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')    
    updated_at = models.DateTimeField(auto_now=True)
    objects = ThreadManager()

    class Meta:
        ordering = ['-updated_at']

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


"""def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)

    false_pk_set = set()
    if action=="pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)
            
    #Buscar los mensajes de false_pk_set que están en pk_set y borrarlos de pk_set
    pk_set.difference_update(false_pk_set)

    # Forzar la actualización de la relación haciendo un save
    instance.save()

m2m_changed.connect(messages_changed, sender=Thread.messages.through)"""