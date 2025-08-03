import requests

api_key = '491d91b273a24193468205f0f4cba2ba'
movie_id = 550  # Fight Club
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("✅ Success! Movie title:", data['title'])
    print("🎬 Poster URL:", "https://image.tmdb.org/t/p/w500/" + data["poster_path"])
else:
    print("❌ Failed to fetch movie data. Error code:", response.status_code)
