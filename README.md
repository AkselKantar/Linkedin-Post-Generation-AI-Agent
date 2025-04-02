# LinkedIn Content Generator

This project uses CrewAI agents to generate SEO-optimized LinkedIn post options for AI topics targeted at mid-market companies.

## 🚀 Features

- Multi-agent orchestration with CrewAI
- Topics generation, content writing, and SEO enhancement
- Uses OpenAI's GPT-4 via LangChain backend

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/AkselKantar/Linkedin-Post-Generation-AI-Agent.git
cd LinkedIn-Content_Generator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create and Set Up Your .env File

```bash
copy .env.example .env
```

Then add your GROQ API key to `.env`:

```
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxx
```

### 5. Run the Project

```bash
python main.py
```

---

## 🧠 Agents

- `Topic Researcher`: Suggests 3 LinkedIn post topics
- `Content Writer`: Generates 3 post styles per topic
- `SEO Enhancer`: Optimizes posts with hashtags, links, and keywords

---