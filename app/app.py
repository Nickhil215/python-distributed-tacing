from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Set up the tracer provider
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "Fastapi-users"}))
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
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)


# Define a simple route
@app.get("/")
async def read_root():
    return {"Hello": "World"}
