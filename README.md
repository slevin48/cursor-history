# Cursor History 🕒

https://cursor-history.streamlit.app/

<img height="235.98130841121494px" src="https://media2.giphy.com/media/xoicctrOv5aGw6mCZi/giphy.gif?cid=fcde5495gvsnp8hdofdbqr2p604tew7aagk6eztd7293je85&amp;ep=v1_gifs_search&amp;rid=giphy.gif&amp;ct=g" width="404px" itemtype="http://schema.skype.com/Giphy" key="gif_0">

some advanced hacking shit:

![](img/cursor-datasette.png)

- Go to `%APPDATA%\Cursor\User`
- then in one of the folders representing you history for one project
- `datasette f87f6e0b2cf1ae8645cc0c5ffaa99529\state.vscdb`
- Enter the following SQL:

```sql
SELECT
rowid,
[key],
value
FROM
ItemTable
WHERE
[key] IN ("aiService.prompts", "workbench.panel.aichat.view.aichat.chatdata")
```


Resources:
- https://forum.cursor.com/t/chat-history-folder/7653
- https://github.com/abakermi/vscode-cursorchat-downloader
- https://github.com/thomas-pedersen/cursor-chat-browser
- https://github.com/somogyijanos/cursor-chat-export
- https://datasette.io/
