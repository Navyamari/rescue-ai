import flask
from transformers import pipeline, __version__ as transformers_version

# Print Flask version
print("Flask version:", flask.__version__)

# Print Transformers version
print("Transformers version:", transformers_version)

# Test Transformers pipeline
nlp = pipeline("text-generation")
print("Transformers pipeline loaded successfully!")
