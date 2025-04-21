import cv2
import numpy as np

def process_blood_group_image(image_path):
    blood_image = cv2.imread(image_path)
    if blood_image is None:
        return "Error: Could not read image", {}

    # Convert to grayscale
    blood_image_gray = cv2.cvtColor(blood_image, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    filtered_image = cv2.medianBlur(blood_image_gray, 3)

    # Apply binary threshold (Otsu's method)
    _, binary_image = cv2.threshold(filtered_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Morphological opening to remove small noise
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, se)

    # Canny edge detection
    edge_image = cv2.Canny(filtered_image, 70, 180)

    # Split into 3 regions: Anti-A | Anti-B | Anti-D (Rh)
    h, w = edge_image.shape
    region_a = edge_image[:, :w // 3]
    region_b = edge_image[:, w // 3: 2 * w // 3]
    region_rh = edge_image[:, 2 * w // 3:]

    # Edge density and intensity analysis
    edge_density = lambda img: np.sum(img > 0) / img.size
    mean_intensity = lambda img: np.mean(img)

    e_a, i_a = edge_density(region_a), mean_intensity(region_a)
    e_b, i_b = edge_density(region_b), mean_intensity(region_b)
    e_rh, i_rh = edge_density(region_rh), mean_intensity(region_rh)
    var_rh = np.var(region_rh)

    print(f"[Anti-A] Edge Density: {e_a:.4f}, Mean Intensity: {i_a:.2f}")
    print(f"[Anti-B] Edge Density: {e_b:.4f}, Mean Intensity: {i_b:.2f}")
    print(f"[Anti-D] Edge Density: {e_rh:.4f}, Mean Intensity: {i_rh:.2f}, Variance: {var_rh:.2f}")

    # Thresholds (tune as per your dataset)
    THRESH_EDGE = 0.018
    THRESH_INTENSITY = 120
    THRESH_VAR_RH = 100

    # Detect agglutination
    agglutination_a = e_a > THRESH_EDGE and i_a < THRESH_INTENSITY
    agglutination_b = e_b > THRESH_EDGE and i_b < THRESH_INTENSITY
    agglutination_rh = e_rh > THRESH_EDGE and i_rh < THRESH_INTENSITY and var_rh > THRESH_VAR_RH

    # Determine blood group
    if agglutination_a and agglutination_b:
        blood_group = 'AB+' if agglutination_rh else 'AB-'
    elif agglutination_a:
        blood_group = 'A+' if agglutination_rh else 'A-'
    elif agglutination_b:
        blood_group = 'B+' if agglutination_rh else 'B-'
    else:
        blood_group = 'O+' if agglutination_rh else 'O-'

    return blood_group, {
        "Original": blood_image,
        "Grayscale": blood_image_gray,
        "Filtered": filtered_image,
        "Binary": binary_image,
        "Opened": opened_image,
        "Edges": edge_image,
        "Anti-A Region": region_a,
        "Anti-B Region": region_b,
        "Anti-D(Rh) Region": region_rh
    }