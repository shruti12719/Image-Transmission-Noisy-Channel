# 📡 Image Transmission over Noisy Channel

## 📌 Description

This project simulates the transmission of an image over a noisy communication channel. The image is converted into a binary bitstream, transmitted with random errors (bit flips and Gaussian noise), and reconstructed at the receiver. The system evaluates performance using Bit Error Rate (BER) and Peak Signal-to-Noise Ratio (PSNR), along with error visualization and noise reduction.



## 🚀 Features

* Image to Bitstream Conversion
* Binary Symmetric Channel (Bit Flip Noise)
* Gaussian Noise Simulation
* Error Map Visualization
* BER and PSNR Calculation
* Median Filtering for Denoising
* BER vs Noise Probability Graph



## 🛠️ Technologies Used

* Python
* NumPy
* OpenCV
* Matplotlib



## 📂 Project Structure

```
Image-Transmission-Noisy-Channel/
│
├── project.py
├── images.jpg
├── requirements.txt
├── results/
│   ├── output.png
│   ├── ber_graph.png
├── report/
│   └── project_report.pdf
```



## ▶️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Image-Transmission-Noisy-Channel.git
cd Image-Transmission-Noisy-Channel
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Project

```bash
python project.py
```



## 📊 Output

## 📊 Results

### Original Image
![Original](results/original.jpg)

### Output Image(includes reconstructed image, error mapping etc) 
![Original](results/output.png)



## 📈 Performance Metrics

* **Bit Error Rate (BER):** Measures the percentage of corrupted bits
* **PSNR:** Indicates the quality of the reconstructed image



## 📚 Applications

* Wireless Communication
* Satellite Image Transmission
* Medical Imaging
* Digital Image Processing



## 🔮 Future Scope

* Implement advanced error correction codes
* Add GUI for real-time parameter control
* Improve denoising techniques using AI/ML



## 👨‍💻 Author
shruti sathe 



## 📄 License

This project is for educational purposes.
