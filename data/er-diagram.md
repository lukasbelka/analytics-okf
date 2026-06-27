# Contoso Entity-Relationship Diagram

This diagram maps out the Galaxy Schema of the Contoso dataset, demonstrating how the fact tables (events) are linked to the dimension tables (entities) through foreign keys.

```mermaid
erDiagram
    %% Dimensions (The "Who, What, Where, When")
    DimProduct {
        int ProductKey PK
        string ProductName
        float UnitPrice
    }
    DimStore {
        int StoreKey PK
        string StoreName
        string Region
    }
    DimCustomer {
        int CustomerKey PK
        string CustomerName
    }
    DimDate {
        int DateKey PK
        date FullDate
    }

    %% Fact Tables (The "Events")
    FactSales {
        int SalesKey PK
        int DateKey FK
        int StoreKey FK
        int ProductKey FK
        int CustomerKey FK
        float SalesAmount
    }
    FactOrders {
        int OrderKey PK
        int DateKey FK
        int CustomerKey FK
        int StoreKey FK
    }
    FactOrderRows {
        int OrderRowKey PK
        int OrderKey FK
        int ProductKey FK
        int Quantity
    }
    FactCurrencyExchange {
        int ExchangeKey PK
        int DateKey FK
        string CurrencyName
        float ExchangeRate
    }

    %% Relationships
    DimProduct ||--o{ FactSales : "is sold in"
    DimStore ||--o{ FactSales : "makes"
    DimCustomer ||--o{ FactSales : "purchases"
    DimDate ||--o{ FactSales : "occurs on"

    DimCustomer ||--o{ FactOrders : "places"
    DimDate ||--o{ FactOrders : "placed on"
    DimStore ||--o{ FactOrders : "fulfilled by"

    FactOrders ||--|{ FactOrderRows : "contains"
    DimProduct ||--o{ FactOrderRows : "includes"

    DimDate ||--o{ FactCurrencyExchange : "rate on"
```
