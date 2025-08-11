# task-7-Image-Resizer-Tool


A simple web application that allows users to upload an image, resize it to specific dimensions, and download the resized version.  
Built using **Flask** and **Pillow**.

---

## Features
- Upload an image via a web form.
- Resize images to any custom width and height.
- Download the resized image instantly.
- Lightweight and easy to run.

---

## Requirements
Install the required Python packages:

```bash
pip install flask pillow
```

---

## Project Structure
```
image_resizer/
│
├── app.py              # Flask backend
├── templates/
│   └── index.html       # Frontend form
├── static/
│   └── uploads/         # Uploaded images
└── README.md
```

---

## How to Run

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/image_resizer.git
cd image_resizer
```

2. **Install dependencies**
```bash
pip install flask pillow
```

3. **Run the Flask app**
```bash
python app.py
```

4. **Access the app**  
Open your browser and go to:
```
http://127.0.0.1:5000
```

5. **Upload and Resize**  
- Select an image file.  
- Enter width and height.  
- Click **Resize** to download the resized image.

---

## Example
**Before:** 1920×1080  
**After:** 800×600  

---

## Notes
- Uploaded images are stored in the `static/uploads` folder.  
- Supported formats: `.jpg`, `.jpeg`, `.png`.  
- You can adjust allowed formats in `app.py`.

---

## Author
GOKULAKANNAN S C
