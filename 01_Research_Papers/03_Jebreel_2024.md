# Jebreel et al. (2024)

## Paper Title

LFighter: Defending against the Label-Flipping Attack in Federated Learning

## Authors

Jebreel et al.

## Year

2024

## Research Problem

The study focuses on detecting and defending against label-flipping attacks in Federated Learning.

## Method / Technique

LFighter analyses gradients associated with source and target class neurons and uses clustering to distinguish malicious clients from benign clients.

## Dataset / Tools

- MNIST
- CIFAR-10
- IMDB
- IID data
- Non-IID data
- Python
- PyTorch / TensorFlow
- Jupyter

## Main Findings

The proposed method was evaluated under both IID and non-IID settings and was designed to identify clients performing label-flipping attacks.

## Limitation

The method is specifically designed for label-flipping attacks. Therefore, its effectiveness against other types of data poisoning attacks may require further investigation.

## Relevance to Proposed Research

The study demonstrates that gradient information can be used as a feature for identifying malicious clients. This provides a possible feature-analysis approach for the proposed detection module.

## Source

Jebreel et al. (2024). *LFighter: Defending against the Label-Flipping Attack in Federated Learning*. Neural Networks, 170, 111–126.

DOI: 10.1016/j.neunet.2023.11.019
