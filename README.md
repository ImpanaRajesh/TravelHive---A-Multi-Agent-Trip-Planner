# ✈️ TravelHive — Multi-Agent Travel Planner Powered by LangGraph

TravelHive AI is an open-source travel planning assistant that converts a simple natural-language request into a complete, ready-to-use travel plan — flight options, hotel picks, and a day-by-day itinerary — all generated automatically. Behind the scenes, a team of coordinated AI agents does the heavy lifting using LangGraph, LangChain, and FastAPI.

## The Problem It Solves

Booking a trip usually means bouncing between flight search engines, hotel comparison sites, and manually stitched-together itineraries. TravelHive AI consolidates that entire process into a single conversational experience by orchestrating four specialized agents:

- a **flight-search agent** that finds relevant flight options,
- a **hotel-research agent** that surfaces accommodation suggestions,
- an **itinerary-planning agent** that builds a day-by-day schedule, and
- a **response agent** that packages everything into a clean, readable plan.

All four are coordinated through a LangGraph-powered workflow.

## Key Features

- ✈️ Flight lookups via the AviationStack API
- 🏨 Hotel recommendations powered by Tavily search
- 🧠 Multi-agent coordination built on LangGraph
- 📝 Auto-generated, structured itineraries
- 🌐 FastAPI backend paired with a lightweight web UI
- 💾 Persistent conversation history stored in PostgreSQL
- ⚡ Fast, LLM-driven responses using Groq

## Built With

- Python 3.10+
- FastAPI
- Jinja2 templating with HTML/CSS/JavaScript on the frontend
- LangGraph
- LangChain
- Groq-hosted LLMs
- PostgreSQL
- Tavily API
- AviationStack API

## Folder Layout

```
.
├── app.py                # FastAPI entry point
├── backend.py            # LangGraph agent workflow logic
├── requirements.txt       # Python package dependencies
├── static/                # Frontend static assets
├── templates/             # Jinja2 HTML templates
└── tools/                 # Flight & web search tool integrations
```

## Before You Start

Make sure the following are ready on your machine:

- Python 3.10 or later
- A running, reachable PostgreSQL instance
- API credentials for:
  - Groq
  - Tavily
  - AviationStack

## Setting Up Environment Variables

In the project's root directory, create a `.env` file containing:

```
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
DEFAULT_ORIGIN_IATA=DAC
```

## Getting It Running Locally

```bash
python -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt
```

Launch the server:

```bash
python app.py
```

Then visit:

```
http://127.0.0.1:8000/
```

## How It Works, Step by Step

1. The user sends a travel request in plain language.
2. The flight agent pulls relevant flight data.
3. The hotel agent researches suitable places to stay.
4. The itinerary agent assembles a realistic day-by-day plan.
5. The final agent compiles everything into a polished, user-facing response.

![TravelHive Website Image](<Screenshot 2026-07-06 at 10.11.13 PM.png>)