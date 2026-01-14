import secrets
import string

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def generate_password(length, use_upper, use_lower, use_nums, use_syms):
    char_pool = ""
    if use_upper: char_pool += string.ascii_uppercase
    if use_lower: char_pool += string.ascii_lowercase
    if use_nums: char_pool += string.digits
    if use_syms: char_pool += string.punctuation

    if not char_pool:
        return "Select at least one option!"

    # Securely select random characters from the pool
    return ''.join(secrets.choice(char_pool) for _ in range(length))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    password = generate_password(
        length=int(data.get('length', 12)),
        use_upper=data.get('upper', True),
        use_lower=data.get('lower', True),
        use_nums=data.get('nums', True),
        use_syms=data.get('syms', False)
    )
    return jsonify({'password': password})


if __name__ == '__main__':
    app.run(debug=True)
