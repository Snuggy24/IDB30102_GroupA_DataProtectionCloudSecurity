# Detection Methods Summary

| Paper | Detection Method | Main Feature / Information | Attack Focus |
|---|---|---|---|
| Qayyum et al. (2022) | Data-model association and cosine similarity | Client model parameters | Poisoned updates |
| Lai et al. (2023) | Relative weight differences and accuracy testing | Model weights | Label flipping and backdoor |
| Jebreel et al. (2024) | Gradient analysis and clustering | Class-related gradients | Label flipping |
| Ding et al. (2024) | Improved Isolation Forest | Singular-value features and update trajectory | Poisoning behaviour |
| Basak & Chatterjee (2025) | Audit mechanism | Client updates | Data poisoning |
| Chen et al. (2025) | K-means clustering | Conditional entropy and mutual information | Data poisoning |
| Ma et al. (2025) | Gradient analysis and clustering | Output-layer gradients | Multi-label poisoning |
| Zhu et al. (2026) | GMM and statistical process control | Client update behaviour | Poisoning attacks |

## Observation

The reviewed studies show that client updates, gradients, statistical information and model behaviour can be used as signals for identifying malicious clients.

These approaches provide the technical basis for investigating a machine-learning-based detection module for cloud-based Federated Learning.
