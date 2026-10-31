# Literature Review: Tabular Foundation Models for Anomaly Detection

This literature review provides an overview of recent advances in tabular foundation models (TabFMs) for anomaly detection, with particular emphasis on novelty detection. It summarizes task-specific TabFMs, strategies for adapting general-purpose models, commonly used benchmarks, and cross-paper comparisons.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Methods](#2-methods)
   - [2.1 Pretrained Methods](#21-pretrained-methods)
   - [2.2 Adaptations of TabFMs](#22-adaptations-of-tabfms)
3. [Datasets](#3-datasets)
4. [Reported Benchmarks](#4-reported-benchmarks)

---

## 1. Introduction

Foundation models (FMs) are pretrained on diverse datasets or tasks to acquire capabilities that can transfer to downstream applications. Some FMs can use task-specific examples as context to predict new instances without updating their parameters. This approach has shown promising results for tabular data through the development of tabular foundation models (TabFMs). More recently, TabFMs have been applied to anomaly detection, both through models pretrained specifically for this task and through adaptations of general-purpose TabFMs.

Methods differ in their inference-time requirements, particularly in the composition of the reference (context) data and the availability of labels. The context supervision regimes considered here are defined as follows:

- **One-Class (Novelty Detection) (OC):** The context contains only samples known or assumed to be normal, with no anomalies included. The objective is to detect query samples that deviate from the normal patterns represented by this context. This regime, commonly associated with novelty detection, is the primary focus of this review.
- **Unsupervised (UN):** The context is unlabeled and may contain both normal and anomalous samples; this is also referred to as a potentially contaminated setting.
- **Semi-Supervised (SS):** The context contains unlabeled samples and a limited number of labeled anomalies. Since the remaining unlabeled samples are not guaranteed to be normal, the context may be contaminated.
- **Fully Supervised (FS):** The context contains ground-truth labels for normal and anomalous samples. Anomaly detection can then be formulated as supervised classification, although class imbalance and generalization to unseen anomaly types may remain challenging.

---

## 2. Methods

This section summarizes recent TabFM-based approaches to anomaly detection. It distinguishes models pretrained specifically for anomaly detection from strategies that adapt general-purpose models. The tables classify methods by the supervision regimes supported by their inference-time contexts.

### 2.1 Pretrained Methods

Pretrained methods include foundation models developed specifically for tabular anomaly or outlier detection, typically enabling inference on new datasets without dataset-specific parameter updates.

| Year | Title                                                                                       | Method    | Supervision Regimes | Paper                                     | Code                                                                                      |
| :--: | :------------------------------------------------------------------------------------------ | :-------- | :------------------ | :---------------------------------------- | :---------------------------------------------------------------------------------------- |
| 2025 | FoMo-0D: A Foundation Model for Zero-shot Tabular Outlier Detection                         | FoMo-0D   | **OC**              | [ArXiv](https://arxiv.org/abs/2409.05672) | [GitHub](https://github.com/A-Chicharito-S/FoMo-0D)                                       |
| 2026 | From Zero to Hero: Advancing Zero-Shot Foundation Models for Tabular Outlier Detection      | OutFormer | **OC**              | [ArXiv](https://arxiv.org/abs/2602.03018) | [GitHub](https://github.com/psorus/Outformer)                                             |
| 2026 | TACTIC for Navigating the Unknown: Tabular Anomaly deteCTion via In-Context inference       | TACTIC-C  | **OC**              | [ArXiv](https://arxiv.org/abs/2603.14171) | [GitHub](https://github.com/gmum/TACTIC)                                                  |
| 2026 | TACTIC for Navigating the Unknown: Tabular Anomaly deteCTion via In-Context inference       | TACTIC-N  | **OC**, UN          | [ArXiv](https://arxiv.org/abs/2603.14171) | [GitHub](https://github.com/gmum/TACTIC)                                                  |
| 2026 | ICLAD: In-Context Learning for Unified Tabular Anomaly Detection Across Supervision Regimes | ICLAD     | **OC**, UN, SS      | [ArXiv](https://arxiv.org/abs/2603.19497) | [Hugging Face](https://huggingface.co/jyiwei/iclad) (checkpoints; full code not verified) |

### 2.2 Adaptations of TabFMs

These approaches repurpose general-purpose TabFMs, including TabPFN and other prior-data fitted networks, for anomaly and novelty detection, rather than pretraining a new anomaly-specific foundation model.

| Year | Title                                                                                                 | Name of Method                            | Supervision Regimes | Paper                                                        | Code                                                                          |
| :--: | :---------------------------------------------------------------------------------------------------- | :---------------------------------------- | :------------------ | :----------------------------------------------------------- | :---------------------------------------------------------------------------- |
| 2025 | Accurate predictions on small data with a tabular foundation model (TabPFN backbone)                  | uTabPFN (official unsupervised extension) | **OC**, UN          | [Nature](https://www.nature.com/articles/s41586-024-08328-6) | [GitHub](https://github.com/PriorLabs/tabpfn-extensions)                      |
| 2026 | Adapting prior-data fitted networks for tabular anomaly detection                                     | ZEN                                       | **OC**, UN          | [ArXiv](https://arxiv.org/abs/2610.06693)                    | [GitHub](https://github.com/Maximilianb1/zen-focus-tabular-anomaly-detection) |
| 2026 | Adapting prior-data fitted networks for tabular anomaly detection                                     | FOCUS                                     | **OC**, UN          | [ArXiv](https://arxiv.org/abs/2610.06693)                    | [GitHub](https://github.com/Maximilianb1/zen-focus-tabular-anomaly-detection) |
| 2026 | TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks | TASKBRIDGE                                | **OC**              | [ArXiv](https://arxiv.org/abs/2609.36968)                    | —                                                                             |

---

## 3. Datasets

This section summarizes the main benchmark suites used to evaluate tabular novelty and anomaly detection methods and their scale. Ground-truth anomaly labels support evaluation and, where accessible, the simulation of different supervision regimes by selecting clean training subsets, withholding labels, or revealing selected anomaly labels. Simply withholding labels does not make a contaminated dataset suitable for one-class evaluation, and some benchmark partitions reserve test labels for private evaluation.

| Title                                                                            | Benchmark | # Datasets | Paper                                     | Link                                                 |
| :------------------------------------------------------------------------------- | :-------- | :--------: | :---------------------------------------- | :--------------------------------------------------- |
| ADBench: Anomaly Detection Benchmark                                             | ADBench   |     57     | [ArXiv](https://arxiv.org/abs/2206.09426) | [GitHub](https://github.com/Minqi824/ADBench)        |
| MacrOData: New Benchmarks of Thousands of Datasets for Tabular Outlier Detection | OddBench  |    790     | [ArXiv](https://arxiv.org/abs/2602.09329) | [Hugging Face](https://huggingface.co/MacrOData-CMU) |
| MacrOData: New Benchmarks of Thousands of Datasets for Tabular Outlier Detection | OvRBench  |    856     | [ArXiv](https://arxiv.org/abs/2602.09329) | [Hugging Face](https://huggingface.co/MacrOData-CMU) |
| MacrOData: New Benchmarks of Thousands of Datasets for Tabular Outlier Detection | SynBench  |    800     | [ArXiv](https://arxiv.org/abs/2602.09329) | [Hugging Face](https://huggingface.co/MacrOData-CMU) |

---

## 4. Reported Benchmarks

This section summarizes the evaluation benchmarks used in each study and identifies which other methods listed in this review were included as experimental baselines. Dataset counts may differ across studies because authors evaluate different benchmark subsets or versions.

| Paper                                                                                                 | Method        | Benchmarks Used                                              | Compared Methods from List                                         |
| :---------------------------------------------------------------------------------------------------- | :------------ | :----------------------------------------------------------- | :----------------------------------------------------------------- |
| FoMo-0D: A Foundation Model for Zero-shot Tabular Outlier Detection                                   | FoMo-0D       | ADBench (57)                                                 | _None (earliest dedicated model listed)_                           |
| From Zero to Hero: Advancing Zero-Shot Foundation Models for Tabular Outlier Detection                | OutFormer     | ADBench (57), OddBench (690), OvRBench (756), SynBench (800) | FoMo-0D                                                            |
| TACTIC for Navigating the Unknown: Tabular Anomaly deteCTion via In-Context inference                 | TACTIC        | ADBench (38); synthetic anomaly experiments                  | uTabPFN (TabPFN2.5 extension)                                      |
| Adapting prior-data fitted networks for tabular anomaly detection                                     | ZEN and FOCUS | ADBench (47)                                                 | uTabPFN (official extension)                                       |
| TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks | TASKBRIDGE    | OddBench (790)                                               | FoMo-0D, OutFormer, TACTIC-C, TACTIC-N, uTabPFN (TabPFN extension) |
| ICLAD: In-Context Learning for Unified Tabular Anomaly Detection Across Supervision Regimes           | ICLAD         | ADBench (57)                                                 | FoMo-0D                                                            |
