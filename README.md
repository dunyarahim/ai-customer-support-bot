# ai-customer-support-bot

A simple Flask web app that simulates a customer support assistant using OpenAI's GPT model.

## Features
- User submits a question or issue
- GPT model replies with a helpful response in a customer support tone

## Setup

1. Clone the repo
2. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key"
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

## Example Use Case
- Online businesses can use this to answer frequent questions related to shipping, refunds, and product information.

## Requirements
Flask==2.3.2
openai==1.3.5
