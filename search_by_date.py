import json 
import os

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
def SearchByDate(name):
    console=Console()
    load_dotenv()
    diaries_path=os.getenv("DIARIES_PATH")
    with open(f"{diaries_path}/{name}.json", "r", encoding="utf-8") as file:
                journal = json.load(file)
    demande_dat=Text("Please provide a date in this format: year-month-day (YYYY-MM-DD) : ",style="bold yellow")
    dat = console.input(demande_dat)
    found=False
    for diary in journal:
                    if diary["Date"].startswith(dat):
                        console.print(Align(f"Title: {diary['Title']}",align="center",style="italic green"))
                        console.print(Align(f"Date: {diary['Date']}",align="center"))
                        console.print(Align(f"Text: {diary['Text']}",align="center"))
                        found=True
    if not found :
            console.print(Align("NO DIARIES  IN THIS DATE",align="center",style="bold red"))
    