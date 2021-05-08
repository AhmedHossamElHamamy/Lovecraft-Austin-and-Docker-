(1) the first book is Beyond_the_Wall_of_Sleep
(2) the second book is Pride and Prejudice
(3) file.py :the file which have python code to find simliar words between books
(4) Dockerfile: it's very important to make the docker image
------------------------------------------------------------------------------
In file.py ,I put the path of the two books on my laptob in it so you should change the path to work successfully with you.
Usig terminal ubuntu 18.04 to make docker image:
(1) docker build . -t  ahmed/docker-app
(2) docker run ahmed/firstapp
-------------------------------------------------------------------------------
The docker image will work now.
