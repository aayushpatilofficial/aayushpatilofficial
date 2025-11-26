# Aayush Patil Portfolio Website

## Overview

This is a personal portfolio website for Aayush Patil, a 14-year-old AI Engineer & Digital Innovator. The site serves as a showcase for 18+ projects spanning AI/ML, web development, and social impact applications. It features an interactive AI chatbot assistant powered by OpenAI that answers visitor questions about Aayush's work, skills, and contact information.

The application is built as a simple Flask web server serving a single-page HTML portfolio with an integrated AI chat interface.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
**Decision: Single-page HTML application with vanilla JavaScript**
- **Rationale**: Simplicity and fast loading times for a portfolio site
- **Implementation**: All frontend code in `index.html` with minimal external dependencies
- **Styling**: Inline CSS with modern, clean design principles (Apple-inspired minimal aesthetic)
- **Interactivity**: Vanilla JavaScript for smooth scrolling, animations, and AI chat interface

### Backend Architecture
**Decision: Flask microframework with minimal routing**
- **Rationale**: Lightweight Python server suitable for serving static content and handling API requests
- **Structure**: Single `app.py` file containing all backend logic
- **Endpoints**:
  - `GET /` - Serves the main portfolio page
  - Chat endpoint (implied for AI assistant interaction)
- **Static file serving**: Flask configured to serve static assets from current directory

### AI Integration
**Decision: OpenAI API integration for conversational AI assistant**
- **Rationale**: Provides visitors with an interactive way to learn about Aayush's work
- **Implementation**: 
  - Lazy initialization of OpenAI client (singleton pattern)
  - API key stored in environment variables for security
  - Custom system prompt encoding Aayush's profile, 18 projects, skills, and contact information
- **Functionality**: Acts as a virtual representative answering questions about projects, skills, hiring/collaboration opportunities

### Content Management
**Decision: Static content embedded in system prompt**
- **Rationale**: No database needed for this simple portfolio; content rarely changes
- **Content includes**:
  - Personal information (age, role, contact details)
  - Detailed descriptions of 18 projects
  - Skills listing (Python, TensorFlow, PyTorch, React, Node.js, etc.)
  - Communication guidelines for the AI

### Security Considerations
- API keys stored as environment variables (`OPENAI_API_KEY`)
- No user authentication system (public portfolio site)
- No sensitive data storage

## External Dependencies

### Third-Party APIs
- **OpenAI API**: Powers the AI chatbot assistant
  - Used for: Natural language conversation about Aayush's portfolio
  - Authentication: API key via environment variable

### Python Packages
- **Flask**: Web framework for serving the application
- **openai**: Official OpenAI Python client library

### Frontend Libraries
- None explicitly listed (appears to use vanilla JavaScript)

### Hosting/Infrastructure
- Designed for Replit deployment (evidenced by `main.py` and `repl-nix-workspace` references)
- No database system required
- Static file serving from application root directory

### Environment Configuration
- `OPENAI_API_KEY`: Required environment variable for AI functionality
- No other external configuration dependencies identified