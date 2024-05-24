# Use official python image
FROM python:3.10

# Install the dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install the rest of the files
COPY . .

# Run comparison of models
CMD ["make", "compare_tune_test_random_forest"]
