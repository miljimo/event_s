"""
 The base class of all the event objects.
"""
class Event(object):

    def __init__(self, typeid ):
        self.__typeid  = typeid;
        self.__stopPropagation = False;

    @property
    def Type(self):
        return self.__typeid;

    @property
    def StopPropagation(self):
        return self.__stopPropagation;

    @StopPropagation.setter
    def StopPropagation(self, stopStatus):
        if(type(stopStatus)  == bool):
            self.__stopPropagation = stopStatus;


"""
 Test the event class.
"""
if(__name__ =="__main__"):
    event  = Event(89);
    print(event.Type);
    print(event.StopPropagation);
    event.StopPropagation = True;
    print(event.StopPropagation);
