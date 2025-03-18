# ACME_backend
![image](https://github.com/user-attachments/assets/6b627062-2a60-430f-a9dc-374940f01ab4)

## Setup

### Prerequisites

Python 3.x installed

Use pyenv

```
brew install pyenv
```

The use the .python-version

```
pyenv local
```

### Run the docker container

```bash
docker-compose up -d
```

### Setting Up a Virtual Environment

Create a Virtual Environment:

Navigate to your project directory and run:

```bash
python3 -m venv venv
```

### Activate the Virtual Environment:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
.\venv\Scripts\activate
```

## Install Required Python Packages

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Seed dummy data

```
python -m app.seed
```

### Run service

```
uvicorn app.main:app --reload
```
