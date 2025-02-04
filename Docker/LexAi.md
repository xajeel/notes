# LexAi Application Dockerizing 

Create a `Dockerfile` in the root directory of the project. Then add the following lines in the `Dockerfile`.

```docker 
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y git pkg-config default-mysql-client libmariadb-dev gcc python3-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

```

---

## File Explanation

- Getting python image with particular version.

``` docker
FROM python:3.10-slim
```
- Setting a working directory

```docker
WORKDIR /app
```
- Copy the `requirements.txt` file to the working directory `/app`

```docker
COPY requirements.txt .
```
- Installing dependencies used in the project.

```docker
RUN apt-get update && apt-get install -y git pkg-config default-mysql-client libmariadb-dev gcc python3-dev
```
- Installing `requirements` of the application

```docker
RUN pip install --no-cache-dir -r requirements.txt
```
- Copying all the remaining files to the `/app` directory

```docker
COPY . .
```
- Exposing a specific port for the application 

```docker
EXPOSE 5000
```
- Setting python environment variable (optional)

```docker
ENV PYTHONUNBUFFERED=1
```
- Running the CMD command that will run the application 

```docker
CMD ["python", "main.py"]
```

---

## Building Image

- The command `docker build -t flask_app .` is used to build a Docker image from a Dockerfile in the current directory.

```docker
docker build -t flask_app .
```
`docker`: This is the command-line interface for interacting with Docker.

`build`: This command tells Docker to build an image. It processes the instructions in the Dockerfile and creates a Docker image from it.

`-t flask_app`: The -t option allows you to tag the image with a name. In this case, the image will be tagged as flask_app. 

You can think of this as naming the image, which will be useful when you later run or manage the image. The tag is optional, but it’s recommended to give your image a meaningful name (and optionally a version).

For example, if you wanted to add a version, you could tag it like this: `flask_app:v1.0`.

`.`: The period (dot) represents the current directory. It tells Docker to look for the Dockerfile in the current directory.

---

## Running a container

The command is used to run a Docker container from an image.

```docker
docker run -p 5000:5000 -v D:/medtronix-system/LexiAi/LexAi-3.0/lexai.db:/app/lexai.db flask_app
```

`docker run`: This command runs a container from a specified Docker image.

`-p 5000:5000`: This option maps port 5000 on your host machine (your computer) to port 5000 on the Docker container.

`-v D:/.../lexai.db`: This option is for mounting a volume. It maps a file or directory from your local system to a location inside the container.

- On the left side (`D:/.../lexai.db`), you specify the path to the SQLite database on your host machine.

- On the right side (`/app/lexai.db`), you specify the path inside the container where the SQLite database should be mounted.

`flask_app`: This is the name of the Docker image you're running.
