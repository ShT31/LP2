import random
import re

# Dictionary of possible customer inquiries and their respective responses
responses = {
    "greeting": ["Hello! Welcome to our mobile repairing shop. How can I assist you today?", "Hi there! How may I help you with your mobile?", "Welcome! What seems to be the problem with your phone?"],
    "farewell": ["Thank you for choosing our mobile repairing services. Have a great day!", "Your satisfaction is our top priority. Goodbye!", "If you have any more questions, feel free to ask. Take care and goodbye!"],
    "help": ["Sure, I'm here to help. What issues are you facing with your mobile?", "How can I assist you with your mobile repair? Please let me know.", "I'm here to provide the best possible solutions for your mobile problems. What do you need help with?"],
    "screen_cracked": ["A cracked screen is a common issue. We can replace the screen for you. Please bring your mobile to our shop, and our technicians will take care of it.", "Oh no! A cracked screen can be quite bothersome. Don't worry, we offer screen replacement services. Visit our shop, and we'll fix it for you."],
    "battery_problem": ["If you're experiencing battery issues, we can replace your mobile's battery. Bring it to our shop, and we'll ensure it gets fixed.", "Battery problems are quite common. We can replace your mobile's battery with a new one. Please visit our shop for assistance."],
    "software_issue": ["Software issues can often be resolved by resetting your mobile or updating its software. We can assist you with that. Please bring your phone to our shop, and our technicians will help you out.", "Software problems can be frustrating. We recommend trying a software reset or update. If the issue persists, our technicians can assist you further. Just drop by our shop."],
    "water_damage": ["Water damage can be critical for mobiles. We suggest immediately turning off your device and bringing it to our shop for professional repair. Do not attempt to power it on.", "Water damage requires immediate attention. Please switch off your mobile, remove any SIM cards or memory cards, and bring it to our shop. Our experts will assess the damage and offer a suitable solution."],
    "default": ["I apologize, but I couldn't understand your request.", "Apologies, I didn't quite get that. Could you please rephrase?", "I'm still learning. Can you provide more information?"],
     "phone_not_turning_on": ["If your phone isn't turning on, try charging it for a while. If it still doesn't turn on, there might be a hardware issue. Bring it to our shop for diagnosis and repair.", "Phone not turning on? First, check if the battery is charged. If it still won't power up, visit our shop for professional assistance."],
    "speaker_issue": ["Having trouble with the speaker? We can diagnose and repair speaker issues. Bring your phone to our shop, and we'll take care of it.", "If you're experiencing problems with the speaker, it could be a hardware issue. Let our technicians examine your phone at our shop for a solution."],
    "camera_not_working": ["Is your camera malfunctioning? We offer camera repair services. Visit our shop, and we'll troubleshoot and fix the issue for you.", "Camera not working? Don't worry, we specialize in camera repairs. Bring your phone to our shop, and we'll get it working again."],
    "touchscreen_unresponsive": ["If your touchscreen is unresponsive, try restarting your phone. If that doesn't work, it might be a hardware issue. Bring it to our shop for expert assistance.", "Having trouble with the touchscreen? A restart might help, but if not, visit our shop for professional diagnosis and repair."]
}

# Function to handle customer inquiries
def respond_to_inquiry(inquiry):
    inquiry = inquiry.lower()
    if re.search(r"\b(?:hello|hi)\b", inquiry):
        return random.choice(responses["greeting"])
    elif re.search(r"\b(?:goodbye|bye)\b", inquiry):
        return random.choice(responses["farewell"])
    elif re.search(r"\b(?:help|support)\b", inquiry):
        return random.choice(responses["help"])
    elif re.search(r"\b(?:screen|cracked)\b", inquiry):
        return random.choice(responses["screen_cracked"])
    elif re.search(r"\b(?:battery|charge)\b", inquiry):
        return random.choice(responses["battery_problem"])
    elif re.search(r"\b(?:software|update|reset)\b", inquiry):
        return random.choice(responses["software_issue"])
    elif re.search(r"\b(?:water|damage)\b", inquiry):
        return random.choice(responses["water_damage"])
    elif re.search(r"\b(?:phone|turning|on)\b", inquiry):
        return random.choice(responses["phone_not_turning_on"])
    elif re.search(r"\b(?:speaker)\b", inquiry):
        return random.choice(responses["speaker_issue"])
    elif re.search(r"\b(?:camera)\b", inquiry):
        return random.choice(responses["camera_not_working"])
    elif re.search(r"\b(?:touchscreen|unresponsive)\b", inquiry):
        return random.choice(responses["touchscreen_unresponsive"])
    else:
        return random.choice(responses["default"])


# Main loop to simulate customer interaction
print("Welcome to the Customer Interaction Chatbot!")
print("Type 'exit' to end the conversation.")

while True:
    user_input = input("Customer: ")

    if user_input.lower() == "exit":
        break

    bot_response = respond_to_inquiry(user_input)
    print("Chatbot: " + bot_response)

print("Thank you for using the Customer Interaction Chatbot. Goodbye!")