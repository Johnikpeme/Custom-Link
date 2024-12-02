import os
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def redirect_to_store():
    user_agent = request.headers.get('User-Agent', 'Unknown')
    print(f"User-Agent: {user_agent}")

    if "iPhone" in user_agent or "iPad" in user_agent:
        return redirect("https://apps.apple.com/si/app/nouns-hunt/id1667269607")
    elif "Android" in user_agent:
        return redirect("https://play.google.com/store/apps/details?id=com.DashStudios.NounsFlutter&hl=en")
    else:
        return redirect("https://play.google.com/store/apps/details?id=com.DashStudios.NounsFlutter&hl=en")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Use Render's provided PORT
    app.run(host='0.0.0.0', port=port)
