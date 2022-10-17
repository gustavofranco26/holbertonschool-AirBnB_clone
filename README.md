[![Airbnbconsole.png](https://i.postimg.cc/nhyPbv9H/Airbnbconsole.png)](https://postimg.cc/NKx4R2xV)
# AirBnB Clone - The Console
## Learning Objectives
------------
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Requirements
------------
### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## More Info
------------
### Execution

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
```
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
```
## Compilation & Output
----
The code will be executed this way:

``` $ ./console ```

- Any output must be printed on stdout

```
root@GUSCARDENASS:~/hs/holbertonschool-AirBnB_clone$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
	    print(obj)

		print("-- Create a new object --")
		my_model = BaseModel()
		my_model.name = "My_First_Model"
		my_model.my_number = 89
		my_model.save()
		print(my_model)
root@GUSCARDENASS:~/hs/holbertonschool-AirBnB_clone$ cat file.json
cat: file.json: No such file or directory
root@GUSCARDENASS:~/hs/holbertonschool-AirBnB_clone$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
	[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
root@GUSCARDENASS:~/hs/holbertonschool-AirBnB_clone$ cat file.json ; echo ""
	{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
root@GUSCARDENASS:~/hs/holbertonschool-AirBnB_clone$ ./test_save_reload_base_model.py
-- Reloaded objects --
	[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
	[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
root@GUSCARDENASS:~/hs/holbertonschool-AirBnB_clone$ ./test_save_reload_base_model.py
		-- Reloaded objects --
		[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
		[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
		-- Create a new object --
		[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
root@GUSCARDENASS:~/hs/holbertonschool-AirBnB_clone$
		{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}

```



## Attributes by Class
---
All classes that inherit from `BaseModel`

1. Class User

	Public class attributes:
	- `email`: string - empty string
	- `password`: string - empty string
	- `first_name`: string - empty string
	- `last_name`: string - empty string
2. Class State

	Public class attributes:
	- `name`: string - empty string

3. Class Amenity

	Public class attributes:
	- `name`: string - empty string

4. Class Place

	Public class attributes:
	- `city_id`: string - empty string: it will be the City.id
	- `user_id`: string - empty string: it will be the User.id
	- `name`: string - empty string
	- `description`: string - empty string
	- `number_rooms`: integer - 0
	- `number_bathrooms`: integer - 0
	- `max_guest`: integer - 0
	- `price_by_night`: integer - 0
	- `latitude`: float - 0.0
	- `longitude`: float - 0.0
	- `amenity_ids`: list of string - empty list: it will be the list of Amenity.id later

5. Class Review

	Public class attributes:
	- `place_id`: string - empty string: it will be the Place.id
	- `user_id`: string - empty string: it will be the User.id
	- `text`: string - empty string

## Opcodes from Console
---
| Opcode | Description                    |
| ------------- | ------------------------------ |
| `quite`   | Quit command to exit the program     |
| `create`      | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id|
| `show`   | Show string representation of an instance based on the class name and id.  |
| `destroy`      | Deletes an instance based on the class name and id.|
| `all`   | Prints all string representation of all instances based or not on the classnam. |
| `update`      | Update an instance based on the class name and id by adding or updating attribute (save the change into the JSON file. |

## Examples to use the console.py
---
In this section the operation of the console will be shown
```
(hbnb)create User
db53f522-7d37-4f62-adb5-520ec7dbfaf4

(hbnb)create Place
5c7521b5-702c-4a4e-b67c-b7361dfb3cb0

(hbnb)create Place
b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9

(hbnb)create Place
7c115662-fefa-417f-8183-2e146548a83f

(hbnb)all
["[User] (db53f522-7d37-4f62-adb5-520ec7dbfaf4) {'id': 'db53f522-7d37-4f62-adb5-520ec7dbfaf4', 'created_at': datetime.datetime(2022, 7, 1, 10, 23, 8, 995907), 'updated_at': datetime.datetime(2022, 7, 1, 10, 23, 8, 995915)}", "[Place] (5c7521b5-702c-4a4e-b67c-b7361dfb3cb0) {'id': '5c7521b5-702c-4a4e-b67c-b7361dfb3cb0', 'created_at': datetime.datetime(2022, 7, 1, 10, 23, 12, 735579), 'updated_at': datetime.datetime(2022, 7, 1, 10, 23, 12, 735600)}", "[Place] (b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9) {'id': 'b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9', 'created_at': datetime.datetime(2022, 7, 1, 10, 23, 15, 8285), 'updated_at': datetime.datetime(2022, 7, 1, 10, 23, 15, 8293)}", "[Place] (7c115662-fefa-417f-8183-2e146548a83f) {'id': '7c115662-fefa-417f-8183-2e146548a83f', 'created_at': datetime.datetime(2022, 7, 1, 10, 23, 17, 27311), 'updated_at': datetime.datetime(2022, 7, 1, 10, 23, 17, 27351)}"]

(hbnb)all Place
[Place] (5c7521b5-702c-4a4e-b67c-b7361dfb3cb0) {'id': '5c7521b5-702c-4a4e-b67c-b7361dfb3cb0', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 12, 735579), 'updated_at': datetime.datetime(2022, 10, 15, 10, 23, 12, 735600)}
[Place] (b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9) {'id': 'b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 15, 8285), 'updated_at': datetime.datetime(2022, 10, 15, 10, 23, 15, 8293)}
[Place] (7c115662-fefa-417f-8183-2e146548a83f) {'id': '7c115662-fefa-417f-8183-2e146548a83f', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 17, 27311), 'updated_at': datetime.datetime(2022, 10, 15, 10, 23, 17, 27351)}

(hbnb)update 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0 name "Cesar Evanan"

(hbnb)show Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0
[Place] (5c7521b5-702c-4a4e-b67c-b7361dfb3cb0) {'id': '5c7521b5-702c-4a4e-b67c-b7361dfb3cb0', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 12, 735579), 'updated_at': datetime.datetime(2022, 10, 15, 10, 24, 59, 829520), 'name': 'Cesar Evanan'}

(hbnb)update Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0 max_guest 6

(hbnb)show Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0
[Place] (5c7521b5-702c-4a4e-b67c-b7361dfb3cb0) {'id': '5c7521b5-702c-4a4e-b67c-b7361dfb3cb0', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 12, 735579), 'updated_at': datetime.datetime(2022, 10, 15, 10, 25, 47, 295161), 'name': 'Cesar Evanan', 'max_guest': 6}

(hbnb)update Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0 latitude -34.603722

(hbnb)update Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0 longitude -58.381592

(hbnb)show Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0
[Place] (5c7521b5-702c-4a4e-b67c-b7361dfb3cb0) {'id': '5c7521b5-702c-4a4e-b67c-b7361dfb3cb0', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 12, 735579), 'updated_at': datetime.datetime(2022, 10, 15, 10, 28, 21, 913195), 'name': 'Cesar Evanan', 'max_guest': 6, 'latitude': -34.603722, 'longitude': -58.381592}

(hbnb)update Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0 amenity_ids ["pool", "tv", "internet"]

(hbnb)show Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0
[Place] (5c7521b5-702c-4a4e-b67c-b7361dfb3cb0) {'id': '5c7521b5-702c-4a4e-b67c-b7361dfb3cb0', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 12, 735579), 'updated_at': datetime.datetime(2022, 10, 15, 10, 29, 43, 866028), 'name': 'Cesar Evanan', 'max_guest': 6, 'latitude': -34.603722, 'longitude': -58.381592, 'amenity_ids': ['pool', 'tv', 'internet']}

(hbnb)all Place
[Place] (5c7521b5-702c-4a4e-b67c-b7361dfb3cb0) {'id': '5c7521b5-702c-4a4e-b67c-b7361dfb3cb0', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 12, 735579), 'updated_at': datetime.datetime(2022, 10, 15, 10, 29, 43, 866028), 'name': 'Cesar Evanan', 'max_guest': 6, 'latitude': -34.603722, 'longitude': -58.381592, 'amenity_ids': ['pool', 'tv', 'internet']}
[Place] (b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9) {'id': 'b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 15, 8285), 'updated_at': datetime.datetime(2022, 10, 15, 10, 23, 15, 8293)}
[Place] (7c115662-fefa-417f-8183-2e146548a83f) {'id': '7c115662-fefa-417f-8183-2e146548a83f', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 17, 27311), 'updated_at': datetime.datetime(2022, 10, 15, 10, 23, 17, 27351)

(hbnb)destroy Place 5c7521b5-702c-4a4e-b67c-b7361dfb3cb0

(hbnb)all Place
[Place] (b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9) {'id': 'b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 15, 8285), 'updated_at': datetime.datetime(2022, 10, 15, 10, 23, 15, 8293)}
[Place] (7c115662-fefa-417f-8183-2e146548a83f) {'id': '7c115662-fefa-417f-8183-2e146548a83f', 'created_at': datetime.datetime(2022, 10, 15, 10, 23, 17, 27311), 'updated_at': datetime.datetime(2022, 10, 15, 10, 23, 17, 27351)}
```
## Examples to use the console.py by class name
---

In this section, the operation of the console will be shown by calling each method with the respective class.

## How to use:
- Retrieve all instances of a class by using: `<class name>.all()`
- Retrieve the number of instances of a class: `<class name>.count()`
- Retrieve an instance based on its ID: `<class name>.show(<id>)`
- Destroy an instance based on his ID: `<class name>.destroy(<id>)`
- Update an instance based on his ID: `<class name>.update(<id>, <attribute name>, <attribute value>)`

```
(hbnb)create Place
e5954ba0-388a-40e4-809c-1e5a372a1c77

(hbnb)create User
8952c825-c6d1-4be5-89ba-e6bcb78792f7

(hbnb)create Place
efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6

(hbnb)create Place
2ba37c8a-f7ce-4878-96ec-7170bca9fef2

(hbnb)Place.all()
[Place] (e5954ba0-388a-40e4-809c-1e5a372a1c77) {'id': 'e5954ba0-388a-40e4-809c-1e5a372a1c77', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 28, 677181), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 28, 677207)}
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406017)}
[Place] (2ba37c8a-f7ce-4878-96ec-7170bca9fef2) {'id': '2ba37c8a-f7ce-4878-96ec-7170bca9fef2', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658069), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658076)}

(hbnb)User.all()
[User] (8952c825-c6d1-4be5-89ba-e6bcb78792f7) {'id': '8952c825-c6d1-4be5-89ba-e6bcb78792f7', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 30, 676093), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 30, 676102)}

(hbnb)User.count()
1

(hbnb)Place.show("2ba37c8a-f7ce-4878-96ec-7170bca9fef2")
[Place] (2ba37c8a-f7ce-4878-96ec-7170bca9fef2) {'id': '2ba37c8a-f7ce-4878-96ec-7170bca9fef2', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658069), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658076)}

(hbnb)Place.count()
3

(hbnb)Place.all()
[Place] (e5954ba0-388a-40e4-809c-1e5a372a1c77) {'id': 'e5954ba0-388a-40e4-809c-1e5a372a1c77', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 28, 677181), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 28, 677207)}
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406017)}
[Place] (2ba37c8a-f7ce-4878-96ec-7170bca9fef2) {'id': '2ba37c8a-f7ce-4878-96ec-7170bca9fef2', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658069), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658076)}

(hbnb)Place.destroy("e5954ba0-388a-40e4-809c-1e5a372a1c77")

(hbnb)Place.count()
2

(hbnb)Place.all()
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406017)}
[Place] (2ba37c8a-f7ce-4878-96ec-7170bca9fef2) {'id': '2ba37c8a-f7ce-4878-96ec-7170bca9fef2', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658069), 'updated_at': datetime.datetime(2022, 10, 15, 10, 34, 53, 658076)}

(hbnb)Place.update("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6", "name", "Franco Cardenas")

(hbnb)Place.show("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6")
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 10, 15, 10, 39, 49, 536812), 'name': 'Franco'}

(hbnb)Place.update("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6", "max_guest", "5")

(hbnb)Place.show("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6")
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 10, 15, 10, 40, 46, 576557), 'name': 'Franco', 'max_guest': 5}

(hbnb)Place.update("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6", "latitude", "40.416775")

(hbnb)Place.update("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6", "longitude", "-3.703790")

(hbnb)Place.show("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6")
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 10, 15, 10, 42, 41, 978670), 'name': 'Luis', 'max_guest': 5, 'latitude': 4.0, 'longitude': -3.703790}

(hbnb)Place.update("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6", "amenity_ids", ["pool", "sauna", "karaoke", "bar"])

(hbnb)Place.show("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6")
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 10, 15, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 10, 15, 10, 45, 50, 119480), 'name': 'Franco', 'max_guest': 5, 'latitude': 4.0, 'longitude': '-', 'amenity_ids': ['pool', 'sauna', 'karaoke', 'bar']}

```



## Authors
---
- Cesar Evanan - (https://github.com/Cesar240998)
- Franco Cardenas - (https://github.com/gustavofranco26)
