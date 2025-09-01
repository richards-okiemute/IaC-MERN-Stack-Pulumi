# Deploying a MERN Stack Application using Pulumi IaC
Pulumi IaC project to deploy a MERN stack application on Docker.

![Pulumi deployment resources graphical view](https://github.com/richards-okiemute/IaC-MERN-Stack-Pulumi/blob/main/images/pulumi%20resource%20graphical%20view.PNG)


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

### Install Resource Provider (Pulumi_Docker provider for Python)
Use the command below to activate a Python virtual environment (venv) and then install the pulumi_docker provider

```bash
source venv/bin/activate
pip3 install pulumi_docker
```
You should see output showing the provider package being installed, just like for any Python package install. 
Use the command below to add the package to the `requirements.txt` file by adding `pulumi_docker` on a new line at the end of the file.

```bash
$ echo "pulumi_docker" >> requirements.txt
```


### Inspect your new project
Open the `__main__.py` file and review it's content. 

```bash
"""A Python Pulumi program"""

import pulumi
```

Refer to the [`__main__.py`](https://github.com/richards-okiemute/IaC-MERN-Stack-Pulumi/blob/main/__main__.py) file for the complete python code.

Note: The python code references the Remote Docker images used to run the container for the application

### Configuring and Provisioning Containers

Pass/run these environment variables in vai your terminal
```bash
pulumi config set pulumi-app:frontendPort 3001
pulumi config set pulumi-app:backendPort 3000
pulumi config set pulumi-app:mongoPort 27017
pulumi config set set pulumi-app:mongoHost mongodb://mongo:27017
pulumi config set pulumi-app:database cart
pulumi config set pulumi-app:nodeEnvironment development
pulumi config set pulumi-app:protocol http://
```

This will automatically populate the [`python.dev.yaml`](https://github.com/richards-okiemute/IaC-MERN-Stack-Pulumi/blob/main/Pulumi.dev.yaml) file with the application confiuration
![pulumi application environment config.](https://github.com/richards-okiemute/IaC-MERN-Stack-Pulumi/blob/main/images/environment-config.PNG)

### Deploy The Application Using Pulumi Up
Now, you can deploy the application using the pulumi command below:

```bash
pulumi up
```
See screenshot below:
![pulumi up](https://github.com/richards-okiemute/IaC-MERN-Stack-Pulumi/blob/main/images/pulumi%20up.PNG)
### Accessing the Application
Open a browser to `http://localhost:3001` and you should see that the Boba Tea shop is now deployed.

See screenshot below:
![app deployed with pulumi](https://github.com/richards-okiemute/IaC-MERN-Stack-Pulumi/blob/main/images/puluminus.PNG)

