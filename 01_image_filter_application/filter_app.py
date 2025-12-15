"""
Image Filter Application - Processes images with grayscale, blur, and edge detection filters
Usage: python filter_app.py -i input.jpg -o output_folder
"""

import cv2
import argparse
import os

def apply_filters(image_path, output_dir):
    """Apply three basic filters to an image and save results."""
    
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image {image_path}")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get base filename
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    
    # 1. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{output_dir}/{base_name}_grayscale.jpg", gray)
    
    # 2. Apply Gaussian blur
    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(f"{output_dir}/{base_name}_blurred.jpg", blurred)
    
    # 3. Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    cv2.imwrite(f"{output_dir}/{base_name}_edges.jpg", edges)
    
    print(f"✓ Processed {image_path}")
    print(f"  - Grayscale saved as: {base_name}_grayscale.jpg")
    print(f"  - Blurred saved as:   {base_name}_blurred.jpg")
    print(f"  - Edges saved as:     {base_name}_edges.jpg")

    

def main():
    parser = argparse.ArgumentParser(description="Image Filter Application")
    parser.add_argument("-i", "--input", required=True, help="Input image path")
    parser.add_argument("-o", "--output", required=True, help="Output directory")
    
    args = parser.parse_args()
    
    # Time the processing
    import time
    start_time = time.time()
    
    apply_filters(args.input, args.output)
    
    elapsed = time.time() - start_time
    print(f"\n✅ Processing completed in {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()