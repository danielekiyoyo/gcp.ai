# gcp.ai
GCP Projects AI for Daniel Ekiyoyo 

Refer to:
https://www.kaggle.com/code/kaggle5daysofai/day-1a-from-prompt-to-action

https://aistudio.google.com/api-keys

A Step-by-Step Guide to Using Google’s Agent Development Kit (ADK)
https://medium.com/@munsifrazaofficial/a-step-by-step-guide-to-using-googles-agent-development-kit-adk-73dd467cae44


How to Create a Virtual Environment in Python
https://www.hostinger.com/uk/tutorials/how-to-create-a-python-virtual-environment

Python Quickstart for ADK
https://google.github.io/adk-docs/get-started/python/#installation


# create virtual environment
python -m venv de_venv

#activate virtual environment
.\de_venv\Scripts\activate

# install
pip install google-adk
adk --version 
pip install google-adk[all]  # Installs all optional dependencies

# create agent
adk create de_agent

# run agent
adk web
adk run de_agent

# deactivate virtual environment
deactivate