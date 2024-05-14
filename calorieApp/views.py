from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        response = requests.get(api_url + query, headers={'X-Api-Key': 'mwmSgJkC/rHgVjWe1QpQPw==lC81SizR8lLMQRCp'})
        if response.status_code == requests.codes.ok:
            data = response.json()
            print(data)
            items = data.get('items', [])
            return render(request, 'calorieApp/index.html', {'items': items})
        else:
            error_message = f"Error: {response.status_code} {response.text}"
            return render(request, 'calorieApp/index.html', {'error_message': error_message})
    return render(request, 'calorieApp/index.html')