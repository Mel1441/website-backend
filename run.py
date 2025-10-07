import argparse
import os
from dotenv import load_dotenv
import uvicorn

def main():
    # 🧠 CLI Argument Parser
    parser = argparse.ArgumentParser(description="Run FastAPI app with environment config")
    parser.add_argument("--env", choices=["dev", "prod"], default="dev", help="Environment to run in")
    args = parser.parse_args()

    # 🧪 Load the correct .env file
    if args == 'dev':

    env_file = f".env.{args.env}"
    load_dotenv(dotenv_path=env_file)

    # 🧭 Set ENV variable for downstream use
    os.environ["ENV"] = args.env

    # 🚀 Launch FastAPI app
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=(args.env == "dev"))

if __name__ == "__main__":
    main()