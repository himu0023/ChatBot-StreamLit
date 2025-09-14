# 🤖 Basic Chatbot

A conversational AI chatbot built with Streamlit and machine learning using TF-IDF vectorization and Logistic Regression.

## Features

- Natural language processing with NLTK
- Machine learning-based intent recognition
- Multiple conversation topics (greetings, goodbye, thanks, help, age, weather, fitness, life)
- Simple and intuitive web interface
- Real-time responses

## Technologies Used

- Python 3
- Streamlit (Web interface)
- Scikit-learn (TF-IDF Vectorizer + Logistic Regression)
- NLTK (Natural Language Toolkit)

## Installation

1. Clone the repository:
```bash```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install required dependencies:

```bash```
pip install -r requirements.txt

3. Download NLTK data:
```python```
import nltk
nltk.download('punkt')
## How to Run

### Method 1: Using Streamlit (Recommended)
```bash```
streamlit run app.py

### Method 2: Alternative run command
```bash```
python -m streamlit run app.py

### Method 3: With specific port (if default port 8501 is busy)
```bash```
streamlit run app.py --server.port 8502

## Usage
1. After running the command, your browser will automatically open at http://localhost:8501
2. Type your message in the input box and press Enter
3. The chatbot will respond based on the trained intents
4. Type "goodbye" or "bye" to end the conversation

## Project Structure
```text```
chatbot-project/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation

## Intents Configuration
The chatbot understands these conversation topics:
* Greetings (Hi, Hello, Hey)
* Goodbye (Bye, See you later)
* Thanks (Thank you, Thanks)
* About (Who are you, What can you do)
* Help (Help, I need help)
* Age (How old are you)
* Weather (What's the weather like)
* Fitness (How to stay fit)
* Life (Philosophical questions)

## Customization
To add new intents, modify the intents list in app.py:

```python```
{
    "tag": "your_new_tag",
    "patterns": ["pattern1", "pattern2", "pattern3"],
    "responses": ["response1", "response2", "response3"]
}

### Requirements
Create a requirements.txt file with:

```txt```
streamlit==1.32.0
scikit-learn==1.4.0
nltk==3.8.1

## Troubleshooting
Port already in use:
```bash```
streamlit run app.py --server.port 8502

## NLTK data not found:
```python```
import nltk
nltk.download('punkt')

## Module not found errors:
```bash```
pip install -r requirements.txt

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License
This project is open source and available under the MIT License.

## Author
Created by Himu23



