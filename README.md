# Docker Resource Limits

This repo contains files necessary for experimenting with two of the resource limits you can set while running Docker images:
- `cpu` - the amount of CPU cores available to the different processes running in the Docker container
- `memory` - the amount of memory allocated to the parent process (and its child processes) running in the Docker container

## Testing Memory Exhaustion

The file `mem.py`