# ml_app/views.py

from django.http import JsonResponse
import joblib

def predict_with_ml_model(request):
    if request.method == 'POST':
        try:
            # Load the trained model from disk
            model = joblib.load('ml_models/my_model.pkl')

            # Perform predictions using the model (provide your own data)
            input_data = ...  # Replace with your input data
            predictions = model.predict(input_data)

            # Return predictions as JSON
            return JsonResponse({'predictions': predictions.tolist()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
