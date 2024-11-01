# Set the Python version as a build-time argument
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Install Node.js and npm for Tailwind CSS
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Create a virtual environment
RUN python -m venv /opt/venv

# Set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install OS dependencies for the Django project
RUN apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create the app's code directory
RUN mkdir -p /code

# Set the working directory to the code directory
WORKDIR /code

# Copy the requirements file and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy the project code into the container's working directory
COPY ./src /code

# Install Tailwind CSS as a development dependency
COPY package.json /code/package.json
RUN npm install

# Run Tailwind CSS to generate output CSS files
RUN npx tailwindcss -i src/staticfiles/src/tailwind-input.css -o src/staticfiles/css/tailwind-output.css --minify

# Set up environment variables for Django
ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

ARG DJANGO_DEBUG=0
ENV DJANGO_DEBUG=${DJANGO_DEBUG}

# Database isn't available during build, so only run commands that don't need it
RUN python manage.py vendor_pull
RUN python manage.py collectstatic --noinput

# Set the Django default project name
ARG PROJ_NAME="home"

# Create a bash script to run the Django project
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJ_NAME}.wsgi:application --bind \"0.0.0.0:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# Make the bash script executable
RUN chmod +x paracord_runner.sh

# Clean up the apt cache to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the Django project via the runtime script when the container starts
CMD ./paracord_runner.sh
