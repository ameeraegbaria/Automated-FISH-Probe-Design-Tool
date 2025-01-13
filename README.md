# Automated FISH Probe Design Tool

## Introduction

Fluorescence in situ hybridization (FISH) is a molecular cytogenetic technique used to detect and localize specific nucleic acid sequences (DNA or RNA) within cells or tissues. This method employs fluorescently labeled probes that bind to complementary sequences of interest, allowing visualization under a fluorescence microscope.

A key step in FISH is designing DNA probes that hybridize efficiently to target sequences. This process requires careful consideration of probe length, G/C content, melting temperature, and specificity to avoid off-target binding. Manual probe design is labor-intensive and prone to errors, necessitating an automated solution. This project proposes the development of a Python-based tool to automate the probe design process, streamlining workflows for researchers utilizing FISH technologies.

RNA FISH Diagram: ![image](https://github.com/user-attachments/assets/3b5e6fd7-581b-4684-9743-e4da06bd9b89)


## Objectives

The primary objective of this project is to develop a Python script that automates the design of DNA probes for FISH experiments. The tool will ensure high accuracy, flexibility, and user-friendliness by enabling researchers to input a target sequence and customize design parameters as needed. If no specific criteria are provided, the script will use default parameters to generate optimized probe sets suitable for experimental validation.

## Overview of the Tool

The proposed Python tool will process an input DNA sequence to generate a set of probes that adhere to either default or user-defined criteria. The script will incorporate robust validation methods, computational algorithms for sequence analysis, and comprehensive output formats. By automating these steps, the tool will significantly reduce the time and effort required for probe design.

## Methodology

### Input Processing:
- Accept a DNA sequence as input.
- Validate the sequence to ensure it consists of valid nucleotide characters (A, T, C, G).

### Default and Custom Criteria:
- **Default parameters include:**
  - Probe length: 25 nucleotides
  - G/C content range: 40%-60%
  - Melting temperature (Tm) range: 50-70°C
- Users can override default criteria by specifying custom parameters such as probe length, G/C content, and Tm range.

### Probe Design Workflow:
1. Segment the DNA sequence into overlapping or non-overlapping probes of the specified length.
2. Calculate G/C content for each probe.
3. Determine the melting temperature (Tm) using established thermodynamic equations.
4. Filter probes based on the provided or default thresholds for G/C content and Tm.

### Specificity Analysis:
- Perform basic checks to exclude probes with repetitive sequences or regions prone to secondary structure formation.

### Output Generation:
- Compile a list of probes meeting all criteria.
- Provide detailed outputs in CSV and FASTA formats.

## Requirements

### Programming Libraries:
- **Biopython:** For sequence manipulation.
- **Pandas:** For efficient data handling.
- **NumPy:** For computational analysis of melting temperatures and G/C content.
- **Matplotlib (optional):** For graphical visualization.

### System Requirements:
- Python 3.x installed on the user’s system.
- A suitable text editor or Integrated Development Environment (IDE).

## User Input

The script will prompt users to provide the following inputs:
- **DNA Sequence:** The target DNA sequence for probe design.
- **Optional Parameters:**
  - Probe Length
  - G/C Content Range
  - Melting Temperature Range
  - Overlap Length (for overlapping probes)

If no optional parameters are specified, the script will apply default values.

## Output Specifications

The tool will generate:
- A list of probe sequences that meet the specified or default criteria.
- A CSV file containing detailed probe information, including:
  - Sequence
  - G/C content
  - Melting temperature
  - Start and end positions within the input sequence
- A summary report including:
  - Total number of probes designed
  - Average G/C content and Tm
- A FASTA file with the final probe sequences for integration into downstream applications.

## Deliverables

- A fully functional Python script for FISH probe design.
- Comprehensive documentation, including a user guide and installation instructions.
- Example datasets for testing and demonstration purposes.

## Conclusion

The proposed Python-based tool aims to revolutionize the FISH probe design process by automating the generation of optimized probes tailored to either default or user-specified requirements. By combining efficiency, accuracy, and ease of use, this tool will address critical challenges faced by researchers and enhance the reliability of FISH experiments. This project will serve as a practical application of Python programming in the field of molecular biology and bioinformatics.
