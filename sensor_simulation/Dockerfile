FROM python:3.9

WORKDIR /app

COPY sensor_simulation.py /app/sensor_simulation.py

RUN pip install paho-mqtt

CMD ["python", "sensor_simulation.py"]
