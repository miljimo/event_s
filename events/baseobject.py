"""************************************************************
* @brief
*   The base object of the system.
* 
************************************************************"""
import uuid;


class BaseObject(object):
    
    __OBJECT_COUNTS__  =  0;
    def __init__(self):
        
        self.__OBJECT_COUNTS__  = self.__OBJECT_COUNTS__ + 1;
        self.__id               = "{0}{1}".format(uuid.uuid4(), self.__OBJECT_COUNTS__);
        self.__name             = self.__id;
        
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


if(__name__ == "__main__"):
    obj1  =  BaseObject();
    obj2  =  BaseObject();
    obj1.Name= "Obaro I. Johnson";
    print(obj1.Name);
    print(obj2.ID);
