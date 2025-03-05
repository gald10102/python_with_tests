import requests

def get_status_code(url):
    """
    שלח בקשה לאתר ותחזיר את קוד הסטטוס.
    """
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
