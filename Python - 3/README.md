HGA – Hidden/Covert Agent: Multi-Threaded Intelligence Extraction System

A Python-based simulation of a multi-agent spy intelligence gathering system. Multiple concurrent "agents" (threads) scan classified log files, extract structured intelligence using regex, and compile everything into a serialized, zipped "mission report."

📖 Overview

This project simulates a covert operations pipeline where independent agents work in parallel to process secret log files, extract key intelligence (emails, dates, codes, keywords), and securely package their findings for delivery — all while demonstrating safe multi-threaded file handling in Python.

✨ Features

- **Concurrent Processing** – Spawns a dedicated thread ("agent") per log file for parallel analysis
- **Thread Synchronization** – Uses `Lock` and `Semaphore` to safely manage shared resources and limit concurrent access
- **Regex-Based Extraction** – Pulls structured data out of raw log text:
  - Email addresses
  - Dates
  - Secret codes
  - Priority keywords (`URGENT`, `CONFIDENTIAL`, `TOP-SECRET`, etc.)
- **Serialization** – Stores the compiled intelligence vault using `pickle`
- **Archiving** – Packages the final report into a `.zip` mission report using `zipfile`

 🛠️ Tech Stack

- Python 3.13
- `threading` (Thread, Lock, Semaphore)
- `re` (Regular Expressions)
- `pickle`
- `zipfile`
- `os`
- 
 📂 Project Structure

```
HGA/
├── secret_files/           # Raw input log files to be analyzed
│   ├── log1.txt
│   ├── log2.txt
│   ├── intel.pkl           # Serialized intelligence vault
│   └── mission_report.zip  # Final zipped report
├── extracted_reports/      # Per-agent extracted report output
│   ├── report_log1.txt
│   ├── report_log2.txt
│   └── report_intel.pkl
└── spylog.py                # Main script
```

## ⚙️ How It Works

1. **Initialization** – Global shared resources are set up: an intelligence vault (list), a `Lock` for synchronized writes, and a `Semaphore` to cap concurrent agents.
2. **Agent Dispatch** – For every file in `secret_files/`, a new thread is spawned and assigned an agent name (`agent-1`, `agent-2`, ...).
3. **Analysis** – Each agent reads its assigned file, applies regex patterns to extract emails, dates, codes, and keywords, and previews the file's content.
4. **Reporting** – Extracted data is written to individual report files and appended to the shared intelligence vault (thread-safe via `Lock`).
5. **Serialization & Packaging** – Once all agents finish, the intelligence vault is pickled, and the reports are compressed into a final `mission_report.zip`.

▶️ Running the Project

```bash
python spylog.py
```

Sample output:
```
HGA Mission Started
[agent-1] Started analyzing log1.txt
[agent-2] Started analyzing log2.txt
[agent-2] Finished log2.txt
[agent-1] Finished log1.txt

Saving intelligence using pickle
Zipping the mission report

Mission Complete Successfully

🎓 Learning Outcomes

Built as part of the **Python Programming: Zero to Hero** course on the **GUVI (HCL)** platform, this project reinforced:
- Safe multi-threaded programming with locks and semaphores
- Designing and applying regex patterns for real-world text extraction
- File I/O, serialization, and archiving workflows in Python
- Structuring a small end-to-end data processing pipeline

📜 License

This project is for educational purposes as part of a course assignment.

*Built with 🐍 Python as part of the HCL-GUVI Python Programming Bootcamp.*
