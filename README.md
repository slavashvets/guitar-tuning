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


## Example Output

<details>
  <summary>Click to expand example output</summary>

```bash
❯ uv run python cli.py config.yaml --lang en_US
Guitar Tuning Analysis

 String ⁨6 (E2)⁩ (Open: ⁨82.2⁩  
            Hz)             
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Fret ┃ Deviation (cents) ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│  1   │       +6.2        │
│  3   │       +4.4        │
│  5   │       +2.8        │
│  7   │       +2.0        │
│  9   │       +4.5        │
│  12  │       +5.3        │
└──────┴───────────────────┘
╭──────────────────────────────────────────── String: 6 (E2) ─────────────────────────────────────────────╮
│ Grouped Averages:                                                                                           │
│ Low (1,3): ⁨+5.3⁩ cents                                                                                       │
│ Mid (5,7): ⁨+2.4⁩ cents                                                                                       │
│ High (9,12): ⁨+4.9⁩ cents                                                                                     │
│                                                                                                             │
│ Recommendations:                                                                                            │
│ Saddle: ⁨Notes at high frets are significantly sharp. Move the saddle backward (scale length too short).⁩     │
│ Nut: ⁨Low frets are slightly sharp relative to high frets. Consider slightly lowering the nut.⁩               │
│ Bridge: ⁨The string height at the bridge is too high. Lower the saddle (reduce string height at the bridge).⁩ │
│ Truss diff (Mid - High): ⁨-2.5⁩ cents                                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 String ⁨5 (A2)⁩ (Open: ⁨109.8⁩ 
            Hz)             
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Fret ┃ Deviation (cents) ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│  1   │       +5.5        │
│  3   │       +5.6        │
│  5   │       +5.1        │
│  7   │       +0.9        │
│  9   │       +3.2        │
│  12  │       +3.2        │
└──────┴───────────────────┘
╭──────────────────────────────────────────── String: 5 (A2) ─────────────────────────────────────────────╮
│ Grouped Averages:                                                                                       │
│ Low (1,3): ⁨+5.6⁩ cents                                                                                   │
│ Mid (5,7): ⁨+3.0⁩ cents                                                                                   │
│ High (9,12): ⁨+3.2⁩ cents                                                                                 │
│                                                                                                         │
│ Recommendations:                                                                                        │
│ Saddle: ⁨Notes at high frets are significantly sharp. Move the saddle backward (scale length too short).⁩ │
│ Nut: ⁨Low frets are slightly sharp relative to high frets. Consider slightly lowering the nut.⁩           │
│ Bridge: ⁨String height at the bridge is within normal range.⁩                                             │
│ Truss diff (Mid - High): ⁨-0.1⁩ cents                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 String ⁨4 (D3)⁩ (Open: ⁨147.3⁩ 
            Hz)             
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Fret ┃ Deviation (cents) ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│  1   │       +2.7        │
│  3   │       +3.3        │
│  5   │       +4.2        │
│  7   │       +3.1        │
│  9   │       +1.9        │
│  12  │       +3.5        │
└──────┴───────────────────┘
╭─────────────────────────────────────────── String: 4 (D3) ───────────────────────────────────────────╮
│ Grouped Averages:                                                                                    │
│ Low (1,3): ⁨+3.0⁩ cents                                                                                │
│ Mid (5,7): ⁨+3.7⁩ cents                                                                                │
│ High (9,12): ⁨+2.7⁩ cents                                                                              │
│                                                                                                      │
│ Recommendations:                                                                                     │
│ Saddle: ⁨Notes at high frets are slightly sharp. Consider a slight backward adjustment of the saddle.⁩ │
│ Nut: ⁨Low frets are slightly sharp relative to high frets. Consider slightly lowering the nut.⁩        │
│ Bridge: ⁨String height at the bridge is within normal range.⁩                                          │
│ Truss diff (Mid - High): ⁨+1.0⁩ cents                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯
 String ⁨3 (G3)⁩ (Open: ⁨196.2⁩ 
            Hz)             
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Fret ┃ Deviation (cents) ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│  1   │       +3.6        │
│  3   │       +2.1        │
│  5   │       +4.0        │
│  7   │       +0.2        │
│  9   │       -0.9        │
│  12  │       +0.0        │
└──────┴───────────────────┘
╭─────────────────────────────────────────────── String: 3 (G3) ───────────────────────────────────────────────╮
│ Grouped Averages:                                                                                            │
│ Low (1,3): ⁨+2.8⁩ cents                                                                                        │
│ Mid (5,7): ⁨+2.1⁩ cents                                                                                        │
│ High (9,12): ⁨-0.4⁩ cents                                                                                      │
│                                                                                                              │
│ Recommendations:                                                                                             │
│ Saddle: ⁨Notes at high frets are slightly flat. Consider a slight forward adjustment of the saddle.⁩           │
│ Nut: ⁨Low frets are significantly sharp relative to high frets. Lower the nut.⁩                                │
│ Bridge: ⁨The string height at the bridge is too low. Raise the saddle (increase string height at the bridge).⁩ │
│ Truss diff (Mid - High): ⁨+2.5⁩ cents                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 String ⁨2 (B3)⁩ (Open: ⁨247.2⁩ 
            Hz)             
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Fret ┃ Deviation (cents) ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│  1   │       +4.6        │
│  3   │       +3.7        │
│  5   │       +4.3        │
│  7   │       +3.4        │
│  9   │       +2.7        │
│  12  │       +5.6        │
└──────┴───────────────────┘
╭──────────────────────────────────────────── String: 2 (B3) ─────────────────────────────────────────────╮
│ Grouped Averages:                                                                                       │
│ Low (1,3): ⁨+4.2⁩ cents                                                                                   │
│ Mid (5,7): ⁨+3.8⁩ cents                                                                                   │
│ High (9,12): ⁨+4.2⁩ cents                                                                                 │
│                                                                                                         │
│ Recommendations:                                                                                        │
│ Saddle: ⁨Notes at high frets are significantly sharp. Move the saddle backward (scale length too short).⁩ │
│ Nut: ⁨Low frets are slightly flat relative to high frets. Consider slightly raising the nut.⁩             │
│ Bridge: ⁨String height at the bridge is within normal range.⁩                                             │
│ Truss diff (Mid - High): ⁨-0.3⁩ cents                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 String ⁨1 (E4)⁩ (Open: ⁨330.1⁩ 
            Hz)             
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Fret ┃ Deviation (cents) ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│  1   │       +2.8        │
│  3   │       +4.2        │
│  5   │       +3.0        │
│  7   │       +2.8        │
│  9   │       +1.4        │
│  12  │       +4.5        │
└──────┴───────────────────┘
╭─────────────────────────────────────────── String: 1 (E4) ───────────────────────────────────────────╮
│ Grouped Averages:                                                                                    │
│ Low (1,3): ⁨+3.5⁩ cents                                                                                │
│ Mid (5,7): ⁨+2.9⁩ cents                                                                                │
│ High (9,12): ⁨+2.9⁩ cents                                                                              │
│                                                                                                      │
│ Recommendations:                                                                                     │
│ Saddle: ⁨Notes at high frets are slightly sharp. Consider a slight backward adjustment of the saddle.⁩ │
│ Nut: ⁨Low frets are slightly sharp relative to high frets. Consider slightly lowering the nut.⁩        │
│ Bridge: ⁨String height at the bridge is within normal range.⁩                                          │
│ Truss diff (Mid - High): ⁨+0.0⁩ cents                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────── Overall ─────────────────────────────────────────────────────────────────────────╮
│ Overall Truss Rod Recommendation:                                                                                                                         │
│ Average Truss Diff (Mid - High): ⁨+0.1⁩ cents                                                                                                               │
│                                                                                                                                                           │
│ Mid frets are slightly sharp relative to high frets. Consider a slight truss rod adjustment.Tip: Rotate the truss rod ⁨clockwise⁩ by ⁨⁨0.01⁩ turns (about ⁨3⁩°).⁩ │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

</details>

## License

This project is released under the [MIT License](LICENSE).
