from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details', methods=['GET'])
def student_details():
    return jsonify({
        "name": "Jatin Nath",
        "roll_number": "2023BCD0014",
        "register_number": "2023BCD0014"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)