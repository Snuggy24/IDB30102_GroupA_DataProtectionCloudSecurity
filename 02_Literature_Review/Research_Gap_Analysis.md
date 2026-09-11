# Research Gap Analysis

## Identified Research Gaps

The reviewed studies show several limitations in existing poisoning detection approaches.

### 1. Attack-Specific Detection

Several existing methods are designed for particular attack types, such as label-flipping, multi-label poisoning or specific malicious update behaviours. This may limit their applicability to different poisoning scenarios.

### 2. Non-IID Client Data

In Federated Learning, clients may naturally have different data distributions. Therefore, benign client updates can appear different from each other, making it difficult to distinguish normal behaviour from malicious behaviour.

### 3. Detection Accuracy and Processing Efficiency

Existing detection methods may provide good detection performance but introduce additional feature extraction, clustering, statistical analysis or auditing processes. A practical detection module needs to balance detection performance with processing efficiency.

### 4. Cloud-Based Federated Learning

The reviewed studies provide limited focus on a practical detection module operating within a cloud-based Federated Learning environment where client updates need to be analysed before aggregation.

## Proposed Research Direction

Based on these gaps, this research proposes a machine-learning-based detection module that analyses client updates to identify potentially poisoned or anomalous client behaviour before aggregation.

The proposed system will evaluate detection accuracy, precision, recall, F1-score, false positive rate, processing latency and the impact on global model performance.
