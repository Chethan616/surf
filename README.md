# Chethan616 

A real-time AI-powered search application built with Flutter and FastAPI, inspired by Perplexity AI.

## Overview

This project combines modern web search capabilities with AI-powered responses to provide a Perplexity-like experience. The application features a clean, responsive UI built with Flutter and a robust backend powered by FastAPI.

## Features

- **Real-time Search Responses**: Get instant search results and AI-generated answers
- **WebSocket Communication**: Stream responses in real-time for a seamless experience
- **Modern UI**: Clean, responsive interface with dark mode
- **Source Attribution**: Responses include citations to original sources
- **Relevance Ranking**: Uses semantic similarity to rank search results by relevance

## Tech Stack

### Frontend
- Flutter (Web/Desktop/Mobile)
- WebSocket for real-time communication
- Markdown rendering for formatted responses

### Backend
- FastAPI (Python)
- Google Gemini AI API for response generation
- Tavily API for web search capabilities
- Sentence Transformers for semantic similarity ranking

## Setup Instructions

### Backend Setup

1. Navigate to the server directory:
   ```
   cd server
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the server directory with the following variables:
   ```
   TAVILY_API_KEY=your_tavily_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. Run the server:
   ```
   # Windows (PowerShell)
   python -m uvicorn main:app --reload
   
   # Linux/Mac
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Install Flutter (if not already installed):
   https://flutter.dev/docs/get-started/install

2. Install dependencies:
   ```
   flutter pub get
   ```

3. Run the application:
   ```
   flutter run -d chrome  # For web
   # OR
   flutter run  # For default device
   ```

## API Endpoints

- **WebSocket**: `/ws/chat` - Main WebSocket endpoint for real-time chat
- **WebSocket Test**: `/ws/test` - Simple test endpoint for verifying WebSocket connectivity
- **REST API**: `/chat` - POST endpoint for non-WebSocket chat interactions

## Known Issues and Limitations

- The UI may display overflow errors in some components
- WebSocket connections may have transient connectivity issues
- The Gemini model may occasionally be overloaded and return a 503 error

## License

This project is open source and available under the MIT License.

## Owner

**Chethan616** 