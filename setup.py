from setuptools import setup;

setup(
      name = "messaging",
      version="0.1.0",
      description="Event handling system using the pub/subscriber pattern",
      url="https://github.com/miljimo/messaging",
      author="Obaro I. Johnson",
      author_email="johnson.obaro@hotmail.com",
      packages=["messaging",], 
      install_requires=['mpi4py>=2.0',
                       ],
      classifiers=[
          "Users : Developers, Python Engineers",
          "Target : Python 2 and Python 3"
          ]);

      
