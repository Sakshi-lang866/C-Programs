import time

while True:
    message = input("Enter message: ")

    print("\nSending message...")
    time.sleep(1)

    print("\n--- E Notice Board ---")
    print("Displaying Message:")
    print(message)

    choice = input("\nSend another message? (y/n): ")
    if choice.lower() != 'y':
        break
