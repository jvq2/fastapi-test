# 1 Week Example Project
This projects goal is to showcase 1 weeks worth of effort (minus continuous recruiter calls and interviews) using a specific set of tech.

### Project specifications
The project requester asked for me to focus on the following items:
* FastAPI
* pydantic
* asyncio
* mongoengine

### Notes
#### Mongoengine
It appears `mongoengine` does not support `asyncio`. In order to fully leverage `asyncio`, it may be worth while to look into something like `motorengine`. But since `mongoengine` was requested to be used, we will stick with it.

----
## Setup
### Install docker / docker-compose
You will first need to install docker and docker-compose.

[Installation instructions for Docker](https://docs.docker.com/get-docker/)
[Installation instructions for docker-compose](https://docs.docker.com/compose/install/)

## Running the app
Once docker and docker-compose are installed, you can start the application stack by running:
```bash
docker-compose up
```

If you want to want to keep the containers running in the background without taking over your terminal, you can add the `-d` flag to the above command like so.
```bash
docker-compose up -d
```

After that, you can watch the logs with `docker-compose logs -f` or turn off the containers by running `docker-compose down`.


### [Optional] For Development: Setup python virtual environment
All testing and development on the application is done outside of the docker environment and contained inside of a virtual environment.
This allows the app to maintain its exact library versions and not conflict with any other versions install on the OS. 

```bash
# Feel free to replace the last venv here to name your virtual environment something else
python3 -m venv venv/

# The following line turns on the virtual environment. You will need to do this every time you open a new terminal to this project.
. venv/bin/activate
```

You should now see a `(venv)` prefix on your bash prompt like so:
```bash
(venv) user@host:~/project$
```

To deactivate the virtual environment, run the following command.
```bash
deactivate
```

# Run the App
