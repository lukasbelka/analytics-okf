import argparse

def main():
    parser = argparse.ArgumentParser(description="Analytics OKF CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: download
    parser_download = subparsers.add_parser("download", help="Download the Contoso dataset CSVs")
    
    # Command: build_db
    parser_build = subparsers.add_parser("build_db", help="Build the DuckDB database from CSVs")
    
    # Command: chat
    parser_chat = subparsers.add_parser("chat", help="Start the OKF-Aware AI Agent")

    args = parser.parse_args()

    if args.command == "download":
        print("Starting data ingestion...")
        from src.data_pipeline.download import download_data
        download_data()
    elif args.command == "build_db":
        print("Building database...")
        from src.data_pipeline.build_db import build_database
        build_database()
    elif args.command == "chat":
        print("Starting Agent... (Not implemented yet)")
        # from src.agent.core import start_chat
        # start_chat()
    else:
        parser.print_help()

    return 0
