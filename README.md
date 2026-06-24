# ai-research-assistant

AI Research Assistant with Multi-Agent Workflows using Google's Agent Development Kit (ADK)

## Setup

### Prerequisites
- Python 3.9 or higher (recommended)
- Pip (Python package installer)

### Environment Configuration

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd ai-research-assistant
   ```

2. **Create and activate a virtual environment:**
   - For macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - For Windows:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. **Upgrade pip and install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory based on `.env.example`:
   ```text
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/your-service-account-key.json
   PROJECT_ID=your-gcp-project-id
   LOCATION=us-central1
   ```

## Getting Started

To run the research assistant:
```bash
python3 main.py
```
