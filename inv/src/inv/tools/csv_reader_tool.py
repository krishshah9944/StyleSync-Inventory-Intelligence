from crewai.tools import BaseTool
from pydantic import Field
import pandas as pd

class CsvReaderTool(BaseTool):
    name: str = "csv_reader"
    description: str = "Reads a CSV file and returns data"
    csv_path: str = Field(..., description="Path to the inventory CSV file")

    def _run(self):
        try:
            df = pd.read_csv(self.csv_path)
            return df.to_dict(orient='records')  # Return as list of dictionaries
        except Exception as e:
            return {"error": str(e)}
