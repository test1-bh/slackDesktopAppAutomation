import subprocess
import requests

def run_slack():
    # Run the Slack command
    subprocess.Popen([r"C:\Users\USER 19\AppData\Local\slack\slack.exe"])

def send_message_and_reply(bot_token, channel_id, message, reply):
    headers = {
        "Authorization": f"Bearer {bot_token}",
        "Content-Type": "application/json"
    }

    # Send the initial message
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        json={"channel": channel_id, "text": message},
        headers=headers
    )
    data = response.json()
    print("Initial message response:", data)

    if not data.get("ok"):
        raise Exception(f"Failed to send message: {data.get('error')}")

    ts = data.get("ts")

    # Send threaded reply
    if ts and reply:
        reply_response = requests.post(
            "https://slack.com/api/chat.postMessage",
            json={"channel": channel_id, "text": reply, "thread_ts": ts},
            headers=headers
        )
        reply_data = reply_response.json()
        print("Thread reply response:", reply_data)
        if not reply_data.get("ok"):
            raise Exception(f"Failed to send threaded reply: {reply_data.get('error')}")
        
# def upload_file_to_slack(bot_token, channel_id, file_path, title=None, thread_ts=None):
#     url = "https://slack.com/api/files.upload"

#     with open(file_path, "rb") as file_data:
#         files = {"file": (file_path, file_data)}

#         form_data = {
#             "channels": channel_id
#         }

#         if title:
#             form_data["title"] = title
#         if thread_ts:
#             form_data["thread_ts"] = thread_ts

#         headers = {
#             "Authorization": f"Bearer {bot_token}"
#         }

#         response = requests.post(url, headers=headers, data=form_data, files=files)
#         result = response.json()
#         print("Upload response:", result)

#         if not result.get("ok"):
#             raise Exception(f"Failed to upload file: {result.get('error')}")

def send_image_link(bot_token, channel_id, image_url, alt_text="Image"):
    headers = {
        "Authorization": f"Bearer {bot_token}",
        "Content-Type": "application/json"
    }

    data = {
        "channel": channel_id,
        "blocks": [
            {
                "type": "image",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/11/Test-Logo.svg",
                "alt_text": alt_text
            }
        ]
    }

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers=headers,
        json=data
    )

    result = response.json()
    print("Image block post response:", result)
    if not result.get("ok"):
        raise Exception(f"Failed to send image block: {result.get('error')}")


