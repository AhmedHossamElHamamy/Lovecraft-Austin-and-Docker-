FROM python:3
COPY . /home/ahmed/Assignment_cloud/Docker
WORKDIR /home/ahmed/Assignment_cloud/Docker
CMD ["python", "file.py"]
