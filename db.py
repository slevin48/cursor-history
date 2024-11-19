#%%

import sqlite3
import os
import pandas as pd
sqlite_db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.vscdb")
# sqlite_db_path = "C:\\Users\\ydebray\\AppData\\Roaming\\Cursor\\User\\workspaceStorage\\6ae6eb0531606929850a78b0a04649f1\\state.vscdb"
conn = sqlite3.connect(f'file:{sqlite_db_path}?mode=ro', uri=True)
#%%
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)
#%%
cursor = conn.execute("PRAGMA table_info('ItemTable');")
schema = cursor.fetchall()
print(schema)

#%% discover tables
cursor = conn.execute("SELECT value FROM ItemTable")
tables = cursor.fetchall()
tables
#%% get prompts
cursor = conn.execute("""
    SELECT
    rowid,
    [key],
    value
    FROM
    ItemTable
    WHERE
    [key] IN ("aiService.prompts", "workbench.panel.aichat.view.aichat.chatdata")
""")
df = pd.DataFrame(cursor.fetchall(), columns=["rowid", "key", "value"])
df
#%% export to json
df.to_json("prompts.json", orient="records")


# %%
