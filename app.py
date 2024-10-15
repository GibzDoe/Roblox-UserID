from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def check_roblox_profile(user_id):
    url = f"https://users.roblox.com/v1/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "name" in data:
            return {"status": "success", "username": data['name'], "userId": user_id}
        else:
            return {"status": "error", "message": "Profile not found"}
    else:
        return {"status": "error", "message": f"Unable to reach Roblox API. Status code: {response.status_code}"}

# Create the API endpoint
@app.route('/check_profile', methods=['GET'])
def check_profile():
    # Get the user_id from query parameters
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"status": "error", "message": "Missing user_id parameter"}), 400

    # Call the function to check the Roblox profile
    result = check_roblox_profile(user_id)
    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
