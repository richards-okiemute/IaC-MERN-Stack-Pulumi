# Deploying a MERN Stack Application using Pulumi IaC
Pulumi IaC project to deploy a MERN stack application on Docker.



## Technologies Used
* Pulumi: For Infrastructure as Code (IaC).

* Docker: Containerization platform (an understanding of Docker is required).

* MERN Stack: The application stack. This includes:

  * MongoDB: The database technology.

  * Express.js: The backend framework.

  * React: The frontend library.

  * Node.js: The runtime environment.

* Git/GitHub: Version control and remote repository management.

* Python: The programming language used with Pulumi.


##  Installation and Setup
Make sure you have the following tools installed:

* Node.js (with npm)
* Docker
* Pulumi
* Pulumi account nad PAT

### Creating The Pulumi Project
Create a directory for the app and change into the directory by using the commands below in your terminal:

```bash
$ mkdir pulumi-app
$ cd pulumi-app
```
### Initialize your project
Run the command below to initialize the diectory with your desired programming language

```bash
$ pulumi new python -y
```

### Inspect your new project
Open the `__main__.py` file and review it's content. 

```bash
"""A Python Pulumi program"""

import pulumi
```

Refer to the __main__.py file for the complete python code.




