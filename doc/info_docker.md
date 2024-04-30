# Docker. Basic commands
## Linux post-install steps
[These optional post-installation procedures](https://docs.docker.com/engine/install/linux-postinstall/) shows you how to configure your Linux host machine to work better with Docker. For example, managing docker with [a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

### Configure Docker to start on boot
```bash
sudo systemctl enable docker

# To disable this behavior, use disable instead.
sudo systemctl disable docker
```

### Clear all Docker unused objects (images, containers, networks, local volumes)
```bash
docker system prune # Clear all
docker system prune -a # Clear all (includes unused and dangling containers)

# By default, volumes are not removed to prevent important data from being deleted if there is currently no container using the volume. Use the `--volumes` flag when running the command to prune volumes: `docker system prune -a --volumes`

docker image prune # Clear unused images
docker container prune # Clear unused containers
docker volume prune # Clear unused volumes
docker network prune # Clear unused networks
```

## Docker Compose. Basic commands
More info about Docker Compose commands at [docker compose reference](https://docs.docker.com/compose/reference/).

```bash
# Basic. All containers or specific container: <container>
## Starts existing containers for a service.
docker compose start <container>

## Restarts existing containers/container for a service.
docker compose restart <container>

## Stops running containers without removing them.
docker compose stop <container>

## Pauses running containers of a service.
docker compose pause <container>

## Unpauses paused containers of a service.
docker compose unpause <container>

# Display the logs of a container. Is it possible to retrieve only the last n seconds or other
docker logs [--since 60s]  <container> -f 

## Lists containers.
docker compose ps

## Remove all docker compose project
docker compose rm <container>


# Build.
## Builds, (re)creates, starts, and attaches to containers for a service.
docker compose [-f <docker compose-file>] up

## Build & up all the containers.
docker compose [-f <docker compose-file>] up -d --build

## Build & up an specific container.
docker compose [-f <docker compose-file>] up -d --build <container>

## To avoid using a cache of the previous build while creating a new image.
docker compose [-f <docker compose-file>] build --no-cache

## Build a project with a specific Docker Compose prefix.
docker compose [-f <docker compose-file>] -p <my_project> up -d --build

## Log the build
docker compose build --no-cache &> docker_build.log


# Down
# Stops containers and removes containers, networks, volumes, and images created by up.
docker compose [-p <my_project>] down
```

