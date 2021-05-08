the first book is Beyond_the_Wall_of_Sleep
the second book is Pride and Prejudice
file.py :the file which have python code to find simliar words between books
Dockerfile: it's very important to make the docker image
------------------------------------------------------------------------------
In file.py ,I put the path of the two books on my laptob in it so you should change the path to work successfully with you.
Usig terminal ubuntu 18.04 to make docker image:
docker build . -t  ahmed/docker-app
docker run ahmed/firstapp
-------------------------------------------------------------------------------
The docker image will work now.
