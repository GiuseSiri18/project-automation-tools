# 🚀 Project Automation Toolkit + Jira Integration

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jira](https://img.shields.io/badge/Jira-Cloud-0052CC)
![License](https://img.shields.io/badge/License-MIT-green)

> **"Standardization is the first step to scaling engineering teams."**

### 📖 About The Project

This toolkit automates the initialization of new software projects. It bridges the gap between **Local Development** and **Project Management** by:
1.  Scaffolding a standard directory structure locally.
2.  **Automatically creating a tracking ticket in Jira** to signal the team that a new service has started.

---

### ✨ Key Features

* **⚡ Instant Scaffolding:** Generates a full project structure (`src`, `tests`, `docs`) in a dedicated output folder.
* **🔗 Jira Integration:** Connects to Jira Cloud API to create a "Setup Task" automatically.
* **🔒 Secure:** Uses environment variables to handle credentials safely.
* **🛡️ Clean Workspace:** All generated projects are isolated in a `generated_projects/` directory.

---

### ⚙️ Configuration (Required)

To enable Jira integration, you must configure your credentials.

1.  Create a file named `.env` in the root directory.
2.  Add your Jira Cloud credentials (do not commit this file!):

```env
JIRA_URL="[https://your-domain.atlassian.net](https://your-domain.atlassian.net)"
JIRA_EMAIL="your-email@example.com"
JIRA_TOKEN="your-api-token"
JIRA_PROJECT_KEY="PROJ"