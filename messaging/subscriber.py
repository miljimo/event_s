from event import Event;

"""
 The class for a class listener event;
"""
class Subscriber(object):

    def __init__(self):
        pass;
    
    def __call__(self, event):
        if(isinstance(event, Event) != True):
             raise ValueError("@Subscriber: event must be an object of event type");
        self.OnNotify(event);
    
    def OnNotify(self,  event):
        raise NotImplementedError("@Subscriber- OnNotify must be implement");
