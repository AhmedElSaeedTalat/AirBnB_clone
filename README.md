Description of the project :

The AirBnB clone project aims to build a simple web application similar to AirBnB. The first step of the project involves creating a command interpreter to manage AirBnB objects. The command interpreter will allow users to perform various operations on objects like creating, retrieving, updating, and destroying instances of classes such as User, State, City, Place, etc. These classes will all inherit from a parent class called BaseModel, which takes care of initialization, serialization, and deserialization of instances.

Description of the command interpreter:

The command interpreter is a program that allows users to interact with the AirBnB objects through the command line. It behaves like a simplified version of a shell, where users can enter specific commands to perform actions on the objects. The command interpreter will have functionalities to create new objects, retrieve objects from storage, perform operations on objects, update object attributes, and delete objects.

How to start it:

To start the command interpreter, you need to run the Python script that contains the main logic for the interpreter. Typically, the script will be named something like "console.py" or "cmd.py."

$ python3 console.py
Welcome to the AirBnB clone command interpreter!


How to use it:

Once the command interpreter is running, it will display a prompt where users can enter commands to interact with the AirBnB objects. The commands are structured in a specific format, and users can use various commands to create, retrieve, update, and delete objects.


examples:

$ python3 console.py
Welcome to the AirBnB clone command interpreter!
(hbnb) create User 135
(hbnb) update User 1235 name John
(hbnb) show User 125
(hbnb) destroy User 125
(hbnb) quit


