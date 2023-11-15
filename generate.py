import os
from urllib.parse import urlparse

# CSV content
csv_data = """
https://realigned.app/,https://realigned.substack.com/
https://realigned.app/blog/making-of-sunrise-forest-video,https://realigned.substack.com/p/making-of-sunrise-forest-video
https://realigned.app/blog/the-first-game-with-asmr-music,https://realigned.substack.com/p/the-first-game-with-asmr-music
https://realigned.app/blog/can-a-game-be-both-challenging-and-relaxing,https://realigned.substack.com/p/can-a-game-be-both-challenging-and-relaxing
"""

def render_html_template(new_url):
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url={new_url}" />
</head>
<body>
    <p>Redirecting to <a rel="canonical" href="{new_url}">{new_url}</a>.</p>
</body>
</html>
"""

def process_csv_data(csv_data):
    for line in csv_data.strip().split("\n"):
        old_url, new_url = line.split(",")
        parsed_url = urlparse(old_url)
        path = parsed_url.path
        if not path.endswith("/"):
            path += "/"
        old_path = "." + path + "index.html"
        html_content = render_html_template(new_url)
        print(old_path)
        os.makedirs(os.path.dirname(old_path), exist_ok=True)
        with open(old_path, "w") as f:
            f.write(html_content)

process_csv_data(csv_data)
