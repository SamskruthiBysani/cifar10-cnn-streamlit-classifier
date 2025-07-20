# 🧠 CIFAR-10 Image Classifier using CNN and Streamlit

This project showcases a simple yet powerful image classifier built using a Convolutional Neural Network (CNN) trained on the **CIFAR-10** dataset. The trained model is deployed with a clean and interactive **Streamlit** web interface, allowing users to upload an image and get a prediction from 10 possible classes.

## 📦 What’s Inside

- `app.py` – Streamlit app that loads the model and predicts the class of uploaded images.
- `cifar10_model.keras` – The trained CNN model saved in Keras format.
- `cnn_training.ipynb` – Jupyter Notebook used to train the CNN.
- `requirements.txt` – Python dependencies needed to run the project.

## 📊 CIFAR-10 Classes

The model predicts one of the following classes:
['airplane', 'automobile', 'bird', 'cat', 'deer',
'dog', 'frog', 'horse', 'ship', 'truck']

bash
Copy
Edit

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/cifar10-image-classifier.git
cd cifar10-image-classifier
2. Install dependencies
Make sure you have Python 3.7+ installed, then:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
Then go to http://localhost:8501 in your browser.

📷 Upload Instructions
Upload a 32x32 PNG/JPG image (model expects CIFAR-10 format).

The app will show the image and predict the most likely class.

🛠 Tech Stack
Python

TensorFlow / Keras

Streamlit

NumPy

PIL (Pillow)

🤖 Model Performance
Trained using a simple CNN on the CIFAR-10 dataset.

Achieved ~accuracy of 75–80% on test data.

Suitable for learning/demo purposes.

📌 Notes
This app demonstrates:

How to train a CNN on CIFAR-10

How to save and load a Keras model

How to deploy with Streamlit locally

📚 License
This project is open-source and available under the MIT License.

Made with ❤️ by Samskruthi
