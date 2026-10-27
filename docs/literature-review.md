# Literature Review: Tabular Foundation Models for Anomaly Detection

This literature review provides a comprehensive overview of recent advancements in Tabular Foundation Models (TABFMs) applied to anomaly detection. It synthesizes state-of-the-art pretrained methodologies, general-purpose model adaptation strategies, standardized evaluation benchmark suites, and cross-paper comparative analyses.

## Table of Contents

1. [Methods](#1-methods)
   - [1.1 Pretrained Methods](#11-pretrained-methods)
   - [1.2 Adaptations of TabFMs](#12-adaptations-of-tabfms)
2. [Datasets](#2-datasets)
3. [Reported Benchmarks](#3-reported-benchmarks)

---

## 1. Methods

### 1.1 Pretrained Methods

Pretrained methods comprise dedicated foundation models built specifically for tabular outlier and anomaly detection in a zero-shot manner.

| Year | Title                                                                                       | Method    | Paper                                     | Code                                                |
| :--: | :------------------------------------------------------------------------------------------ | :-------- | :---------------------------------------- | :-------------------------------------------------- |
| 2025 | FoMo-0D: A Foundation Model for Zero-shot Tabular Outlier Detection                         | FoMo-0D   | [ArXiv](https://arxiv.org/abs/2409.05672) | [GitHub](https://github.com/A-Chicharito-S/FoMo-0D) |
| 2025 | From zero to hero: Advancing zero-shot foundation models for tabular outlier detection      | OutFormer | [ArXiv](https://arxiv.org/abs/2602.03018) | [GitHub](https://github.com/psorus/Outformer)       |
| 2026 | TACTIC for Navigating the Unknown: Tabular Anomaly deteCTion via In-Context inference       | TACTIC    | [ArXiv](https://arxiv.org/abs/2603.14171) | [GitHub](https://github.com/gmum/TACTIC)            |
| 2026 | ICLAD: In-context learning for unified tabular anomaly detection across supervision regimes | ICLAD     | [ArXiv](https://arxiv.org/abs/2603.19497) | -                                                   |

### 1.2 Adaptations of TabFMs

Adaptations take general-purpose tabular foundation models (such as TabPFN or prior-data fitted networks) and adapt or utilize them for anomaly and novelty detection tasks.

| Year | Title                                                                                                 | Name of Method | Paper                                     | Code                                                                          |
| :--: | :---------------------------------------------------------------------------------------------------- | :------------- | :---------------------------------------- | :---------------------------------------------------------------------------- |
| 2026 | Adapting prior-data fitted networks for tabular anomaly detection                                     | ZEN and FOCUS  | [ArXiv](https://arxiv.org/abs/2610.06693) | [GitHub](https://github.com/Maximilianb1/zen-focus-tabular-anomaly-detection) |
| 2026 | TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks | TASKBRIDGE     | [ArXiv](https://arxiv.org/abs/2609.36968) | -                                                                             |

---

## 2. Datasets

Primary benchmark suites utilized across for evaluating tabular novelty and anomaly detection models, summarizing their scale and supported supervision regimes among:

- **One-Class (Novelty):** 100% clean normal data, no anomalous instances.
- **Unsupervised:** Unlabeled, potentially contaminated data containing mixed normal and unknown anomalous instances.
- **Semi-Supervised:** Combines unlabeled data with a small fraction of verified anomaly labels.
- **Fully Supervised:** Ground-truth labels for both normal and anomalous classes.

| Title                                                                            | Benchmark | # Datasets | Supervision regimes                                        | Paper                                     | Link                                                |
| -------------------------------------------------------------------------------- | --------- | ---------- | ---------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------- |
| ADBench: Anomaly Detection Benchmark                                             | ADBench   | 57         | Unsupervised, Semi-supervised, Fully-supervised, One-Class | [ArXiv](https://arxiv.org/abs/2206.09426) | [GitHub](https://github.com/Minqi824/ADBench)       |
| MACRODATA: New Benchmarks of Thousands of Datasets for Tabular Outlier Detection | ODDbench  | 790        | One-Class, Unsupervised                                    | [ArXiv](https://arxiv.org/abs/2602.09329) | [HuggingFace](https://huggingface.co/MacrOData-CMU) |

---

## 3. Reported Benchmarks

Comparative summary of cross-paper benchmarking, mapping each reviewed study to the specific benchmark suites it utilized and the baseline models included in its evaluations.

| Paper                                                                                                 | Method        | Benchmarks Used   | Compared Methods from List |
| :---------------------------------------------------------------------------------------------------- | :------------ | :---------------- | :------------------------- |
| FoMo-0D: A Foundation Model for Zero-shot Tabular Outlier Detection                                   | FoMo-0D       | ADBench           | _None_ (Pioneer model)     |
| From zero to hero: Advancing zero-shot foundation models for tabular outlier detection                | OutFormer     | ADBench, ODDbench | FoMo-0D                    |
| TACTIC for Navigating the Unknown: Tabular Anomaly deteCTion via In-Context inference                 | TACTIC        | ADBench, ODDbench | FoMo-0D, OutFormer         |
| Adapting prior-data fitted networks for tabular anomaly detection                                     | ZEN and FOCUS | ADBench           | TACTIC, FoMo-0D, OutFormer |
| TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks | TASKBRIDGE    | ODDbench          | TACTIC, FoMo-0D, OutFormer |
| ICLAD: In-context learning for unified tabular anomaly detection across supervision regimes           | ICLAD         | ADBench           | _None_                     |
