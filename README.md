# LinkedIn Content Generator

This project uses CrewAI agents to generate SEO-optimized LinkedIn post options for AI topics targeted at mid-market companies.

## 🚀 Features

- Multi-agent orchestration with CrewAI
- Topics generation, content writing, and SEO enhancement
- Uses OpenAI's GPT-4 via LangChain backend

## 🛠️ Setup Instructions

### 1. Clone the Repo

git clone https://github.com/your-username/LinkedIn-Content_Generator.git
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

Then add your OpenAI key to `.env`:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
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

## 📄 License

MIT

---

## 🧪 Try it on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/drive/1Zqgp99DQV_b_UXlZU5R9Y0pMC8jxc7al?usp=sharing)
