import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# ==============================
# Step 0: Check Files
# ==============================
print("Files in folder:", os.listdir())

image_path = "images.jpg"
img = cv2.imread(image_path)

if img is None:
    print("❌ Image not found. Check filename/path.")
    exit()

# ==============================
# Step 1: Preprocessing
# ==============================
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (128, 128))

# ==============================
# Function: BER Calculation
# ==============================
def calculate_ber(original_bits, noisy_bits):
    return np.sum(original_bits != noisy_bits) / len(original_bits)

# ==============================
# Function: PSNR Calculation
# ==============================
def calculate_psnr(original, reconstructed):
    mse = np.mean((original - reconstructed) ** 2)
    if mse == 0:
        return 100
    return 10 * np.log10((255 ** 2) / mse)

# ==============================
# Function: Bit Flip Channel
# ==============================
def bit_flip_channel(bitstream, p):
    noise = np.random.rand(len(bitstream)) < p
    noisy_bits = np.bitwise_xor(bitstream, noise.astype(np.uint8))
    return noisy_bits

# ==============================
# Function: Gaussian Noise Channel
# ==============================
def gaussian_noise(image, mean=0, std=25):
    noise = np.random.normal(mean, std, image.shape)
    noisy_img = image + noise
    return np.clip(noisy_img, 0, 255).astype(np.uint8)

# ==============================
# Step 2: Convert to Bitstream
# ==============================
flat_pixels = gray.flatten()
bitstream = np.unpackbits(flat_pixels)

# ==============================
# Step 3: Experiment with Different Noise Levels
# ==============================
probabilities = [0.01, 0.05, 0.1, 0.2]
ber_values = []

for p in probabilities:
    noisy_bits = bit_flip_channel(bitstream, p)
    ber = calculate_ber(bitstream, noisy_bits)
    ber_values.append(ber)

# ==============================
# Step 4: Plot BER vs Probability
# ==============================
plt.figure()
plt.plot(probabilities, ber_values, marker='o')
plt.xlabel("Noise Probability")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs Noise Probability")
plt.grid()
plt.show()

# ==============================
# Step 5: Single Case Visualization (p = 0.05)
# ==============================
p = 0.05
noisy_bits = bit_flip_channel(bitstream, p)

# Reconstruct image
reconstructed_pixels = np.packbits(noisy_bits)
reconstructed_img = reconstructed_pixels.reshape(gray.shape)

# Error map
error_map = gray != reconstructed_img

# BER
BER = calculate_ber(bitstream, noisy_bits)

# PSNR
psnr_value = calculate_psnr(gray, reconstructed_img)

print(f"\n📊 Results for p = {p}")
print("BER:", BER)
print("PSNR:", psnr_value)

# ==============================
# Step 6: Denoising (Median Filter)
# ==============================
denoised_img = cv2.medianBlur(reconstructed_img, 3)

psnr_denoised = calculate_psnr(gray, denoised_img)

print("PSNR after Denoising:", psnr_denoised)

# ==============================
# Step 7: Gaussian Noise Comparison
# ==============================
gaussian_img = gaussian_noise(gray)

# ==============================
# Step 8: Visualization
# ==============================
plt.figure(figsize=(12,10))

plt.subplot(2,3,1)
plt.title("Original")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(2,3,2)
plt.title("Bit Flip Noise")
plt.imshow(reconstructed_img, cmap='gray')
plt.axis('off')

plt.subplot(2,3,3)
plt.title("Error Map")
plt.imshow(error_map, cmap='gray')
plt.axis('off')

plt.subplot(2,3,4)
plt.title("Denoised Image")
plt.imshow(denoised_img, cmap='gray')
plt.axis('off')

plt.subplot(2,3,5)
plt.title("Gaussian Noise")
plt.imshow(gaussian_img, cmap='gray')
plt.axis('off')

highlight = reconstructed_img.copy()
highlight[error_map] = 255

plt.subplot(2,3,6)
plt.title(f"Error Highlight\nBER={BER:.4f}")
plt.imshow(highlight, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()