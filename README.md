
# Media Preparation Automation

This project automates the process of generating step-by-step instructions for preparing cell culture media. It includes calculations for stock solution preparations, media preparation steps, and an appendix with detailed calculations.

## Features

- **Base Media Volume Adjustment**: Ensures that the base media volume is adjusted to account for all components, keeping the final volume accurate.
- **Media Preparation Table**: Includes steps for each component, the desired concentration, and the volume to add.
- **Detailed Appendix**: Provides calculations for stock solutions and media preparation for transparency and reproducibility.
- **Dynamic Output Filename**: Generates a Word document with the recipe name and final volume as part of the filename (e.g., `colonMedia_15mL.docx`).

## File Structure

- `components.py`: Defines the available components in the lab, including their initial weights, units, molecular weights, and other properties.
- `mediaCalc.py`: Contains helper classes and functions for calculations and Word document generation.
- `recipe_generator.py`: Main script for generating media preparation documents.
- `colonMedia.csv`: Example recipe file for preparing colon media.

## Prerequisites

1. Python 3.8 or higher.
2. Required Python libraries:
   - `python-docx`: For generating Word documents.
   - `pandas`: For handling CSV files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/media-prep.git
   cd media-prep
   ```

2. Install the required dependencies:
   ```bash
   pip install python-docx pandas
   ```

3. Ensure your recipe files are in CSV format with the following structure:
   ```
   Name,Desired Concentration,Desired Unit,Dilution Factor
   Gentamicin,50,μg/mL,
   FBS,,10%,
   ...
   ```

## Usage

1. Edit the `recipe_generator.py` file to specify the recipe file and desired final volume:
   ```python
   recipe_file = 'colonMedia.csv'
   final_volume_ml = 15
   ```

2. Run the main script:
   ```bash
   python recipe_generator.py
   ```

3. The output Word document will be saved in the current directory with a filename like `colonMedia_15mL.docx`.

## Example Output

The generated Word document includes:
- A materials section listing required components.
- Detailed steps for preparing the media, including the base media, FBS, and additives.
- An appendix with all relevant calculations.

## Troubleshooting

- **Incorrect Final Volume**: Ensure that the total volume of additives and FBS does not exceed the desired final volume.
- **Missing Data**: Verify that the recipe file includes all necessary components and values.
- **Stock Preparation Errors**: Check `components.py` to ensure that all components have valid initial weights and units.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
