# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Add Google's official GPG key
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

# Set up the Chrome repository
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && chmod +x chromedriver \
    && mv -f chromedriver /usr/local/bin/chromedriver \
    && rm chromedriver_linux64.zip

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Create and activate virtual environment
RUN python -m venv myenv
ENV PATH="/app/myenv/bin:$PATH"

# Install Python dependencies
RUN /app/myenv/bin/pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app with Gunicorn
CMD ["/app/myenv/bin/gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "600", "app:app"]