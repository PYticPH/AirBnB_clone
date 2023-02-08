# AirBnB clone

The goal of the project is to deploy on your server a simple copy of the [AirBnB]("https://www.airbnb.com/")  website.

## The Console Interpreter

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

=> Create a new object (ex: a new User or a new Place)
=> Retrieve an object from a file, a database etc…
=> Do operations on objects (count, compute stats, etc…)
=> Update attributes of an object
=> Destroy an object

### How to start the console Interpreter
    
    <ins> interactive mode </ins>

    $ ./console.py
    (hbnb) help
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $

    <ins> non-interactive mode </ins>
    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py

    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)
    $
