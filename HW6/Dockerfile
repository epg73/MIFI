FROM ubuntu
WORKDIR /test
COPY requirements.txt .
RUN apt update && apt upgrade -y
RUN apt install python3 -y
RUN apt install pip -y
RUN apt install iputils-ping -y
RUN apt install mc -y
RUN apt install net-tools -y
RUN pip install requests
RUN pip install requirements.txt






