from django.shortcuts import render
import requests

# Create your views here.

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/query"

def chatbot_view(request):
    response_text = ""
    if request.method == "POST":
        platform = request.POST.get("platform")
        question = request.POST.get("question")

        # Send the query to the FastAPI backend
        try:
            response = requests.post(API_URL, json={"platform": platform, "question": question})
            response_data = response.json()
            response_text = response_data.get("answer", "Sorry, something went wrong.")
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "chatbot/index.html", {"response": response_text})
