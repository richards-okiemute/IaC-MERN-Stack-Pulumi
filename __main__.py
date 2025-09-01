"""A Python Pulumi program"""

import pulumi
import pulumi_docker as docker

# Get configuration values

config = pulumi.Config()
frontend_port = config.require_int("frontendPort")
backend_port = config.require_int("backendPort")
mongo_port = config.require_int("mongoPort")
mongo_host = config.require("mongoHost")  # Note that strings are the default, so it's not `config.require_str`, just `config.require`.
database = config.require("database")
node_environment = config.require("nodeEnvironment")
protocol = config.require("protocol")


stack = pulumi.get_stack()


# Pull the backend image

backend_image_name = "backend"
backend = docker.RemoteImage(
        f"{backend_image_name}_image",
        name="pulumi/tutorial-pulumi-fundamentals-backend:latest",
        )

# Pull the frontend image

front_image_name = "frontend"
frontend = docker.RemoteImage(
        f"{front_image_name}_image",
        name="pulumi/tutorial-pulumi-fundamentals-frontend:latest",
        )

# Pull the MongoDB image

mongo_image = docker.RemoteImage(
        "mongo_image", name="pulumi/tutorial-pulumi-fundamentals-database:latest",
        )
network = docker.Network("docker network", name=f"services_{stack}")

# Create the MongoDB container

mongo_container = docker.Container(
	"mongo_container", name=f"mongo-{stack}",
	image=mongo_image.repo_digest,
        ports=[docker.ContainerPortArgs(internal=mongo_port, external=mongo_port)],
        networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
)

# Create the backend container

backend_container = docker.Container(
	"backend_container", name=f"backend-{stack}",
	image=backend.repo_digest,
        ports=[docker.ContainerPortArgs(internal=backend_port, external=backend_port)],
        envs=[
            f"DATABASE_HOST={mongo_host}",
            f"DATABASE_NAME={database}",
            f"NODE_ENV={node_environment}",
         ],
        networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
        opts=pulumi.ResourceOptions(depends_on=[mongo_container]),
)

# Create the frontend container

frontend_container = docker.Container(
	"frontend_container", name=f"frontend-{stack}",
	image=frontend.repo_digest,
        ports=[docker.ContainerPortArgs(internal=frontend_port, external=frontend_port)],
        envs=[
        f"PORT={frontend_port}",
        f"HTTP_PROXY=backend-{stack}:{backend_port}",
        f"PROXY_PROTOCOL={protocol}",
         ],
        networks_advanced=[docker.ContainerNetworksAdvancedArgs(name=network.name)],
)

