# Contributing to The Hub

First off, thank you for considering contributing to The Hub! It's people like you that make the open-source AI community such a fantastic place to learn, inspire, and create.

## 🚀 How to Contribute

### 1. Reporting Bugs
- Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/TadiwanasheZvidzaRodney/the_agent_app_store/issues).
- If you're unable to find an open issue addressing the problem, open a new one. Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.

### 2. Suggesting Enhancements
- Open a new [Issue](https://github.com/TadiwanasheZvidzaRodney/the_agent_app_store/issues) and select the Feature Request template. 
- Provide a clear, detailed explanation of the feature.

### 3. Submitting Pull Requests
1. Fork the repository and create your branch from `main`.
2. Ensure you have installed the required dependencies for both `backend/` and `frontend/`.
3. If you've added code that should be tested, add tests.
4. If you've changed APIs, update the documentation.
5. Ensure your code follows our strict architectural guidelines located in `AGENTS.md`. **Separation of Concerns is critical.**
6. Submit your Pull Request!

## 🛠 Development Setup

To run the project locally for development:

1. Clone your fork.
2. Start the FastAPI backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
3. Start the React frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

Thank you for contributing! 🤖✨
