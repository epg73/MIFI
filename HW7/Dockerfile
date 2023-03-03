FROM ubuntu
WORKDIR /Develop
COPY requirements.txt /Develop
RUN apt update && apt upgrade -y
RUN apt install python3 -y
RUN apt install pip -y
RUN apt install iputils-ping -y
RUN apt install mc -y
RUN apt install net-tools -y
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN apt install curl -y
CMD uvicorn server:app --port 8000 --reload --host 0.0.0.0



