#custom signal
from django.dispatch import Signal, receiver
# create signal
notification = Signal(providing_args=["request", "user"])
owner = Signal(providing_args=["request", "owner_id"])

# create reciever
@receiver(notification)
def show_notification(sender, **kwargs):
    print('Notification')
    print(sender)
    print(f'kwargs {kwargs}')

@receiver(owner)
def pick_owner(sender, **kwargs):
    print('pick owner')
    print(sender)
    print(f'kwargs {kwargs}')



# using built-in login ,logout related signals
from django.contrib.auth.signals import user_logged_in\
    , user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

"""
# the below function is reciever of imported func
@receiver(user_logged_in, sender=User)  #connected reciever to signal by decorator
def login_success(sender,request, user, **kwargs):
    print("---------------")
    print("loged-in signal")
    print("sender", sender)
    print("request", request)
    print("user", user)
    print(f"kwargs, {kwargs}")
    
"""

"""
the below statement connects the above signal with manual connect route
user_logged_in.connect(login_success, sender=User)
"""

from django.db.models.signals import pre_save\
    , pre_init, post_save, post_init

"""
built in signals 

@receiver(pre_save, sender=User)
def before_save(sender, instance, **kwargs):
    print("---------------")
    print("pre save signal")
    print("sender", sender)
    print(f"kwargs, {kwargs}")

# pre_save.connect(before_save, sender=User)


@receiver(post_init, sender=User)
def after_init(sender, *args, **kwargs):
    print("---------------")
    print("post init signal")
    print("sender", sender)
    print(f"kwargs, {kwargs}")
"""

#custom signal
from django.dispatch import Signal, receiver
# create signal
notification = Signal(providing_args=["request", "user"])

# create reciever
@receiver(notification)
def show_notification(sender, **kwargs):
    print('Notification')
    print(sender)
    print(f'kwargs {kwargs}')