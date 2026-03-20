import hashlib
import hmac

class VehicleApp:
    def __init__(self):
        self.vehicles = {}  # Dictionary to store vehicle details
        # A simple "secret key" used for the digital signature simulation
        self.secret_key = b"my_super_secret_key_123"

    def generate_sha256(self):
        print("\n--- SHA-256 Hashing ---")
        message = input("Enter the text message to hash: ")
        # Convert string to bytes and hash it
        hash_obj = hashlib.sha256(message.encode())
        print(f"SHA-256 Hash: {hash_obj.hexdigest()}")

    def digital_signature_demo(self):
        print("\n--- Message Authentication (HMAC) ---")
        message = input("Enter message to authenticate: ").encode()

        # 1. Generate the 'signature' (HMAC)
        signature = hmac.new(self.secret_key, message, hashlib.sha256).hexdigest()
        print(f"Generated Signature: {signature}")

        # 2. Verify
        print("\n--- Verification Simulation ---")
        check_msg = input("Re-enter the message to verify: ").encode()
        expected_sig = hmac.new(self.secret_key, check_msg, hashlib.sha256).hexdigest()

        if hmac.compare_digest(signature, expected_sig):
            print("Verification Result: Valid Signature ✅ (Message is untampered)")
        else:
            print("Verification Result: Invalid Signature ❌ (Message was changed)")

    def register_vehicle(self):
        print("\n--- Register Vehicle ---")
        plate = input("Enter Number Plate: ").strip().upper()
        
        if plate in self.vehicles:
            print(f"Error: Vehicle with plate {plate} already exists!")
            return

        owner = input("Enter Owner Name: ").strip()
        model = input("Enter Vehicle Model: ").strip()
        
        self.vehicles[plate] = {"owner": owner, "model": model}
        print(f"Vehicle {plate} registered successfully.")

    def retrieve_vehicle(self):
        print("\n--- Retrieve Vehicle Details ---")
        plate = input("Enter Number Plate to search: ").strip().upper()
        
        vehicle = self.vehicles.get(plate)
        if vehicle:
            print(f"Details for {plate}:")
            print(f"  Owner: {vehicle['owner']}")
            print(f"  Model: {vehicle['model']}")
        else:
            print("Error: Number Plate not found.")

    def run(self):
        while True:
            print("\n" + "="*30)
            print("   VEHICLE & SECURITY TOOL")
            print("="*30)
            print("1. Generate SHA-256 Hash")
            print("2. Message Signature (HMAC)")
            print("3. Register Vehicle")
            print("4. Retrieve Vehicle Details")
            print("5. Exit")
            
            choice = input("\nSelect an option (1-5): ")

            if choice == '1':
                self.generate_sha256()
            elif choice == '2':
                self.digital_signature_demo()
            elif choice == '3':
                self.register_vehicle()
            elif choice == '4':
                self.retrieve_vehicle()
            elif choice == '5':
                print("Exiting. Have a great day!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = VehicleApp()
    app.run()
       
     
      
