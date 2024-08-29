def get_content_type(file_path):
    if file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        type = 'image/jpeg'
    elif file_path.endswith('.png'):
        type = 'image/png'
    elif file_path.endswith('.gif'):
        type = 'image/gif'
    elif file_path.endswith('.txt'):
        type = 'text/plain; charset=UTF-8'
    elif file_path.endswith('.html'):
        type = 'text/html'
    elif file_path.endswith('.json'):
        type = 'application/json'
    elif file_path.endswith('.mp4'):
        type = 'video/mp4'
    elif file_path.endswith('.webm'):
        type = 'video/webm'
    elif file_path.endswith('.pdf'):
        type = 'application/pdf'
    else:
        type = 'application/octet-stream'
    return type
