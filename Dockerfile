# Use a lightweight Python base image. It comes with Python pre-installed.
FROM python:3.9-slim-buster 

# Set the working directory inside the container.
WORKDIR /app 

# Copy requirements.txt first to leverage Docker's build cache.
# If requirements.txt doesn't change, Docker can reuse the layer for pip install.
COPY requirements.txt . 

# Install dependencies from requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the rest of the application code into the container.
COPY . . 

# Expose the port your Flask app will listen on. Flask defaults to 5000.
EXPOSE 5000 

# Define the command to run when the container starts.
# Use exec form to ensure signals are handled correctly.
CMD ["python", "app.py"] 
