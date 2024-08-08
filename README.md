# PC-Auto-lock-Using-Face-Recognition

Welcome to **PC-Auto-lock-Using-Face-Recognition**!

Thank you for checking out this project! The primary aim of this project is to ensure that your computer remains secure by locking it instantly if someone who is not recognized or not registered in the system tries to access it. This provides an additional layer of protection, reducing the risk of unauthorized access.

---

## Key Features

- **Automatic Locking**: Locks your PC automatically when an unregistered or unauthorized face is detected.
- **Enhanced Security**: Ensures only recognized users can keep the computer unlocked.
- **Real-Time Detection**: Continuously monitors and verifies faces for seamless security.

---

*This is italicized text*

---

## Objective

The objective of the PC Auto Lock Using Face Recognition project is to enhance computer security by implementing an automatic locking mechanism. The system utilizes face recognition technology to identify users and locks the PC when an unauthorized or unregistered face is detected. This approach ensures that only verified users can access the computer, providing a higher level of security and protection against unauthorized access.

---

## Implementation

The feature involves continuously running the webcam until an unregistered face is detected. When an unregistered face is detected, the PC will automatically lock. The project includes an "auto-lock" toggle key that the Admin can turn on or off as needed. When enabled, the webcam continuously runs until the Admin turns off the toggle key or an unregistered face is detected.

---

## Installations

To set up the project, you'll need the following Python packages:

- `opencv-python-headless`
- `numpy`
- `pyautogui`
- `pillow`
- `opencv-python`
- `gunicorn`
- `flask`
- `psutil`

---

## Steps for Setup the Project:

 1. download the project Zip folder form my github account, then extract that zip folder in your PC or Laptop.
 2. Doownload the VSCode and open the project folder from where You Extracted.
 3. open terminal in VSCode and run This command `pip install -r requirements.txt` it install all the requred tools for run this project.
 4. change all the path from `create_face_datasets.py`,`lock_unlock_face_recognition.py`, `training_model.py` ,`app.py` also in the `script_runner.bat`  example path r'C:\Users\heman\Downloads\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master (1)\Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition-master  ,you should change to your folder path.
 5. in `script_runner.bat` file you should change only the `lock_unlock_face_recognition.py` path.
 6. if you done all this steps correctly then run the project by run this command in terminal `python app.py`.
 7. after you run `python app.py` command you get one url http://127.0.0.1:8000/  click that ,once you click that it will go to web browser.


---
## my Web Interface Design :

![WhatsApp Image 2024-08-08 at 7 36 41 PM (1)](https://github.com/user-attachments/assets/0a7c5953-5f74-4003-8271-bf7ea763203f)
![WhatsApp Image 2024-08-08 at 7 36 41 PM](https://github.com/user-attachments/assets/095f6156-af68-43bb-a01f-3cde392f5ad0)

---

## steps for run the project :
 1. for run the project you should run this command in terminal `python app.py` then click this url http://127.0.0.1:8000/ afetr click this you should go to web browser and run the project.
 2. In this project fisrt You Register your Face by clicking the create face Dataset in the browser, then it will ask the admin security pin enter the security pin '1234'.
 3. After you enter the security pin the webcam will on and start for face registration you should give some changes in the position your face (left,right,up down) and give some expression.
 4. after that train the model by clicking 'train face recognision model' after you clicking the this button you shoild wiat some few second (5sec).
 5. after you train the model you on the 'Auto-Lock' toggle key and start the face recognition.
 6. if the register face is detected the webcam will be continuesly runing until the un register face is detected ,if the unregister face is detected the pc will automaticly lock.

