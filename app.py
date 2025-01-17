from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Set up the tracer provider
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "flask111-users"}))
)
tracer_provider = trace.get_tracer_provider()

# Configure Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

# Add the Jaeger exporter to the tracer provider
tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

# Create a FastAPI app and instrument it
# FastAPIInstrumentor.instrument_app(app)

# Create a Flask app
app = Flask(__name__)
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Instrument the Flask application
FlaskInstrumentor().instrument_app(app)
FlaskInstrumentor().instrument(enable_commenter=True, commenter_options={})


@app.route("/")
def hello_world():
    return "Hello, OpenTelemetry!"

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

