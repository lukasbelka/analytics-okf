# Analytics-OKF: Improved AI Agent Queries with OKF Metadata

This project demonstrates how Google's **Open Knowledge Format (OKF)** can increase the reliability of agentic database queries by reducing SQL hallucinations. We use the **Contoso dataset** ingested into **DuckDB**. **LangChain** is used to build an AI agent that queries the data based on metadata from the OKF bundle. 

This project uses the `langchain-google-genai` package. An API key from Google is required (store `GOOGLE_API_KEY` in a `.env` file).

## Project Structure

The codebase follows a modular Python structure:

- `data/`: Local data storage (ignored in git except for raw files).
  - `raw/`: Raw CSV downloads.
  - `contoso.db`: Compiled DuckDB file.
- `okf_bundle/`: The Semantic Knowledge Graph using Markdown files.
  - `tables/`: Table definitions (`fact_sales.md`, etc.).
  - `metrics/`: Metric definitions (`net_revenue.md`, etc.).
- `src/`: Main Application Code.
  - `data_pipeline/`: Scripts to fetch CSVs and build the DuckDB tables.
  - `okf/`: Logic to parse the YAML/Markdown OKF specification.
  - `agent/`: LangChain AI logic, tools, and prompts.
  - `cli.py`: Command Line Interface logic.
- `main.py`: Clean entrypoint for the application.

## Setup Instructions

### Prerequisites
- Python 3.12+
- `uv` for dependency management
- A `.env` file in the root directory:
  ```env
  GOOGLE_API_KEY=your_key_here
  ```

### Installation
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    uv add duckdb pandas langchain langchain-community langchain-google-genai requests
    ```

## Usage

You can use the CLI to interact with the project:

```bash
# Download the raw data
python main.py download

# Build the DuckDB database
python main.py build

# Start the interactive AI Agent
python main.py chat
```