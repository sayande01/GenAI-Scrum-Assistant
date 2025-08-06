# AI Scrum Master Agent: Intelligent Agile Facilitation 🚀

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.42.2-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.19-green.svg)](https://www.langchain.com/)
[![Google Gemini 2.0 Flash](https://img.shields.io/badge/Google%20Gemini-2.0%20Flash-orange.svg)](https://ai.google.dev/models/gemini)

## 🌟 Overview: Empowering Agile Teams with AI

Welcome to the **AI Scrum Master Agent** – a cutting-edge web application designed to enhance agile processes by providing intelligent assistance to Scrum Masters and development teams. This project leverages **Generative AI (GenAI)**, specifically **Google Gemini 2.0 Flash**, orchestrated through **LangChain**, to automate and optimize various Scrum activities.

From generating personalized daily standup questions to analyzing sprint health, providing retrospective insights, and suggesting impediment resolutions, this agent aims to foster **continuous improvement**, **boost team productivity**, and ensure **sprint success**. It's a powerful demonstration of how AI can streamline project management and facilitate a more effective agile environment.

---

## ✨ Core Capabilities: What It Does

This AI Scrum Master Agent offers a suite of features to support your agile workflow:

* **AI Sprint Health Analysis**: 🔍 Provides a comprehensive assessment of the current sprint's health (Red/Yellow/Green), along with key concerns, recommendations, and motivational suggestions.
* **Daily Standup Assistant**: 📝 Generates personalized, thoughtful questions for each team member based on their previous work context, facilitating focused and productive standups.
* **Retrospective Insights**: 🧠 Analyzes team feedback to identify key themes, top improvement opportunities, actionable items, and team strengths, fostering a culture of learning.
* **Impediment Management & Resolution**: ⚠️ Offers root cause analysis and specific resolution strategies for identified impediments, helping teams overcome blockers faster.
* **AI Scrum Master Recommendations**: 🤖 Provides strategic recommendations for daily standups, discussions with the product owner, sprint planning, and potential sprint risks based on comprehensive team and backlog data.
* **Interactive Analytics & Reports**: 📊 Visualizes sprint progress with burndown charts, team velocity trends, workload distribution, and generates summary reports.
* **Team & Backlog Tracker**: 📋 Keeps track of daily team updates, current implementations, and the product backlog in an organized manner.
* **User-Friendly Interface**: ✨ Built with **Streamlit** for an intuitive, interactive, and visually appealing user experience.

---

## ⚙️ Under the Hood: Architecture & Technologies

This robust application is powered by a modern and integrated tech stack:

* **Frontend**: **Streamlit** with custom CSS for a dynamic, responsive, and aesthetically pleasing user interface.
* **NLP Engine**: **Google Generative AI** (`gemini-2.0-flash-exp`) serves as the core intelligence, driving natural language understanding and generation for all AI-powered insights.
* **Framework**: **LangChain** orchestrates the interactions between the language model and various data inputs, enabling complex prompt engineering and structured responses.
* **Data Handling**: **Pandas** is utilized for efficient management and display of structured data such as team updates, implementations, and product backlog.
* **Visualizations**: **Plotly** is employed to create interactive and informative charts, including burndown, velocity, and workload distribution graphs.
* **Date & Time Management**: Python's `datetime` module for handling sprint dates and durations.

---

## 🚀 Getting Started: Set Up & Run

Follow these steps to get the AI Scrum Master Agent up and running on your local machine.

### Prerequisites

* Python 3.9+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/AI-Scrum-Master-Agent.git](https://github.com/your-username/AI-Scrum-Master-Agent.git)
    cd AI-Scrum-Master-Agent
    ```

2.  **Create a virtual environment (recommended for dependency isolation):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file in your project root with the following content:
    ```
    streamlit
    google-generativeai
    pandas
    plotly
    langchain
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Set your Google API Key:**
    The application requires a Google API Key to access the Gemini 2.0 Flash model. Obtain yours from the [Google AI Studio](https://ai.google.dev/).

    Set it as an environment variable (replace `"YOUR_API_KEY_HERE"` with your actual key):
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
    (On Windows Command Prompt: `set GEMINI_API_KEY="YOUR_API_KEY_HERE"` | On PowerShell: `$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"`)

    *The app will display an error in the sidebar if the API key is not found.*

### Running the Application

1.  **Launch the Streamlit app:**
    ```bash
    streamlit run scrum_agent_v1.py
    ```

    The application will automatically open in your default web browser at `http://localhost:8501`.

---

## 💡 How to Use: Your Agile Companion

Navigate through the different tabs and sections of the application to utilize its features:

* **AI Sprint Analysis**: Click "Analyze Current Sprint" to get an AI-powered health check of your ongoing sprint.
* **Daily Standup**: Select a team member and their previous work context to generate personalized standup questions. Add daily updates to track progress.
* **Retrospective**: Input team feedback and click "Generate AI Insights" to get actionable insights for continuous improvement.
* **Impediments**: View current impediments, add new ones, and get AI-generated resolution suggestions.
* **Reports**: Explore various sprint analytics charts and generate a summary report.
* **Tracker**: Review detailed dataframes for team updates, current implementations, and the product backlog.
* **AI Scrum Master Recommendations**: Get strategic advice based on the current state of your sprint and backlog.

---

## 🤝 Contributing: Join the Evolution!

We welcome contributions to make this AI Scrum Master Agent even more powerful! If you have ideas for improvements, bug fixes, or exciting new features, please feel free to:

* Open an [Issue](https://github.com/your-username/AI-Scrum-Master-Agent/issues) to report bugs or suggest enhancements.
* Submit a [Pull Request](https://github.com/your-username/AI-Scrum-Master-Agent/pulls) with your code changes.

Let's build the future of agile project management together!

---

## 📄 License

This project is released under a **Proprietary License**. Please review the license file for details.

---

## 📧 Contact

For any questions, support, or feature requests, please open an issue in this repository. We're here to help!
