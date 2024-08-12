responses = {
    "hi": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "hello": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "hey": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "do you have smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "shipping time": "Shipping usually takes 3-5 business days.",
    "how long is shipping": "Shipping usually takes 3-5 business days.",
    "how long does shipping take": "Shipping usually takes 3-5 business days.",
    "shipping methods": "We offer standard, expedited, and overnight shipping.",
    "return policy": "You can return products within 30 days of receipt for a full refund.",
    "how to return": "To return a product, please visit our returns page for a step-by-step guide.",
    "return a product": "To return a product, please visit our returns page for a step-by-step guide.",
    "won’t turn on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "won't turn on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "reset device": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "reset my device": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "reset gadget": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "bye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!",
    "goodbye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!",
    "exit": "Goodbye! If you have any more questions, we're here to help.",
    "quit": "Goodbye! If you have any more questions, we're here to help.",
    "contact human": "Please hold on while I connect you to a human representative.",
    "talk to human": "Please hold on while I connect you to a human representative.",
    "representative": "Please hold on while I connect you to a human representative."
}

unrecognized_count = 0

def get_bot_response(user_input):
    global unrecognized_count
    user_input = user_input.lower()

    for keyword, response in responses.items():
        if keyword in user_input:
            unrecognized_count = 0  # reset the counter when a valid response is found
            return response

    unrecognized_count += 1
    if unrecognized_count >= 3:
        unrecognized_count = 0  # reset counter after directing to human
        return "I'm having trouble understanding. Please hold on while I connect you to a human representative."
    
    return "I'm not sure how to respond to that. Can you try asking something else?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! If you have any more questions, we're here to help.")
        break

    response = get_bot_response(user_input)
    print(f"Bot: {response}")

