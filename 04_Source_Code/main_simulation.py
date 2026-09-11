"""
main_simulation.py
Research Title: Detecting Data Poisoning Attacks in Cloud-Based Federated Learning
Group A - Preliminary Source Code
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import time
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# ==========================================
# 1. GLOBAL MODEL DEFINITION
# ==========================================
class SimpleCNN(nn.Module):
    """Basic CNN for MNIST/CIFAR-10 baseline testing."""
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.fc1 = nn.Linear(32 * 26 * 26, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        return x

# ==========================================
# 2. CLIENT NODE LAYER
# ==========================================
def simulate_client_update(model, is_malicious=False):
    """
    Simulates local training at distributed edge clients.
    Honest nodes produce clean parameter updates, whereas compromised nodes execute data poisoning or parameter tampering.
    """
    local_model = SimpleCNN()
    local_model.load_state_dict(model.state_dict())
    
    # Simulate weight updates (dummy data for simulation)
    update_vector = []
    for param in local_model.parameters():
        noise_level = 0.5 if is_malicious else 0.01 # Malicious nodes inject larger discrepancies
        noise = torch.randn(param.size()) * noise_level
        param.data.add_(noise)
        update_vector.extend(param.data.view(-1).tolist())
        
    return local_model.state_dict(), np.array(update_vector)

# ==========================================
# 3. CLOUD INSPECTION LAYER (ML DETECTION)
# ==========================================
class MLDetectionModule:
    """
    Intercepts and inspects updates using statistical feature extraction and an ML classifier.
    """
    def __init__(self):
        # Using Isolation Forest for anomaly detection as referenced in Phase 4 / Ding et al.
        self.classifier = IsolationForest(contamination=0.2, random_state=42)
        self.is_fitted = False

    def extract_features(self, update_vectors):
        """Extracts statistical features like weight distances."""
        # For prototype, we use the L2 norm of the update vectors as a basic statistical feature
        norms = np.linalg.norm(update_vectors, axis=1).reshape(-1, 1)
        return norms

    def inspect_and_filter(self, update_vectors, client_states):
        """Classifies incoming parameters and dynamically quarantines malicious ones."""
        start_time = time.time()
        features = self.extract_features(update_vectors)
        
        if not self.is_fitted:
            self.classifier.fit(features)
            self.is_fitted = True
            
        predictions = self.classifier.predict(features) # 1 for inliers (benign), -1 for outliers (malicious)
        latency = (time.time() - start_time) * 1000 # Inspection latency in milliseconds
        
        accepted_updates = []
        for i, pred in enumerate(predictions):
            if pred == 1:
                accepted_updates.append(client_states[i])
                
        return accepted_updates, predictions, latency

# ==========================================
# 4. AGGREGATION LAYER
# ==========================================
def fed_avg(accepted_updates, global_model):
    """
    Applies standard FedAvg exclusively to accepted/benign parameters.
    """
    if not accepted_updates:
        return global_model.state_dict()
        
    avg_state_dict = global_model.state_dict()
    for key in avg_state_dict.keys():
        avg_state_dict[key] = torch.stack([client[key] for client in accepted_updates], dim=0).mean(dim=0)
    return avg_state_dict

# ==========================================
# 5. MAIN SIMULATION LOOP
# ==========================================
def run_simulation():
    print("--- Starting FL Data Poisoning Detection Simulation ---")
    global_model = SimpleCNN()
    detector = MLDetectionModule()
    
    num_clients = 10
    malicious_ratio = 0.2
    ground_truth = [1 if i >= int(num_clients * malicious_ratio) else -1 for i in range(num_clients)]
    
    # Simulate a single communication round
    client_states = []
    update_vectors = []
    
    for i in range(num_clients):
        is_malicious = (ground_truth[i] == -1)
        state, vector = simulate_client_update(global_model, is_malicious)
        client_states.append(state)
        update_vectors.append(vector)
        
    # Cloud Inspection Layer intercepts updates
    accepted_updates, predictions, latency = detector.inspect_and_filter(update_vectors, client_states)
    
    # Aggregation Layer
    new_global_weights = fed_avg(accepted_updates, global_model)
    global_model.load_state_dict(new_global_weights)
    
    # Calculate Evaluation Metrics
    precision = precision_score(ground_truth, predictions, pos_label=-1, zero_division=0) * 100
    recall = recall_score(ground_truth, predictions, pos_label=-1, zero_division=0) * 100
    f1 = f1_score(ground_truth, predictions, pos_label=-1, zero_division=0) * 100
    
    print(f"Inspection Latency: {latency:.2f} milliseconds")
    print(f"Detection Precision: {precision:.2f}%")
    print(f"Detection Recall: {recall:.2f}%")
    print(f"Detection F1-Score: {f1:.2f}%")
    print(f"Number of models aggregated: {len(accepted_updates)} / {num_clients}")

if __name__ == "__main__":
    run_simulation()