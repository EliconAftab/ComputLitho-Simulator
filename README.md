# ComputLitho-Simulator
ComputLitho is a Python + Flask-based web application that allows users to simulate and analyze aerial image formation from GDSII files — a key step in photolithography. The tool enables the calculation of fragmentation and aerial intensity maps based on parameters such as wavelength, numerical aperture, and resist settings.
# Features
GDSII File Upload: Parse and process input GDSII layout files.

🔬 Aerial Image Simulation: Simulate image intensity distribution based on exposure system parameters.

⚙️ Custom Input Parameters: Choose wavelength (λ), numerical aperture (NA), layer, and datatype.

🧩 Fragmentation Engine: Break complex mask geometries into smaller regions for precise optical simulation.

📊 Intensity Visualization: Generate and export aerial image plots with simulated intensity distributions.

🖥️ Web Interface: User-friendly Flask UI to run simulations and view results interactively.


# WHAT IS COMPUTATIONAL LITHOHGRAPHY
Lithography is the process of transferring patterns of geometric shapes in a mask to a thin layer of radiation-sensitive material (called resist) covering the surface of a semiconductor wafer.

# GUI (Graphical User Interface) for ComputLitho
<img width="2092" height="1158" alt="image" src="https://github.com/user-attachments/assets/f127c706-e03a-4200-88fe-be67aa6fd27b" />
# Web App Architecture
<img width="2635" height="1262" alt="image" src="https://github.com/user-attachments/assets/2450b3a7-adb6-4c92-b3b3-4242cd990cf7" />
# File Handling
Each layer of a GDS File represents a specific fabrication step or material in semiconductor manufacturing.
Each layer has its own datatype.
In a GDS file, the datatype is an additional identifier assigned to a shape within a layer, used to further classify shapes that belong to the same layer.
<img width="2680" height="1320" alt="image" src="https://github.com/user-attachments/assets/481c0530-89cd-48e5-ba2a-c2481599f32d" />
<img width="2671" height="1312" alt="image" src="https://github.com/user-attachments/assets/e10bf27c-be9e-45a3-8cc9-d93f19762f80" />

# Results
<img width="2620" height="1290" alt="image" src="https://github.com/user-attachments/assets/bb96fca6-63b1-4f52-b159-3f8a6776901a" />
