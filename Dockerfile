# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code
COPY . .

# Define the command to run the bot
CMD ["python", "bot.py"]
