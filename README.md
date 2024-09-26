# WWII Missions

This project is designed to simulate or analyze World War II missions, 
providing data models and functionalities around various historical 
elements like cities, countries, and targets.

## Features

- **Target Management**: Manage and simulate mission targets (cities, countries, etc.).
  
- **Database Interaction**: Use SQL scripts for creating and managing data tables.
  
- **Data Models**: Python classes to represent the essential elements (City, Country, Target).

---

## Setup Instructions

### 1. Clone the repository:

```bash
git clone <https://github.com/shai-r/wwii_missions>
```

### 2. Install dependencies:

This project assumes you have Python 3 installed. 
Use the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the application:

```bash
python app.py
```

# Database Setup Instructions

## SQL Scripts Location
The SQL scripts for creating tables and inserting data are located in the `native_sql/` directory.

## Steps to Set Up the Database

1. **Run the Schema Creation Script**
   - Execute the following SQL script to set up the initial database schema:
     ```sql
     -- Run this script to create the necessary tables
     source native_sql/create_tables.sql;
     ```

2. **Populate the Tables with Initial Data**
   - Use the following SQL script to insert initial data into the tables:
     ```sql
     -- Run this script to populate the tables with data
     source native_sql/insertion.sql;
     ```
