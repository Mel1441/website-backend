import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# 🔐 Load environment variables
env_file = ".env.dev"
load_dotenv(dotenv_path=env_file)


user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")

# 🛠️ Connect to the database
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{dbname}?sslmode=require")


# 📁 Migration folder
MIGRATIONS_DIR = "migrations"

with engine.connect() as conn:

    with conn.begin():
    #  Ensure migration_log table exists
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS migration_log (
                id SERIAL PRIMARY KEY,
                filename TEXT UNIQUE,
                schema TEXT,
                applied_at TIMESTAMP DEFAULT now()
            );
        """))


    #  Get already applied migrations
        result = conn.execute(text("SELECT filename FROM migration_log"))
        applied = {row[0] for row in result}
        
        #  Apply new migrations
        for filename in sorted(os.listdir(MIGRATIONS_DIR)):
            path = os.path.join(MIGRATIONS_DIR, filename)
            if filename.endswith(".sql") and filename not in applied:
                print(f"🔧 Applying migration: {filename}")
                sql = open(path).read()
                print(sql)
    
            # ensures rollback on failure
                conn.execute(text(sql))
                conn.execute(
                    text("INSERT INTO migration_log (filename) VALUES (:f)"),
                    {"f": filename}
                )
     