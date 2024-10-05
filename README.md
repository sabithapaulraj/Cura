# Overview - Leveraging state-of-the-art AI models using Intel's OpenVINO™ and oneAPI toolkits to develop a custom transfer learning model to diagnose severity of Knee Osteoarthritis, followed by improvising available health-tech
## The Idea
![WhatsApp Image 2024-10-05 at 10 28 53_914ff959](https://github.com/user-attachments/assets/dca45394-054f-4621-ba14-9b2d4c4847b6)

### This project aims to revolutionize the diagnosis and management of knee osteoarthritis by leveraging state-of-the-art AI models and Intel's OpenVINO™ and oneAPI toolkits. The solution uses deep learning to accurately detect osteoarthritis from knee X-rays and provides personalized recommendations to enhance patient care. The system integrates three core features, each powered by AI technologies optimized using Intel’s OpenVINO toolkit:
![WhatsApp Image 2024-10-05 at 10 29 31_5e5169a5](https://github.com/user-attachments/assets/85d22461-720d-4320-beaf-e78128cd658d)
# Tech Stack
![WhatsApp Image 2024-10-05 at 10 30 26_bc6459f8](https://github.com/user-attachments/assets/0dfda760-00df-4b0b-8c0d-a31ba07407ad)

# Main Components
## Retrieval Augmented Generation based LLM Chatbot for Medical Consultation (Qwen 2.5 0.5B Instruct, Qwen 2.5 14B Instruct & OpenVINO)
## Structure Extraction using NuExtract & OpenVINO
## ResNet-based Image Classification with PyTorch Optimization & OpenVINO
# Features
## 1. LLM Chatbot for Medical Consultation
The system includes a Large Language Model (LLM)-powered chatbot built on Qwen 2.5 0.5B Instruct, fine-tuned for medical conversations, including knee osteoarthritis diagnosis and care. Leveraging OpenVINO, the chatbot provides accurate, real-time, and dynamic patient consultation.

Input: Natural language questions regarding knee osteoarthritis.
Output: AI-generated explanations of the condition, prevention tips, and personalized care strategies.
### Technologies:

#### Qwen 2.5 0.5B Instruct (fine-tuned for healthcare)
#### OpenVINO Toolkit for inference optimization
## 2. Structure Extraction using NuExtract & OpenVINO
A core part of the project involves NuExtract, a deep learning model that can extract relevant structural information from medical reports, knee X-rays, and radiology notes. This model processes unstructured data, identifies key medical terms, and extracts structured insights relevant to osteoarthritis diagnosis and treatment.

Input: Unstructured medical reports and X-ray annotations.
Output: Key medical insights like cartilage status, bone spurs, and joint space narrowing.
### Technologies:

#### NuExtract model for structured data extraction.
#### OpenVINO for optimized data extraction and inference.
## 3. ResNet-based Image Classification with PyTorch Optimization
The system employs a ResNet-based image classifier for detecting and classifying the severity of osteoarthritis from X-ray images. The model is optimized using Intel's OpenVINO to enable faster, more efficient inference on local devices or edge environments.

Input: Knee X-ray images.
Output: Osteoarthritis detection and severity classification (e.g., mild, moderate, severe).
### Technologies:

#### ResNet architecture for classification.
#### PyTorch for model training.
### OpenVINO for deployment and inference optimization.

# Key Components and Dependencies
## Intel Toolkits
This project heavily utilizes Intel's suite of toolkits for AI and deep learning optimization:


### Intel® Distribution of OpenVINO™ Toolkit: Speeds up inference and enables deployment on various hardware architectures (CPU, GPU, VPU, etc.).
### Intel® oneAPI Base Toolkit: Facilitates the development of data-centric and HPC applications, supporting efficient model training.

# Other Files
## https://github.com/sabithapaulraj/Knee_OA_Prediction
## https://github.com/sabithapaulraj/Cura_Structure_Extraction

## Front End
![image](https://github.com/user-attachments/assets/87d99e76-9e3b-404c-a898-d3ae7101722e)
![image](https://github.com/user-attachments/assets/d7beb37a-39e7-4a35-b756-3a48fe732c88)
![WhatsApp Image 2024-10-05 at 10 31 06_d689d41e](https://github.com/user-attachments/assets/cbff450d-3f09-411a-bf7d-41380a078205)

![image](https://github.com/user-attachments/assets/7aabb563-cafe-40c6-8091-936b917e809d)
![image](https://github.com/user-attachments/assets/4e5a1396-774d-4a4c-9d41-852d36eabd1f)



