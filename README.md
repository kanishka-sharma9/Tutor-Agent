# Tutor-Agent

Tutor-Agent is a modular AI tutoring system built using the Google Agent Development Kit (ADK). This repository provides an interactive web-based assistant capable of tutoring users in Math, History, and Computer Science.

## Features

- **Multi-Subject Tutoring:** Specialized agents for Math, History, and Computer Science.
- **Web Interface:** Simple interactive experience powered by ADK's web server.
- **100% Python:** Easy to read, modify, and contribute to.

## Getting Started

### Prerequisites

- Python 3.8+
- [Google ADK (Agent Development Kit)](https://github.com/google/adk)
- pip (Python package manager) / uv (by Astral)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kanishka-sharma9/Tutor-Agent.git
   cd Tutor-agent
   ```

2. **Install Dependencies**
   ```bash
   uv add -U google-adk langchain
   ```
3. **Set environment variables**
   ```bash
   setx GOOGLE_API_KEY <your-api-key>
   setx GOOGLE_GENAI_USE_VERTEXAI False
   ```
4. **Run the Tutor Agent**
   ```bash
   adk web
   ```
   OR
   ```
   streamlit run app.py
   ```

Open your browser and navigate to the provided URL to interact with the Tutor Agent.

## Usage

After starting the web server, ask questions in Math, History, or Computer Science, and the corresponding agent will guide you.

## Live Link

![Dancing Banana](https://media.tenor.com/uzbB1bjOc8gAAAAC/im-working-on-it-keanu-reeves.gif)

## Interraction

1. The **tutor** agent has three sub_agents as tools: history_teaching_agent, math_teaching_agent, computer_science_teaching_agent
2. Based on the tasks the tutor invokes the appropriate agent and returns the corresponding output in a formatted way.
3. Each agent has access to certain tools that they can use (google_search, python_tool etc.)

## Challenges faced

Deployment


# HELP NEEDED

# If you are a devloper and know how to deploy these agents for free, Let me know.

## Acknowledgments

- [Google ADK](https://github.com/google/adk) for the agent development framework.
