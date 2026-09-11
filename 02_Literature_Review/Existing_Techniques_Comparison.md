# Existing Techniques Comparison

This section compares the main detection and defense approaches identified from the literature reviewed in Chapter 2.

## Comparison of Existing Approaches

| Approach | Example Studies | Main Technique | Strength | Limitation |
|---|---|---|---|---|
| Similarity-based detection | Qayyum et al. (2022) | Data-model association and cosine similarity | Provides a relatively direct way to compare client updates | Performance may depend on the characteristics of the attack |
| Weight-based analysis | Lai et al. (2023) | Relative weight differences and accuracy testing | Can screen suspicious client updates before aggregation | Mainly evaluated against specific poisoning attacks |
| Gradient-based clustering | Jebreel et al. (2024); Ma et al. (2025) | Gradient analysis and clustering | Provides detailed information about differences between client updates | Can be designed for specific attack types |
| Machine-learning anomaly detection | Ding et al. (2024); Chen et al. (2025) | Isolation Forest, information-based features and clustering | Can identify abnormal client behaviour from update characteristics | Feature extraction and processing may introduce additional computational requirements |
| Statistical monitoring | Zhu et al. (2026) | Gaussian Mixture Model and Statistical Process Control | Supports monitoring of client behaviour across Federated Learning rounds | Depends on statistical modelling and monitoring assumptions |
| Audit-based verification | Basak & Chatterjee (2025) | Client-update auditing before aggregation | Allows suspicious updates to be checked before affecting the global model | The auditing process may introduce additional processing overhead |

## Comparison and Synthesis

The reviewed studies demonstrate several ways of detecting malicious or poisoned client behaviour in Federated Learning.

Similarity-based and weight-based approaches analyse differences between client model updates. These approaches can provide relatively direct methods for identifying suspicious updates, but their effectiveness may depend on the characteristics of the poisoning attack.

Gradient-based approaches provide more detailed information about client behaviour by analysing gradient changes. However, studies such as LFighter and the multi-label poisoning defense focus on particular poisoning scenarios, which may limit their general applicability.

Machine-learning-based anomaly detection approaches provide a more flexible direction because abnormal client behaviour can be identified from selected features. Ding et al. (2024) used an improved Isolation Forest, while Chen et al. (2025) used information-based features with K-means clustering. These studies demonstrate the potential of machine learning for identifying abnormal client updates.

Statistical monitoring provides another approach for identifying suspicious clients across multiple Federated Learning rounds. However, statistical assumptions and monitoring requirements may affect its practical implementation.

Audit-based approaches provide an additional layer of protection by checking client updates before aggregation. However, additional auditing can introduce processing overhead.

## Implication for Proposed Research

Based on the comparison, a machine-learning-based detection approach is suitable for further investigation because it can analyse client-update characteristics and identify abnormal behaviour before aggregation.

The proposed research therefore focuses on developing a machine-learning-based detection module for identifying data poisoning attacks in cloud-based Federated Learning.

The module will focus on analysing client updates without requiring direct access to private client data. Its performance will be evaluated using detection metrics such as accuracy, precision, recall, F1-score and false positive rate, together with processing latency and the effect on global model performance.
