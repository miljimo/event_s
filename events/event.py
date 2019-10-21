import os;


class NamedObject(object):
    __UUID = 0;
    
    def __init__(self, name):
        self.__name  = name;
        self.__id    = self.__UUID + 1;
        
    @property
    def Name(self):
        return self.__name;

    @Name.setter
    def Name(self, value):

        if(type(value) != str):
             raise ValueError("Unexpected value provided");
        self.__name  = value;
        

    @property
    def ID(self):
        return self.__id;

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
