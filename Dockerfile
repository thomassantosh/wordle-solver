# Base image
FROM ubuntu:latest

# Install python
RUN apt-get update && apt-get install -y python3.10

# Copy relevant files
COPY solver.py .
COPY dictionary.txt .

#ENTRYPOINT ["/bin/bash"]


#- To build the docker image locally, run `docker build --no-cache -t "thomassantosh:wordle-solver" .`
#- To run the container locally, run `docker run -it --rm --entrypoint=/bin/bash thomassantosh:wordle-solver`.
#- When in the container, run the script `/usr/bin/python3.10 solver.py`.
