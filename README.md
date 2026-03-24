# 🧠 Gemini AI Explainer

A modern, fast, and interactive web application that leverages Google's **Gemini 2.0 Flash** to briefly explain any topic you enter.

## ✨ Features

-   **Instant Explanations**: Type any topic and get a concise summary in seconds.
-   **Modular FastAPI Structure**: Separated into routers, claims, and models.
-   **Immersive Design**: Dark mode aesthetic with glassmorphism and smooth animations.
-   **Status Bar tracking**: Monitor model status and call latency dynamically.

## 🚀 Getting Started

### Prerequisites

-   Python 3.10+
-   [UV](https://github.com/astral-sh/uv) (Recommended package manager) or standard `pip`

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/ai-explainer-app.git
    cd ai-explainer-app
    ```

2.  **Install Dependencies**
    Using `uv`:
    ```bash
    uv sync
    ```
    Alternatively, using Standard `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup**
    Create a `.env` file and add your Google Gemini API Key:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

### 🏃 Running the App

Start the backend server using `uv`:

```bash
uv run python server.py
```

The app serves at `http://127.0.0.1:8000`.

## 📂 Project Structure

```text
├── .env.example        # Environment secret template
├── pyproject.toml      # Dependency Config (UV)
├── requirements.txt    # Standard requirements file
├── server.py           # Main Entry (Mounts everything)
├── chains/
│   └── explainer.py    # AI Model logic
├── models/
│   └── request.py      # Request Validation Data
├── routers/
│   └── explain.py      # Endpoint routing
└── static/             # Frontend assets (HTML, CSS, JS)
```
