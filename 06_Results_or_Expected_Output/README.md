## 1. Experimental Baselines

To evaluate the detection performance, global model resilience, and operational latency of the proposed detection module, empirical results are benchmarked against two baseline configurations:

1. **Standard Unprotected FL Baseline (FedAvg):** Evaluates a standard Federated Averaging architecture operating without parameter inspection or anomaly filtering under clean (non-attack) conditions.
2. **Unfiltered Adversarial FL Baseline:** Evaluates the impact of active data poisoning (e.g., label flipping) and Byzantine parameter injection attacks on a standard FedAvg aggregator without detection defenses, establishing maximum model accuracy degradation.

---

## 2. Quantitative Evaluation Metrics

| Metric Category | Specific Metric | Unit of Measurement | Analytical Purpose |
| :--- | :--- | :--- | :--- |
| **Detection Efficacy** | Precision, Recall, F1-Score, & False Positive Rate (FPR) | Percentage (%) / Score (0.0–1.0) | Evaluates the capability of the module to accurately identify malicious/poisoned client updates while minimizing false alarms on honest edge nodes. |
| **Global Model Utility** | Global Model Accuracy & Loss Retention | Percentage (%) | Measures global model accuracy retention under active poisoning attacks compared to clean baseline performance. |
| **Operational Overhead** | Inspection Latency & Processing Time | Milliseconds (ms) / Seconds (s) | Tracks the additional computational delay introduced by the inspection process per federated communication round prior to aggregation. |

---

## 3. Proposed Timeline and Project Execution (12-Week DSR Plan)

### Task Allocation Table Across DSR Methodology Phases
| Phase / Timeframe | DSR Methodology Stage | Key Planned Activities & Deliverables |
| :--- | :--- | :--- |
| **Weeks 1 – 2** | **Problem Identification & Objectives** | Finalize research problem statements, define the core research objectives, and consolidate literature review findings on FL data poisoning attacks. |
| **Weeks 3 – 4** | **Design & Architecture Blueprinting** | Model the central aggregator detection architecture, design process flowcharts, select benchmark datasets (MNIST/CIFAR-10/MIMIC-III), and set up the simulation environment. |
| **Weeks 5 – 8** | **Prototype Development & Technical Coding** | Construct Python modules for client simulation, FedAvg aggregation, data poisoning attack injection, and the machine learning anomaly detection script. |
| **Weeks 9 – 10** | **Testing & Experimental Evaluation** | Execute performance benchmarks across simulated federated rounds; measure detection precision, recall, F1-score, inspection latency, and global model accuracy retention. |
| **Weeks 11 – 12** | **Documentation, Formatting & Presentation** | Finalize the comprehensive research proposal report, organize public GitHub technical repository artifacts, and record presentation demonstrations. |

### Project Execution Gantt Chart

```mermaid
gantt
    title Proposed 12-Week Project Execution Plan (DSR Methodology)
    dateFormat  X
    axisFormat W%s

    section Phase 1: Problem ID & Objectives
    Problem Statements & Objectives Formulation :active, p1, 1, 3
    section Phase 2: Design & Blueprinting
    Architecture & Flowchart Design           :p2, 3, 5
    section Phase 3: Development & Coding
    Prototype Development & Attack Scripts    :p3, 5, 9
    section Phase 4: Testing & Evaluation
    Experimental Evaluation & Metric Logging   :p4, 9, 11
    section Phase 5: Documentation & Submission
    Final Report & GitHub Artifacts           :p5, 11, 13
