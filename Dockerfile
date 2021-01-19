FROM python:3.9.1
ADD . /colors-generator
WORKDIR /colors-generator
RUN apt update
RUN apt install -y libgl1-mesa-glx
RUN pip install opencv-python numpy
CMD python ColorsGenerator.py