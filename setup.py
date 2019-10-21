from setuptools import setup;

setup(
      name = "events",
      version="0.0.1",
      description="Event handling system using the pub/subscriber pattern",
      url="https://github.com/miljimo/messaging.git",
      author="Obaro I. Johnson",
      author_email="johnson.obaro@hotmail.com",
      packages=["events",], 
      install_requires=['mpi4py>=2.0',
                        
                       ],
      classifiers=[
          "Users : Developers",
          "Target : Python 2 & 3"
          ]);

      
