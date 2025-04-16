class Smartphone:
    def __init__(self, brand, model, color, storage):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage

    # Method to display smartphone details
    def display_info(self):
        print(f"Smartphone Info: {self.brand} {self.model}, Color: {self.color}, Storage: {self.storage}GB")

    # Method to make a call
    def make_call(self, number):
        print(f"Calling {number}...")

    # Method to send a message
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")
# Creating an instance of Smartphone
my_phone = Smartphone("Apple", "iPhone 13", "Black", 128)

# Display information about the smartphone
my_phone.display_info()

# Making a call
my_phone.make_call("+123456789")

# Sending a message
my_phone.send_message("+123456789", "Hello, how are you?")
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, color, storage, camera_quality):
        # Inheriting from Smartphone class
        super().__init__(brand, model, color, storage)
        self.camera_quality = camera_quality
    
    # Overriding display_info method
    def display_info(self):
        super().display_info()
        print(f"Camera Quality: {self.camera_quality}MP")

    # New method to take a picture
    def take_picture(self):
        print(f"Taking a picture with {self.camera_quality}MP camera...")
# Creating an instance of SmartphoneWithCamera
camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", "Blue", 256, 108)

# Display info and take a picture
camera_phone.display_info()
camera_phone.take_picture()

