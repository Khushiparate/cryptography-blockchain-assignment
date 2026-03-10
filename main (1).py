import hashlib
import rsa

# Vehicle database
vehicle_db = {}

# Generate RSA keys once
public_key, private_key = rsa.newkeys(512)


def sha256_hash():
    message = input("Enter message to hash: ")
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    print("SHA-256 Hash:", hash_value)


def digital_signature():
    message = input("Enter message to sign: ").encode()

    # Sign the message
    signature = rsa.sign(message, private_key, 'SHA-256')
    print("Signature generated.")

    # Verify the signature
    try:
        rsa.verify(message, signature, public_key)
        print("Signature is VALID")
    except:
        print("Signature is INVALID")


def register_vehicle():
    plate = input("Enter Number Plate: ").upper()

    if plate in vehicle_db:
        print("Error: Vehicle with this number plate already exists.")
        return

    owner = input("Enter Owner Name: ")
    model = input("Enter Vehicle Model: ")

    vehicle_db[plate] = {
        "owner": owner,
        "model": model
    }

    print("Vehicle Registered Successfully.")


def retrieve_vehicle():
    plate = input("Enter Number Plate: ").upper()

    if plate in vehicle_db:
        print("Owner:", vehicle_db[plate]["owner"])
        print("Model:", vehicle_db[plate]["model"])
    else:
        print("Vehicle not found.")


def menu():
    while True:
        print("\n===== Cryptography & Blockchain App =====")
        print("1. Generate SHA-256 Hash")
        print("2. Digital Signature")
        print("3. Register Vehicle")
        print("4. Retrieve Vehicle")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sha256_hash()

        elif choice == "2":
            digital_signature()

        elif choice == "3":
            register_vehicle()

        elif choice == "4":
            retrieve_vehicle()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


# Run program
menu()2