# Analytics-OKF: Improved ai agent queries with okf metadata

This project shows how Google's **Open Knowledge Format (OKF)** can increase reliability of agentic database queries by reducing SQL hallucination of AI agents. As data the known contoso dataset is used and ingested with **DuckDB**. Further **LangChain** is used to build an AI agent that queries the data based on information taken form the OKF. To keep cost as low as possible Google's flash-2.5-lite model is used, which is why an API key from Google is required for the agent to work (store `GOOGLE_API_KEY` in `.env` file).

## Project Status

-   **Data Layer**: The "csv-100k.7z" version of the contoso dataset has been downloaded from [sql-bi](https://github.com/sql-bi/Contoso-Data-Generator-V2-data/releases/tag/ready-to-use-data) and ingested into `data/contoso.db`.
-   **OKF Layer**: OPEN. The schema and metric definitions are documented in `okf_bundle/`.
-   **Agent Layer**: OPEN. The `main.py` script initializes an agent that can answer business questions using the OKF metadata.

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
# Build the DuckDB database
python main.py build

# Start the interactive AI Agent
python main.py chat
```