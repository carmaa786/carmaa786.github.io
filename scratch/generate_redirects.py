import os

redirects = [
    ("/blogs/doorstep-car-cleaning-service-noida", "/doorstep-car-washing-service-in-noida/"),
    ("/why-carmaa-is-becoming-dehradun's-choice", "/blogs/why-carmaa-is-becoming-dehradun's-choice/"),
    ("/blogs/doorstep-car-washing-service-in-gurgaon/", "/doorstep-car-washing-service-in-gurgaon/"),
    ("/doorstep-car-washing-service-in-delhi/blogs/", "/doorstep-car-washing-service-in-delhi/"),
    ("/best-car-mechanics-in-dehradun/blogs/", "/best-car-mechanics-in-dehradun/"),
    ("/blogs/why-carmaa-is-becoming-dehradun's-choice/blogs/", "/blogs/why-carmaa-is-becoming-dehradun's-choice/"),
    ("/blogs/dry-cleaning-services-at-your-doorstep/blogs/", "/blogs/dry-cleaning-services-at-your-doorstep/"),
    ("/blogs/about/", "/about/"),
    ("/blogs/doorstep-car-washing-service-in-dehradun/", "/doorstep-car-washing-service-in-dehradun/"),
    ("/blogs/doorstep-car-washing-service-in-meerut/", "/doorstep-car-washing-service-in-noida/"),
    ("/doorstep-car-washing-service-in-Rishikesh/blogs/", "/doorstep-car-washing-service-in-dehradun/"),
    ("/doorstep-car-washing-service-in-Haridwar/blogs/", "/doorstep-car-washing-service-in-dehradun/"),
    ("/doorstep-car-washing-service-in-aligarh/", "/"),
    ("/doorstep-car-washing-service-in-roorkee/", "/"),
    ("/doorstep-car-washing-service-in-haldwani/", "/"),
    ("/doorstep-car-washing-service-in-chandigarh/", "/"),
    ("/doorstep-car-washing-service-in-mussoorie/", "/")
]

def create_redirect(path, destination):
    # Remove leading slash for folder creation
    folder_path = path.lstrip('/')
    
    # Ensure folder path ends with index.html if it's a directory-style URL
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        
    file_path = os.path.join(folder_path, "index.html")
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <link rel="canonical" href="https://carmaacarcare.com{destination}">
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta http-equiv="refresh" content="0;url={destination}">
</head>
<body>
  <p>Redirecting to <a href="{destination}">{destination}</a>...</p>
  <script>window.location.href = "{destination}";</script>
</body>
</html>
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Created redirect: {path} -> {destination}")

for path, destination in redirects:
    create_redirect(path, destination)
