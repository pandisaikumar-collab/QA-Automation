FROM python:3.10 # Base image
WORKDIR /app # Set working directory
COPY . /app # Copy project files
RUN pip install --no-cache-dir -r requirements.txt # Install dependencies
CMD ["pytest", "testcases/", "--html=htmlreports/report.html"] # Run pytest
