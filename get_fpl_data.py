# This script fetches player data from the Fantasy Premier League (FPL) API and processes it into a DataFrame.
# It uses the fpl package, which is an async wrapper for the FPL API.
# Install the fpl package if not already installed:


# source .venv/bin/activate
# pip install asyncio
# pip install nest_asyncio
# pip install pandas
# pip install fpl



import asyncio
import nest_asyncio  # Allows nested event loops in Jupyter notebooks   
import pandas as pd
from fpl import FPL  # Async wrapper for FPL API [11]
import aiohttp

async def fetch_player_data():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()
        return pd.DataFrame([p.__dict__ for p in players])

# Clean data: filter active players, handle missing values
if __name__ == "__main__":
    nest_asyncio.apply()  # Only needed if running in Jupyter, safe otherwise
    df = asyncio.run(fetch_player_data())
    df = df[df['minutes'] > 90]  # Exclude low-minute players
    df.fillna(0, inplace=True)
    df.infer_objects(copy=False)
