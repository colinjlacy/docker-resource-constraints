# Docker Resource Limits

This repo contains files necessary for experimenting with two of the resource limits you can set while running Docker images:
- `cpu` - the amount of CPU cores available to the different processes running in the Docker container
- `memory` - the amount of memory allocated to the parent process (and its child processes) running in the Docker container

## Running the Simulation Images

The images that I used to run through the demo in [this video](https://youtu.be/RcuiszNNm_g) are public.

If you want to test the out-of-memory simulator:
```
docker run --rm -t -m 256m ghcr.io/colinjlacy/docker-oom-simulator:0.1
```

If you want to test the CPU utilization simulator:
```
docker run --rm -t \
  --cpus=1 \
  -e PROCESS_MULTIPLIER=5 \
  ghcr.io/colinjlacy/docker-cpu-simulator:0.1
```

Be sure to check out [the docs](https://docs.docker.com/engine/containers/resource_constraints/) for more info on resource constraints.
