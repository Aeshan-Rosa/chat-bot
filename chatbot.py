from openai import OpenAI
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QFont
import sys

# Initialize OpenAI client
client = OpenAI(api_key="my api")  

# Function to communicate with OpenAI API
def chat_with_openai(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": '''You are Hydra AI, an advanced chatbot designed to assist users with Hydra Hex, the ultimate Free Fire panel.
            Your goal is to provide expert guidance, real-time tips, and seamless panel integration to help users optimize their Free Fire experience.

            Features you support:
            - Hydra Hex Panel Assistance: Explain features, settings, and provide step-by-step instructions.
            - Free Fire Game Assistance: Offer strategies, aim training tips, and gameplay optimization.
            - Personalized User Experience: Remember user preferences and adapt recommendations.
            - Secure & Responsible Use: Educate users on safe and responsible interaction with Hydra Hex.

            Be engaging, informative, and precise. Always maintain a gaming-friendly, supportive tone.
            if the user asks anyhting other than hydra hex or related to Freefire say to them that they are asking 
            out of your bounds and renavigate them to ask about hydra hex and freefire.
            all the features in hydra hex are 100 percent legal so make sure that to not say anything about your 
            legal things,just say how to fix the feature.'''},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Create PyQt6 UI
class HydraAIChatbot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hydra AI")
        self.setGeometry(200, 200, 800, 500)
        
        # Layout
        layout = QVBoxLayout()

        # Title Label
        self.title_label = QLabel("HYDRA AI - FreeFire Panel Assistant")
        self.title_label.setFont(QFont("Times New Roman", 18, weight=QFont.Weight.Bold))
        layout.addWidget(self.title_label)

        # Chat Display
        self.chat_display = QTextBrowser()
        self.chat_display.setFont(QFont("Times New Roman", 16))
        layout.addWidget(self.chat_display)

        # Input Area
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setFixedHeight(40)
        self.input_box.setFont(QFont("Times New Roman", 16))
        self.input_box.setPlaceholderText("Type your message here...")
        input_layout.addWidget(self.input_box)

        # Send Button
        self.send_button = QPushButton("Send")
        self.send_button.setFont(QFont("Times New Roman", 16))
        self.input_box.setFixedHeight(40)
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

        # Welcome message
        self.chat_display.append("HYDRA AI: Welcome to Hydra HEX! I am Hydra AI. How can I assist you today? 🚀\n")

    def send_message(self):
        user_text = self.input_box.text().strip()
        if user_text:
            self.chat_display.append(f"You: {user_text}\n")
            self.input_box.clear()

            # Get AI response
            response = chat_with_openai(user_text)
            self.chat_display.append(f"HYDRA AI: {response}\n")

# Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HydraAIChatbot()
    window.show()
    sys.exit(app.exec())
