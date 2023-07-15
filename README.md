AIRBNB CLONE
-------------
This project is all about creating a clone for a service that will be used
by user to find a place to stay temporarily in a specific city and for a specific
date and time and for a certain period.
HBNB Command-Line Interface
This command-line interface (CLI) provides a way to interact with the HBNB program,
which is responsible for managing instances of various classes such as
BaseModel, User, Place, City, State, Amenity, and Review.

Prerequisites
Python 3.x
Getting Started

Usage
Once you have started the CLI, you will see a prompt (hbnb).
Here are the available commands and their descriptions:

create <class_name>
-------------------
Creates a new instance of the specified class.

Usage:
create <class_name>

show <class_name><instance_id>
------------------------------
Displays the details of a specific instance.

Usage:
show <class_name> <instance_id>

destroy <class_name> <instance_id>
----------------------------------
Deletes a specified instance.

Usage:
destroy <class_name> <instance_id>

all [<class_name>]
------------------
Displays all instances or instances of a specified class.

Usage:
all [<class_name>]

count <class_name>
-------------------
Counts the number of instances of a specified class.

Usage:
count <class_name>

update <class_name> <instance_id> <attribute_name> <attribute_value>
--------------------------------------------------------------------
Updates the attributes of a specific instance.

Usage:
update <class_name> <instance_id> <attribute_name> <attribute_value>

quit
------
Exit the program.

Usage:
quit

Examples
---------
Create a new User instance:
(hbnb) create User

Show details of a specific Place instance with ID "123":
(hbnb) show Place 123

Destroy a City instance with ID "456":
(hbnb) destroy City 456

Display all instances of State class:
(hbnb) all State

Count the number of Review instances:
(hbnb) count Review

Update the name attribute of an instance with ID "789":
(hbnb) update BaseModel 789 name "New Name"

Exiting the Program
To exit the program, you can use the quit command or EOF

Amenity Class
--------------
This module contains the Amenity class,
which represents an amenity in the system.

Class Details
-------------
Class: Amenity
Inheritance: BaseModel
Attributes:
name (str): The name of the amenity.

Usage
To use the Amenity class, follow these steps:

1. Import the Amenity class:
`from models.amenity import Amenity`
2. Create an instance of the Amenity class:
amenity = Amenity()
3. Access and modify the attributes of the Amenity instance:
amenity.name = "Swimming Pool"
4. Save the changes to the instance:
amenity.save()

Examples
---------
Here are some examples to demonstrate the usage of the Amenity class:

# Create a new Amenity instance
amenity = Amenity()
amenity.name = "Gym"

# Save the instance
amenity.save()

# Access the attributes
print(amenity.name)  # Output: Gym

# Update the attributes
amenity.name = "Fitness Center"
amenity.save()

# Delete the instance
amenity.delete()

Inheritance
The Amenity class inherits from the BaseModel class.
This means that the Amenity class inherits all the attributes and
methods from the BaseModel class, which provides basic functionality
for managing instances.

For more information on the BaseModel class, please refer to the BaseModel README.

BaseModel Class
----------------
This module contains the BaseModel class, which serves
as the base class for all other classes in the system.

Class Details
--------------
Class: BaseModel
Attributes:
id (str): The unique identifier of
the instance (automatically generated).
created_at (datetime): The datetime when the instance was created.
updated_at (datetime): The datetime when the instance was last updated.

Usage
------
To use the BaseModel class, follow these steps:

1. Import the BaseModel class:
from models.base_model import BaseModel
2. Create an instance of the BaseModel class:
base_model = BaseModel()
3. Access and modify the attributes of the BaseModel instance:
base_model.created_at = datetime(2022, 1, 1)
4. Save the changes to the instance:
base_model.save()
5. Convert the instance to a dictionary:
base_model_dict = base_model.to_dict()
Examples
Here are some examples to demonstrate
the usage of the BaseModel class:

# Create a new BaseModel instance
base_model = BaseModel()

# Access the attributes
print(base_model.id)           # Output: <a unique identifier>
print(base_model.created_at)  # Output: <current date and time>
print(base_model.updated_at)  # Output: <current date and time>

# Update the attributes
base_model.created_at = datetime(2022, 1, 1)
base_model.updated_at = datetime(2022, 1, 2)
base_model.save()

# Convert the instance to a dictionary
base_model_dict = base_model.to_dict()
print(base_model_dict)
Inheritance
Other classes in the system can inherit from the BaseModel class
to inherit its attributes and methods. By doing so, these classes
can benefit from the common functionality provided by the BaseModel
class, such as unique identifiers and date/time tracking.

City Class
----------
This module contains the City class, which represents a city in the system.

Class Details
-------------
Class: City
Inheritance: BaseModel
Attributes:
state_id (str): The ID of the state associated with the city.
name (str): The name of the city.

Usage
-----
To use the City class, follow these steps:

1. Import the City class:
from models.city import City
2. Create an instance of the City class:
city = City()
3. Access and modify the attributes of the City instance:
city.state_id = "123"
city.name = "New York"
4. Save the changes to the instance:
city.save()

Examples
Here are some examples to demonstrate the usage of the City class:

# Create a new City instance
city = City()
city.state_id = "123"
city.name = "New York"

# Save the instance
city.save()

# Access the attributes
print(city.state_id)  # Output: 123
print(city.name)      # Output: New York

# Update the attributes
city.name = "Los Angeles"
city.save()

# Delete the instance
city.delete()
Inheritance
The City class inherits from the BaseModel class. This means that the
City class inherits all the attributes and methods from the BaseModel class,
which provides basic functionality for managing instances.

For more information on the BaseModel class, please refer to the BaseModel README.

Place Class
------------
This module contains the Place class, which represents a place or accommodation in the system.

Class Details
--------------
Class: Place
Inheritance: BaseModel
Attributes:
city_id (str): The ID of the city where the place is located.
user_id (str): The ID of the user who owns the place.
name (str): The name of the place.
description (str): A description of the place.
number_rooms (int): The number of rooms in the place.
number_bathrooms (int): The number of bathrooms in the place.
max_guest (int): The maximum number of guests allowed in the place.
price_by_night (int): The price per night for the place.
latitude (float): The latitude coordinate of the place's location.
longitude (float): The longitude coordinate of the place's location.
amenity_ids (list): A list of IDs of amenities available in the place.

Usage
To use the Place class, follow these steps:

1. Import the Place class:
from models.place import Place
2. Create an instance of the Place class:
place = Place()
3. Access and modify the attributes of the Place instance:
place.city_id = "123"
place.name = "Cozy Cottage"
place.number_rooms = 2
4. Save the changes to the instance:
place.save()
Examples
Here are some examples to demonstrate the usage of the Place class:

# Create a new Place instance
place = Place()
place.city_id = "123"
place.name = "Cozy Cottage"
place.number_rooms = 2

# Save the instance
place.save()

# Access the attributes
print(place.city_id)        # Output: 123
print(place.name)           # Output: Cozy Cottage
print(place.number_rooms)   # Output: 2

# Update the attributes
place.name = "Modern Apartment"
place.save()

# Delete the instance
place.delete()
Inheritance
The Place class inherits from the BaseModel class. This means that the
Place class inherits all the attributes and methods from the BaseModel
class, which provides basic functionality for managing instances.

For more information on the BaseModel class, please refer to the BaseModel README.


