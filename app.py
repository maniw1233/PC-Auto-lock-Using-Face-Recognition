from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
import psutil  # Required to find and terminate processes by name
import os

app = Flask(__name__)

# Home Route - Main page with options
@app.route('/')
def home():
    success_message = None
    error_message = None

    # Check for the success flag file
    success_flag_path = os.path.join(os.getcwd(), 'dataset', 'success.flag')
    if os.path.exists(success_flag_path):
        success_message = "Face dataset creation was successful."
        os.remove(success_flag_path)  # Remove the flag after reading

    return render_template('index.html', success_message=success_message, error_message=error_message)

# Route to prompt for security PIN
@app.route('/prompt_security', methods=['GET', 'POST'])
def prompt_security():
    if request.method == 'POST':
        entered_pin = request.form.get('pin')
        if entered_pin == '1234':  # Replace with your actual security PIN
            return redirect(url_for('create_dataset'))
        else:
            error_message = "Incorrect security PIN. Please try again."
            return render_template('security_prompt.html', error_message=error_message)

    return render_template('security_prompt.html')

# Route to create face dataset (only accessible after security PIN verification)
@app.route('/create_dataset')
def create_dataset():
    try:
        subprocess.Popen(['python', 'C:\\Users\\heman\\Downloads\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master (1)\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master\\create_face_datasets.py'])
        success_message = "Face dataset creation initiated successfully."
        return render_template('index.html', success_message=success_message)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', error_message=error_message)

# Route to trigger model training
@app.route('/train_model')
def train_model():
    try:
        subprocess.Popen(['python', 'C:\\Users\\heman\\Downloads\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master (1)\\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master\\training_model.py'])
        success_message = "Face recognition model training initiated successfully."
        return render_template('index.html', success_message=success_message)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', error_message=error_message)

# Route to start or stop face recognition system
@app.route('/toggle_recognition', methods=['POST'])
def toggle_recognition():
    action = request.json.get('action')

    try:
        if action == 'start':
            script_path = r'C:\Users\heman\Downloads\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master (1)\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master\lock_unlock_face_recognition.py'
            subprocess.Popen(['python', script_path])
            success_message = "Face recognition system started successfully."
            return jsonify(success_message=success_message)

        elif action == 'stop':
            # Find and terminate the process handling the webcam
            for proc in psutil.process_iter(['pid', 'name']):
                if 'python.exe' in proc.info['name'] and 'lock_unlock_face_recognition.py' in ' '.join(proc.cmdline()):
                    proc.terminate()
            success_message = "Face recognition system stopped successfully."
            return jsonify(success_message=success_message)

        else:
            return jsonify(error_message="Invalid action."), 400

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify(error_message=error_message), 500

if __name__ == '__main__':
    app.run(debug=True)
