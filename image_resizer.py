import os
from PIL import Image

INPUT_FOLDER = 'images_original' 

OUTPUT_FOLDER = 'images_resized'
THUMBNAIL_SIZE = (300, 300) 
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff')

def resize_images():
    """
    Reads images from the INPUT_FOLDER, resizes them using THUMBNAIL_SIZE, 
    and saves them to the OUTPUT_FOLDER while preserving the original file names 
    and aspect ratios.
    """
    print("---Image Resizer ---") 
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created output folder: '{OUTPUT_FOLDER}'")
    try:
        files_to_process = os.listdir(INPUT_FOLDER)
    except FileNotFoundError:
        print(f"\nERROR: Input folder '{INPUT_FOLDER}' not found!")
        print("Please create this folder and add your images before running the script.")
        return
    processed_count = 0
    for filename in files_to_process:
      
        input_path = os.path.join(INPUT_FOLDER, filename)
        
        if os.path.isdir(input_path) or not filename.lower().endswith(VALID_EXTENSIONS):
            print(f"Skipping non-image file/directory: {filename}")
            continue
        try: 
            with Image.open(input_path) as img:              
                img.thumbnail(THUMBNAIL_SIZE) 
                output_path = os.path.join(OUTPUT_FOLDER, filename)
                img.save(output_path) 
                print(f"Successfully resized and saved: {filename}")
                processed_count += 1
                
        except Exception as e:        
            print(f"An unexpected error occurred while processing {filename}: {e}")

    print(f"\n--- Batch Process Complete ---")
    print(f"Total files processed successfully: {processed_count}")
    print(f"Check the '{OUTPUT_FOLDER}' folder for your resized images.")

if __name__ == '__main__':
    resize_images()