# Chen, Feng & Wang (2025)

## Paper Title

AIDFL: An Information-Driven Anomaly Detector for Data Poisoning in Decentralized Federated Learning

## Authors

Chen, Feng & Wang

## Year

2025

## Research Problem

The study investigates how data poisoning attacks can be detected in Federated Learning when client data are non-IID.

## Method / Technique

AIDFL uses information-based features including conditional entropy and mutual information, followed by K-means clustering to identify anomalous client behaviour.

## Dataset / Tools

- MNIST
- FashionMNIST
- CIFAR-10
- Non-IID data
- Conditional entropy
- Mutual information
- K-means clustering

## Main Findings

The method demonstrates that information-based features can be used to distinguish suspicious client behaviour in non-IID Federated Learning environments.

## Limitation

The approach introduces feature calculation and clustering processes that may affect computational efficiency. Further testing is required for practical cloud-based deployment.

## Relevance to Proposed Research

This study is particularly relevant because non-IID client data can make benign client updates naturally different from each other. It provides an example of using machine-learning-based clustering to detect anomalous behaviour.

## Source

Chen, Feng & Wang (2025). *AIDFL: An Information-Driven Anomaly Detector for Data Poisoning in Decentralized Federated Learning*. IEEE Access, 13, 50017–50031.

DOI: 10.1109/ACCESS.2025.3552168
