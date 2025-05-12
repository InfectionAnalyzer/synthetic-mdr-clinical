
import pandas as pd
import argparse
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata

def generate_synthetic(input_csv, output_csv, method='gaussian'):
    df = pd.read_csv(input_csv)

    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(df)

    if method == 'gaussian':
        from sdv.single_table import GaussianCopulaSynthesizer
        synthesizer = GaussianCopulaSynthesizer(metadata)
    else:
        from sdv.single_table import CTGANSynthesizer
        synthesizer = CTGANSynthesizer(metadata)

    synthesizer.fit(df)
    synthetic_df = synthesizer.sample(len(df))
    synthetic_df.to_csv(output_csv, index=False)
    print(f"Synthetic data saved to: {output_csv}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate synthetic clinical data')
    parser.add_argument('--input', type=str, required=True, help='Path to real dataset CSV')
    parser.add_argument('--output', type=str, required=True, help='Output path for synthetic CSV')
    parser.add_argument('--method', type=str, default='gaussian', choices=['gaussian', 'ctgan'], help='Synthesis method')
    args = parser.parse_args()
    
    generate_synthetic(args.input, args.output, args.method)
