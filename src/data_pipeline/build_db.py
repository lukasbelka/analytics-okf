import duckdb
from pathlib import Path

def build_database():
    """
    Reads the CSV files from data/raw/ and builds a persistent
    DuckDB database at data/contoso.db.
    """
    print("Starting database build process...")
    
    db_path = Path("data/contoso.db")
    raw_dir = Path("data/raw")
    
    if not raw_dir.exists():
        print(f"Error: {raw_dir} does not exist. Please ensure CSV files are present.")
        return

    # Connect to the persistent database file
    conn = duckdb.connect(str(db_path))
    
    # Mapping of target table names to source CSV files
    # This applies standard Kimball dimensional modeling naming conventions
    tables_to_create = {
        "FactSales": "sales.csv",
        "DimProduct": "product.csv",
        "DimCustomer": "customer.csv",
        "DimStore": "store.csv",
        "DimDate": "date.csv",
        "FactOrders": "orders.csv",
        "FactOrderRows": "orderrows.csv",
        "FactCurrencyExchange": "currencyexchange.csv"
    }
    
    for table_name, csv_filename in tables_to_create.items():
        csv_path = raw_dir / csv_filename
        
        if csv_path.exists():
            print(f"  Creating table {table_name} from {csv_filename}...")
            # Using DuckDB's native read_csv_auto to create tables
            query = f"""
                CREATE OR REPLACE TABLE {table_name} AS 
                SELECT * FROM '{csv_path}';
            """
            conn.sql(query)
        else:
            print(f"  Warning: {csv_filename} not found, skipping {table_name}.")
            
    print(f"\n✅ Database successfully built at {db_path.absolute()}")
    
    # Print the resulting tables
    print("\nAvailable Tables:")
    print(conn.sql("SHOW TABLES;"))
    
    conn.close()

if __name__ == "__main__":
    build_database()
