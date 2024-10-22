from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

# Zodiac signs with their date ranges
zodiac_signs = [
    ('Capricorn', (12, 22), (1, 19)),
    ('Aquarius', (1, 20), (2, 18)),
    ('Pisces', (2, 19), (3, 20)),
    ('Aries', (3, 21), (4, 19)),
    ('Taurus', (4, 20), (5, 20)),
    ('Gemini', (5, 21), (6, 20)),
    ('Cancer', (6, 21), (7, 22)),
    ('Leo', (7, 23), (8, 22)),
    ('Virgo', (8, 23), (9, 22)),
    ('Libra', (9, 23), (10, 22)),
    ('Scorpio', (10, 23), (11, 21)),
    ('Sagittarius', (11, 22), (12, 21)),
]

def get_zodiac_sign(dob):
    """Determine the zodiac sign from DOB."""
    month = dob.month
    day = dob.day
    for sign, start, end in zodiac_signs:
        if (start[0] == month and start[1] <= day) or (end[0] == month and end[1] >= day):
            return sign
    return 'Capricorn'  # Default fallback (for borderline dates)

def calculate_bechaini(zodiac_sign):
    """Calculate a bechaini score based on the zodiac sign."""
    base_score = random.randint(50, 100)  # Random base score
    zodiac_influence = {
        'Gemini': 10, 'Virgo': 10, 'Aquarius': 10,
        'Aries': 5, 'Leo': 5, 'Scorpio': 5,
        'Taurus': -10, 'Pisces': -10, 'Libra': -10
    }
    return min(100, max(50, base_score + zodiac_influence.get(zodiac_sign, 0)))  # Ensure score stays within 50-100

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dob_str = request.form['dob']
        dob = datetime.strptime(dob_str, '%Y-%m-%d')
        zodiac_sign = get_zodiac_sign(dob)
        bechaini_score = calculate_bechaini(zodiac_sign)
        return render_template('result.html', name=name, zodiac_sign=zodiac_sign, bechaini_score=bechaini_score)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
