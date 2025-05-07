# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LATEST_RELEASE_WITH_LINUX_DISTRO=134.0.3124.51

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft Edge repository and install Microsoft Edge
RUN wget -q -O - https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list' \
    && apt-get update \
    && apt-get install -y microsoft-edge-stable

# Download and install EdgeDriver
RUN wget -q "https://msedgedriver.azureedge.net/${LATEST_RELEASE_WITH_LINUX_DISTRO}/edgedriver_linux64.zip" \
    && unzip edgedriver_linux64.zip -d /usr/local/bin/ \
    && rm edgedriver_linux64.zip

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]