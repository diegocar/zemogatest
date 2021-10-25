# Importants Things about this test

I'm Diego Alberto Carvajal Cárdenas, in this  [repository](https://github.com/diegocar/zemogatest) you will find an python app that was develop woth **Flask** (an python framework to develop an api), and the docker file that will allows you to execute the api.

## Files
- **app.py** contains the python api.
- **requirements.txt** contains a short list of requirements for the installation inside docker.
- **Dockerfile** contains the docker steps to create the image.
- **.github/workflows** contains the github actions to the docker image creation.

## How to execute it 

To run this application it is necessary to download the repository, once it is downloaded, you must run the following command `docker build -t zemogatest .` This line will create the docker image that will be used immediately afterwards. After that you need to execute the following line: `docker run -p 5000:5000 zemogatest` This one will run the container with the `zemogatest` image.

Now you will be able to connect to the api through `http://0.0.0.0:5000/user/<any_name>`  so the api will respond with a message like `'Username: any_name'`

### Aditional info
- A **big challenge** was to find a way to make the docker image stable, because the operating system I used was mainly windows which made it very difficult to integrate the application with docker. Finally I opted better to use docker from a linux virtual machine which allowed me to have better management of docker and not present so much instability.
- For the **handling of environment variables** my option would have been to handle this as a variable for docker, which would allow that at the moment of raising the container that would run the application it would be able to detect in which type of environment it is running. Another option would be to configure the docker image to be able to obtain the information of the environment from AWS and based on this information raise the application correctly.
