# Stratocaster Tuning CLI

A lightweight CLI tool for tuning analysis built specifically for Stratocaster guitars. It compares measured string frequencies against ideal values, computes deviations (in cents), and provides adjustment recommendations.

## Overview

Stratocaster Tuning CLI calculates the deviation of each fret from its ideal frequency and suggests adjustments for components like the saddle, nut, and truss rod. It supports multilingual output for English and Russian.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/guitar-tuning.git
cd guitar-tuning
```

## Usage

Prepare your configuration in `config.yaml` and run the analysis with one of the following commands:

```bash
uv cli.py config.yaml --lang en_US
```

or

```bash
uv cli.py config.yaml --lang ru_RU
```

The tool will display the tuning analysis and localized recommendations directly in your terminal.

## Features

- **Accurate Analysis:** Computes deviations (in cents) for each fret.
- **Localized Output:** Supports English and Russian via Fluent.

## License

This project is released under the [MIT License](LICENSE).
