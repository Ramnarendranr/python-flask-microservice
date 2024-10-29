# Base image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY lambda_function.py .

# Expose the port Flask runs on
EXPOSE 5001

# Define command to run the Flask app (needed for Lambda function)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]

