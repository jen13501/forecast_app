FROM python:3.10-slim

# Install cron & other settings
# RUN apt-get update && \
#     apt-get install -y cron && \
#     rm -rf /var/lib/apt/lists/*
# COPY ./retrieve_forecasts_cron /etc/cron.d/retrieve_forecasts_cron
# COPY ./retrieve_forecasts.py /retrieve_forecasts.py
# RUN chmod +x /retrieve_forecasts.py
# RUN chmod 0644 /etc/cron.d/retrieve_forecasts_cron

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY app.py database.py weather_gov_api.py Weather.db requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the app
CMD ["python3", "app.py"]
