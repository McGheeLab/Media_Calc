# recipe_generator.py

import os  # Import os module to handle file paths
from components import components_stock
from mediaCalc import MediaPreparationHelper

def main():
    # Specify the recipe file and final volume
    recipe_file = 'exampleMedia.csv'  # Replace with your actual recipe file
    final_volume_ml = 15            # Specify the final volume in mL

    # Initialize the helper class
    helper = MediaPreparationHelper(components_stock, final_volume_ml, recipe_file)

    # Generate the recipe
    recipe_output = helper.generate_recipe(helper.recipe_data)

    # Generate the output file name based on the recipe file name and volume
    base_name = os.path.splitext(os.path.basename(recipe_file))[0]
    output_filename = f"{base_name}_{final_volume_ml}mL.docx"

    # Generate the Word document
    helper.generate_word_document(recipe_output, filename=output_filename)

if __name__ == '__main__':
    main()


