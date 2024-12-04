FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies
RUN apt update -y && apt install awscli -y
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to the outside
EXPOSE 8080

# Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]