# Research Project Overview

# Research Title
Detecting Data Poisoning Attacks in Cloud-Based Federated Learning Using a Machine Learning-Based Detection Module

# Group Number
Group A 

#Group Members and Student IDs
1. Member 1: Harith Hakimi Bin Mohd Fadzil – 52215124454
2. Member 2: Nurezzatul Darwena Binti Mohd Jazrin – 52215226101
3. Member 3: Jayquena Jane Anak Stephen – 52215226057
4. Member 4: Madan Easwar Ganesan – 52215124402 

## Assigned Research Area
Cloud Security (Specifically: Federated Learning & Machine Learning Security)

## Research Problem
Current privacy mechanisms in cloud Federated Learning (FL), such as Differential Privacy or Homomorphic Encryption, introduce excessive computational overhead or reduce model accuracy. Furthermore, central cloud aggregators cannot inspect raw local data, making the architecture highly vulnerable to data poisoning and Byzantine parameter tampering attacks from compromised edge nodes. There is a lack of intelligent, lightweight modules to inspect and verify incoming model updates before they are aggregated into the global model.

## Research Aim
The main aim for this research is to design and develop a machine learning-based detection module capable of identifying data poisoning within a cloud-based Federated Learning Environment to protect global model integrity.

## THREE (3) Research Objectives
1. To analyze and model the behavioral and statistical weight discrepancies of client model updates under data poisoning within the simulated cloud-based Federated Learning environment.
2. To design and develop a machine learning-based anomaly detection module to inspect incoming client parameters and updates before global aggregation.
3. To evaluate the detection performance, operational latency, and global model accuracy retention of the proposed module against baseline federated learning architectures.

## Brief Description of the Proposed Solution
The proposed solution is a centralized, machine learning-based anomaly detection module positioned at the cloud aggregator layer. Before applying the Federated Averaging (FedAvg) algorithm, this module intercepts incoming client model updates, extracts statistical features (like weight distances and layer gradient distributions), and uses ML classification to dynamically quarantine malicious parameters, thereby preserving the integrity of the global model.

## Selected Research Methodology and Development Model
*  Methodology/Development Model: Quantitative experimental research design utilizing the *Cross-Industry Standard Process for Data Mining (CRISP-DM)* development model.

## Proposed Evaluation Plan
*  Baseline for Comparison: Standard Unprotected FL Baseline (FedAvg under clean conditions) and Unfiltered Adversarial FL Baseline (FedAvg under active poisoning attacks without detection).
*  Dataset / Test Environment: MNIST and CIFAR-10 benchmark datasets, simulated using Python 3.11 with PyTorch/TensorFlow.
*  Evaluation Metrics: Precision, Recall, F1-Score, False Positive Rate (FPR), Global Model Accuracy/Loss Retention, and Inspection Latency (milliseconds).

## Proposed System Architecture
The architecture consists of three structural layers:
1.  Client Node Layer: Distributed edge clients training local models (includes both benign and compromised nodes).
2.  Cloud Inspection Layer (ML Detection Module): Intercepts and inspects updates using statistical feature extraction and an ML classifier.
3.  Aggregation Layer: Applies standard FedAvg exclusively to accepted/benign parameters.

## Description of the Technical Components Included in the Repository
*   `01_Research_Papers/`: Source materials and literature supporting the study.
*   `02_Literature_Review/`: Literature analysis matrix, research gap identification, and comparison of existing techniques.
*   `03_Architecture_and_Flowchart/`: Proposed system architecture diagram and process flowcharts.
*   `04_Source_Code/`: Preliminary Python scripts for the FL environment, FedAvg aggregation, and the ML anomaly detection algorithm.
*   `05_Data_or_Sample_Input/`: Dataset loading scripts and sample vector logs for MNIST/CIFAR-10.
*   `06_Results_or_Expected_Output/`: Evaluation metrics framework, expected classification outputs, and latency tracking.
*   `07_References/`: Full APA citations for external resources, frameworks, and datasets.

## Programming Languages, Software, Frameworks, Libraries, Datasets, and Tools Expected to be Used
*  Programming Language: Python 3.11
*  Frameworks & Libraries: PyTorch, TensorFlow, PySyft, Flower (FL framework), Scikit-Learn, NumPy
*  Datasets: MNIST, CIFAR-10, MIMIC-III (simulated time-series records)

## Instructions for Executing Preliminary Code
1. Ensure Python 3.11+ is installed on your local environment.
2. Clone this repository: `git clone [repository_url]`
3. Navigate to the Source Code directory: `cd 04_Source_Code`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Run the preliminary simulation: `python main_simulation.py`
