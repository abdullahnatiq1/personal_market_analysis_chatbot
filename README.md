# Intoduction

An advanced Retrieval-Augmented Generation (RAG) chatbot designed to transform static market research into interactive intelligence. Built with LangChain and Groq, this system moves beyond simple search by using a ReAct Agent to reason through complex market data and provide structured, actionable insights.

# Overview

Traditional PDF readers often lose context or fail to connect related data points across pages. This project solves that by implementing an autonomous agent that can:

• Analyze: Scrutinize dense market_analysis.pdf documents.

• Reason: Use the ReAct (Reason + Act) framework to decide when to search and how to interpret findings.

• Retrieve: Utilize ChromaDB and semantic embeddings for high-speed, relevant data fetching.

• Execute: Leverage Llama 3.3 (70B) via Groq for near-instant, high-reasoning responses.

## Technical Stack

• Framework: LangChain (Agentic Workflow)

• LLM: Groq Cloud (llama-3.3-70b-versatile)

• Vector Database: ChromaDB

• Embeddings: all-MiniLM-L6-v2

• Language: Python 3.x

# Get Started

## Prerequsites

we need GROQ API KEY for this project

## Setting up Environment

first create .env file in the root of this project and add GROQ_API_KEY

```
GROQ_API_KEY=YOUR_API_KEY
```

## Create and Activate Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```
