# Linux-Based ETL Pipeline

A self-hosted Linux ETL pipeline that ingests data from a public API, processes it using Python, and stores structured outputs on disk. The pipeline is automated using cron and managed with standard Linux tooling.

## Features
- Python ETL pipeline
- Public REST API ingestion
- Raw and processed data separation
- Cron-based scheduling
- Linux log inspection (grep, sed)
- Process locking to prevent overlapping runs
- Data archiving with tar & gzip

## Tech Stack
- Linux (Ubuntu / WSL)
- Python 3
- Bash
- Cron
- Docker (optional extension)

## Status
🚧 In progress
