from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope = 'jack'
    """so like this u can make a particular throttling class give it a scope name and control the throttle in 
    settings by mentioning the scope and then make this ur throttle class if u want it for an api"""