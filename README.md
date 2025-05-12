
# Synthetic Clinical Data Generator

This toolkit generates high-fidelity synthetic data based on real clinical datasets.

## Features

- Fit marginal distributions to real clinical features (e.g., CRP, LOS)
- Preserve relationships like Age vs Mortality, MDR vs ICU
- Supports:
  - GaussianCopulaSynthesizer (fast, statistically grounded)
  - CTGANSynthesizer (GAN-based)

## How to Use (Google Colab / Local)

```bash
pip install -r requirements.txt
python generate_synthetic.py --input your_real_data.csv --output synthetic_output.csv --method gaussian
```

To use CTGAN:

```bash
python generate_synthetic.py --input your_real_data.csv --output synthetic_output.csv --method ctgan
```

## Author
Built for AI-based MDR Modeling in Clinical Environments
