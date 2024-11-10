from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from livemodel import predict
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)
CORS(app)

# Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_monopharm_side_effects(drug_name):
    """
    Queries the mono_SE table for the side effects of a single drug.
    """
    response = supabase.table("mono_SE").select("side_effects").eq("drug_name", drug_name).execute()
    if response.data:
        # Extract side effects directly from the response
        side_effects = response.data[0]['side_effects']  # Assuming side_effects is stored as a JSON array
        return side_effects
    else:
        return []

def get_polypharm_side_effects(drug_1, drug_2):
    """
    Queries the poly_SE table for side effects between two drugs.
    """
    # Adjust the query to handle field names with spaces correctly and simplify the condition
    response = supabase.table("poly_SE").select('"Side Effects"').or_(
        f'"Drug 1".eq.{drug_1}, "Drug 2".eq.{drug_2}, "Drug 1".eq.{drug_2}, "Drug 2".eq.{drug_1}'
    ).execute()

    if response.data:
        # Extract side effects directly from the response
        side_effects = response.data[0]["Side Effects"]  # Assuming "Side Effects" is stored as a JSON array
        return side_effects
    else:
        return []

@app.route('/mono_se', methods=['GET'])
def mono_se():
    drug_name = request.args.get('drug_name')
    if not drug_name:
        return jsonify({"error": "drug_name parameter is required"}), 400

    # Retrieve monopharmacy side effects
    side_effects = get_monopharm_side_effects(drug_name)
    return jsonify({"drug_name": drug_name, "side_effects": side_effects})

@app.route('/poly_se', methods=['GET'])
def poly_se():
    drug_1 = request.args.get('drug_1')
    drug_2 = request.args.get('drug_2')
    if not drug_1 or not drug_2:
        return jsonify({"error": "Both drug_1 and drug_2 parameters are required"}), 400

    # Retrieve polypharmacy side effects
    side_effects = get_polypharm_side_effects(drug_1, drug_2)
    return jsonify({"drug_1": drug_1, "drug_2": drug_2, "side_effects": side_effects})

# Endpoint for medicine prediction from image
@app.route('/predict', methods=['POST'])
def predict_medicine():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    image_bytes = file.read()
    predicted_medicine, confidence = predict(image_bytes)
    return jsonify({"predicted_medicine": predicted_medicine, "confidence": f"{100 * confidence:.2f}%"})

if __name__ == '__main__':
    app.run(debug=True)
