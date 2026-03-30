# 🧬 NGS Mini-Pipeline Training (Binder)

This repository contains an interactive training resource designed to introduce the basic concepts of NGS bioinformatics pipelines using real tools and simplified data.

The notebooks are intended for trainees with little or no computational background and provide a hands-on approach to understanding how sequencing data is processed.

[![Launch in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Manuel-DominguezCBG/ngs-teaching-binder/main)

---

## 🗺️ Notebooks

| Notebook | Topic |
|---|---|
| 0 — Introduction and basic Linux commands | The environment, terminal basics, Linux commands |
| 1 — Where does the data come from? | Sequencing concepts, FASTQ files, FastQC |
| 2 — It is time to map | BWA alignment, SAM/BAM, samtools, IGV visualisation |
| 3 — Looking for variants | Variant calling with bcftools |
| 4 — What is a VCF file? | VCF format in depth, filtering, clinical context |

---

## 🚀 Launch in Binder

Click the badge above or the link below to launch the full environment in your browser — no installation required:

[![Launch in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Manuel-DominguezCBG/ngs-teaching-binder/main)

---

## 📦 What is Binder?

Binder allows you to run Jupyter Notebooks in a fully configured environment hosted in the cloud.

- No software installation needed
- Runs entirely in your browser
- Safe, isolated environment (you cannot break anything)

---

## ▶️ How to use this repository

1. Click the Binder badge above to launch
2. Open notebook `0` first and work through them in order
3. Read the explanations and follow the instructions step by step
4. Run each cell using **Shift + Enter**
5. Explore the outputs and reflect on the results

---

## 🖥️ Running commands in notebooks

- By default, notebook cells run **Python code**
- To run Linux commands (e.g. `ls`, `fastqc`, `zcat`), prefix them with:

