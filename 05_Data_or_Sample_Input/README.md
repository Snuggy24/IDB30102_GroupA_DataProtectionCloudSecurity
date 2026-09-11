## Overview
This directory serves as the technical repository for dataset specifications, sample input payload structures, pre-processing pipelines, and legal compliance frameworks used to evaluate the proposed module within a cloud-based Federated Learning (FL) environment.

---

## 1. Benchmark Datasets Specifications

### A. MNIST Image Classification Benchmark
* **Description:** A standard vision benchmark containing 70,000 grayscale images ($28 \times 28$ pixels) across 10 digit classes (0–9).
* **Role in Research:** Used to simulate decentralized edge-node client training and evaluate model detection precision under label-flipping and noisy weight injection attacks.
* **Data Allocation:** 60,000 training samples distributed across simulated FL client nodes; 10,000 testing samples reserved for global model validation.

### B. CIFAR-10 Benchmark
* **Description:** Comprises 60,000 $32 \times 32$ color images across 10 object classes (50,000 training, 10,000 testing).
* **Role in Research:** Provides a multi-channel dataset to test detection resilience against targeted feature perturbation and backdoor poisoning attacks.

### C. MIMIC-III Clinical Database
* **Description:** A large, freely accessible clinical database comprising de-identified health-related data associated with ICU patients.
* **Role in Research:** Used to simulate real-world, privacy-preserving healthcare consortia where medical centers collaboratively train predictive models without exposing raw patient records.

---

## 2. Sample Input Payload Structure

During local client training rounds, edge nodes send model parameter updates to the central aggregator. The anomaly detection module inspects incoming payloads structured as follows:

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `client_id` | String | Unique identifier for the participating edge node (e.g., `Node_01`). |
| `round_number` | Integer | Active global federated learning communication round. |
| `weight_vector` | Array / Float32 | Compressed layer weights derived from local SGD training. |
| `gradient_distribution` | Matrix / Float32 | Parameter gradients submitted for global aggregation. |
| `sample_count` | Integer | Total local training samples used by the edge node in the current round. |
| `is_poisoned` | Boolean (0/1) | Ground-truth label used during sandbox evaluation (0 = Clean, 1 = Poisoned). |

---

## 3. Data Pre-Processing & Attack Simulation Pipeline

1. **Non-IID Data Partitioning:** Non-IID (non-independent and identically distributed) data splits are generated using a Dirichlet distribution ($\alpha = 0.5$) across simulated client nodes.
2. **Adversarial Attack Injections:**
   * **Label Flipping Attack:** Inverting target classification labels (e.g., swapping label `1` to `7`) on 20%–40% of local client training samples.
   * **Byzantine Parameter Injection:** Adding Gaussian noise or scaling weight updates to disrupt global model convergence.
3. **Normalization:** Applying L2-norm vector scaling to prepare weight distributions for distance-based statistical checks (Cosine Similarity, Mahalanobis Distance).

---

## 4. Ethical, Legal, and Privacy Compliance

* **PDPA Compliance:** Strictly observes Malaysia’s Personal Data Protection Act 2010 (PDPA) by excluding all un-anonymized Personally Identifiable Information (PII) or proprietary records.
* **GDPR Compliance:** All health-related datasets consist exclusively of open-access, fully de-identified academic research benchmarks (MIMIC-III).
* **Sandbox Security:** All data poisoning simulations and adversarial update tests are executed within an isolated local sandbox environment, ensuring zero risk or disruption to live operational cloud networks.
