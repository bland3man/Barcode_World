import cv2
from pyzbar.pyzbar import decode

barcode_data = []

# Loop through the range of image numbers
for i in range(1, 9375):
    # Construct the file path for the image
    image_path = fr"C:\Users\bwallace\Downloads\3da79483a93cdd2519b110714ca3d06a780644da\Barcode_World\{i}.png"
    
    try:
        # Read the image
        image = cv2.imread(image_path)
        
        if image is not None:
            # Decode barcodes from the image
            detected_barcodes = decode(image)
            
            # Append barcode data to the list
            for barcode in detected_barcodes:
                barcode_data.append(barcode.data.decode('utf-8'))  # Decode bytes to string
        else:
            print(f"Failed to read image: {image_path}")
    except Exception as e:
        print(f"Error processing image: {image_path}")
        print(e)

# Concatenate barcode data into a single string
barcode_data_concatenated = "".join(barcode_data)

# Convert the ASCII to text
barcode_text = ''.join(chr(int(code)) for code in barcode_data_concatenated.split())

# Print the output
print("Concatenated barcode data:", barcode_text)


