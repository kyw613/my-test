from datetime import datetime
import os
from django.conf import settings  # Import Django settings module

def upload_image(file, directory):
    try:
        # Define the base directory to store the files
        base_dir = os.path.join(settings.MEDIA_ROOT)  # Use MEDIA_ROOT from settings
        print("base_dir", base_dir)
        # Ensure the directory exists
        os.makedirs(base_dir, exist_ok=True)
        
        # Create a unique file path
        target_path = os.path.join(base_dir, f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{file.name}")
        
        # Save the file
        with open(target_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Return a relative URL path that might be used in web contexts
        print(f"/media/{directory}/{datetime.now().strftime('%Y%m%d%H%M%S')}-{file.name}")
        return f"/media/{datetime.now().strftime('%Y%m%d%H%M%S')}-{file.name}"
    except Exception as e:
        print(f"Failed to save file: {e}")
        return None
