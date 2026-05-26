# AI PPT Generator using MCP + Streamlit

## 🚀 Overview

AI PPT Generator is a modern presentation generation system built using:

* MCP (Model Context Protocol)
* Streamlit
* LangChain
* HuggingFace LLMs
* Python-PPTX

The system automatically creates professional PowerPoint presentations from a simple topic input.

It generates:

* Structured slide flow
* Professional slide layouts
* Timeline slides
* Cards slides
* Content slides
* Modern Gamma-style presentation design

---

# ✨ Features

## ✅ AI-Powered Presentation Generation

Generate complete presentations using AI from a single topic.

---

## ✅ Modern Gamma-Style Design

Inspired by modern presentation tools like:

* Gamma
* Canva
* Pitch

Includes:

* Minimal layouts
* Large typography
* Clean spacing
* Full-slide utilization

---

## ✅ Multiple Slide Types

### 📄 Content Slides

Professional text-based slides with structured information.

### 🧩 Cards Slides

Modern card-based layouts for:

* Features
* Benefits
* Applications
* Technologies

### ⏳ Timeline Slides

Timeline/workflow visualization for:

* Processes
* Pipelines
* Architectures
* Steps

## ⚙️ How It Works

```text
User Input
   ↓
AI Content Generation
   ↓
Slide Planning
   ↓
MCP Slide Rendering
   ↓
PowerPoint Export
```

### 🎯 Title Slide

Modern hero slide with premium layout.

---

## ✅ Smart AI Content Planning

The AI automatically:

* Starts with introduction
* Builds logical flow
* Generates related content
* Ends with conclusion

---

## ✅ Adjustable Slide Count

Users can generate:

* 5 slides
* 10 slides
* 20 slides
  etc.

The system automatically adjusts:

* Structure
* Conclusion placement
* Content distribution

---

## ✅ Streamlit Frontend

Modern frontend with:

* Topic input
* Slide count selection
* Presentation style selection
* Real-time generation flow
* PPT download button

---

# 🏗️ Project Structure

```bash
my_ppt_project/
│
├── app.py
├── my_ppt_agent.py
├── ppt_mcp_server.py
├── requirements.txt
├── .env
├── README.md
```

---

# 📁 File Explanation

## `app.py`

Frontend application built using Streamlit.

Responsibilities:

* User input
* UI rendering
* Progress flow
* PPT download

---

## `my_ppt_agent.py`

AI presentation planning engine.

Responsibilities:

* Topic extraction
* AI content generation
* Slide structure planning
* Slide type detection
* MCP tool execution

---

## `ppt_mcp_server.py`

MCP PowerPoint rendering server.

Responsibilities:

* Create PPT
* Design slides
* Add content
* Generate layouts
* Export PowerPoint

---

# ⚙️ Technologies Used

## Frontend

* Streamlit

## Backend

* Python

## AI/LLM

* HuggingFace
* Qwen2.5-7B-Instruct

## Presentation Engine

* python-pptx

## MCP

* Model Context Protocol

---

# 🧠 How It Works

## Step 1 — User Enters Topic

Example:

```text
AI in Healthcare
```

---

## Step 2 — AI Generates Structure

The LLM creates:

* Introduction
* Concepts
* Workflow
* Applications
* Benefits
* Challenges
* Future Trends
* Conclusion

---

## Step 3 — Slide Type Detection

The system automatically selects:

* Content slide
* Cards slide
* Timeline slide

based on heading/context.

---

## Step 4 — MCP Creates Slides

The MCP server:

* Designs layouts
* Adds typography
* Applies styling
* Creates PowerPoint

---

## Step 5 — PPT Export

Final presentation exported as:

```text
final_output.pptx
```

---

# ▶️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your_repo_url>
cd my_ppt_project
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 📦 Required Packages

Example packages:

```txt
streamlit
python-pptx
python-dotenv
langchain
langchain-huggingface
langchain-core
langchain-mcp-adapters
mcp
requests
```

---

# ▶️ Run Project

## Start Streamlit App

```bash
streamlit run app.py
```

---

# 🖥️ Frontend Workflow

1. Enter presentation topic
2. Select slide count
3. Select presentation style
4. Click Generate
5. AI generates PPT
6. Download PowerPoint

---

# 🎨 Presentation Styles

Supported styles:

* Professional
* Modern Startup
* Minimal Clean
* Investor Pitch

---

# 📊 Example Topics

* AI in Healthcare
* Blockchain Technology
* Smart Agriculture
* Cloud Computing
* Cybersecurity
* Data Science
* Machine Learning
* IoT Systems

---

# 🚀 Future Improvements

Planned upgrades:

* Charts and graphs
* AI-generated icons
* Animated slides
* PDF export
* Theme system
* Multi-language support
* Real-time collaborative editing

---

# ✅ Current Status

## Working Features

* AI slide generation
* Structured storytelling
* Multiple layouts
* Timeline generation
* Cards layouts
* PPT export
* Streamlit frontend
* MCP integration

---


