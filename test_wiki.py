import requests

def fetch_crop_image(crop_name):
    query = crop_name.lower()
    if query == 'mungbean': query = 'mung bean'
    elif query == 'mothbeans': query = 'moth bean'
    elif query == 'pigeonpeas': query = 'pigeon pea'
    
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={query}&pithumbsize=500&format=json&origin=*"
        response = requests.get(url).json()
        print(response)
        pages = response.get('query', {}).get('pages', {})
        page_id = list(pages.keys())[0]
        return pages[page_id].get('thumbnail', {}).get('source', None)
    except Exception as e:
        print(e)
        return None

print(fetch_crop_image("rice"))
print(fetch_crop_image("maize"))
