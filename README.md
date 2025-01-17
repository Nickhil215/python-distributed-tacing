# Flask_API with OpenTelemetry and Jaeger

This project demonstrates how to integrate OpenTelemetry with a Flask_API application to collect telemetry data (traces) and visualize them using Jaeger.

## Overview

The application is a simple Flask_API web service instrumented with OpenTelemetry to collect traces. Jaeger is used as the observability backend to visualize the traces, helping in monitoring and troubleshooting the application.

### Looks like this

- Flask_API![1710975776341](image/README/1710975776341.png)
- Jaeger![1710975899908](image/README/1710975899908.png)

## Getting Started

### Prerequisites

- Python 3.6+
- Docker
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Nickhil215/python-distributed-tacing.git
   cd https://github.com/Nickhil215/python-distributed-tacing.git
   ```
2. **Create and activate a virtual environment (optional)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start Jaeger with Docker**

   Run Jaeger using Docker with the following command:

   ```bash
   docker run -d --name jaeger \
     -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 \
     -p 5775:5775/udp \
     -p 6831:6831/udp \
     -p 6832:6832/udp \
     -p 5778:5778 \
     -p 16686:16686 \
     -p 14250:14250 \
     -p 14268:14268 \
     -p 14269:14269 \
     -p 9411:9411 \
     jaegertracing/all-in-one:latest
   ```

   Access the Jaeger UI at `http://localhost:16686`.
2. **Run the Flask_API application**

   ```bash
   uvicorn app:app --reload
   ```

   The Flask_API application will be available at `http://localhost:8000`.

### Running the Application with docker-compose

1. Change the `agent_host_name = "jaeger"`  in app.py

   ```
   jaeger_exporter = JaegerExporter(
   agent_host_name="jaeger",
   agent_port=6831,
   )
   ```
2. Start Jaeger with `docker-compose up --build`

### Viewing Traces in Jaeger

- After the application is running and serving requests, navigate to the Jaeger UI (`http://localhost:16686`).
- Select your service from the "Service" dropdown menu and click on "Find Traces" to view the collected traces.

## Contributing

- **AUTHOR** - **AAMER**
- YouTube - [Prograamer YouTube Channel](https://www.youtube.com/@prograamer)
# python-distributed-tacing
