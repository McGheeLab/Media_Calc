# mediaCalc.py
# helpers.py

import csv
from docx import Document
from docx.shared import Inches

class MediaPreparationHelper:
    # Conversion factors for units
    conversion_factors = {
        'mg': 1e-3,      # mg to grams
        'ug': 1e-6,      # ug to grams
        'g': 1,          # grams to grams
        'mg/mL': 1e3,    # mg/mL to μg/mL
        'ug/mL': 1,
        'ng/mL': 1e-3,   # ng/mL to μg/mL
        'M': 1,          # M to M
        'mM': 1e-3,      # mM to M
        'uM': 1e-6,      # uM to M
        'nM': 1e-9,      # nM to M
    }

    def __init__(self, components_stock, final_volume_ml, recipe_file):
        self.components_stock = components_stock
        self.final_volume_ml = final_volume_ml
        self.recipe_file = recipe_file
        self.recipe_data = self.read_recipe(recipe_file)

    def read_recipe(self, recipe_file):
        recipe = []
        with open(recipe_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                component = {
                    'name': row['Name'],
                }
                if 'Dilution Factor' in row and row['Dilution Factor']:
                    component['dilution_factor'] = float(row['Dilution Factor'])
                elif 'Desired Concentration' in row and row['Desired Concentration']:
                    component['desired_concentration'] = float(row['Desired Concentration'])
                    component['desired_unit'] = row['Desired Unit']
                else:
                    continue  # Skip if neither concentration nor dilution factor is provided
                recipe.append(component)
        return recipe

    def find_component_stock(self, name):
        for comp in self.components_stock:
            if comp['name'] == name:
                return comp
        return None

    def calculate_volume(self, component_stock, desired_concentration_info):
        final_volume_ml = self.final_volume_ml

        if 'dilution_factor' in desired_concentration_info:
            # Volume based on dilution factor
            volume_needed_ml = final_volume_ml / desired_concentration_info['dilution_factor']
            volume_needed_ul = volume_needed_ml * 1000
            return volume_needed_ul
        else:
            # Get stock concentration
            stock_concentration = component_stock.get('stock_concentration')
            stock_unit = component_stock.get('stock_unit')
            if stock_concentration is None:
                raise ValueError(f"No stock concentration found for component {component_stock['name']}")

            desired_concentration = desired_concentration_info['desired_concentration']
            desired_unit = desired_concentration_info['desired_unit']

            # Handle working solutions
            if 'working_solution_concentration' in component_stock:
                working_concentration = component_stock['working_solution_concentration']
                working_unit = component_stock['working_solution_unit']

                # Calculate dilution factor to make working solution
                dilution_factor = (stock_concentration * self.conversion_factors[stock_unit]) / \
                                (working_concentration * self.conversion_factors[working_unit])

                component_stock['working_solution_dilution_factor'] = dilution_factor
                stock_concentration = working_concentration
                stock_unit = working_unit

            # Convert concentrations to common units
            stock_conc_common = stock_concentration * self.conversion_factors[stock_unit]
            desired_conc_common = desired_concentration * self.conversion_factors[desired_unit]

            # Calculate volume in uL
            volume_ul = (desired_conc_common * final_volume_ml * 1000) / stock_conc_common

            # Adjust stock concentration if volume is less than 5 uL
            if volume_ul < 5:
                # Calculate new stock concentration to make volume_ul = 5 uL
                volume_ul = 5  # Set minimum volume to 5 uL
                stock_conc_common = (desired_conc_common * final_volume_ml * 1000) / volume_ul
                # Convert back to original stock unit
                new_stock_concentration = stock_conc_common / self.conversion_factors[stock_unit]
                # Update stock concentration in component_stock
                component_stock['adjusted_stock_concentration'] = new_stock_concentration
                component_stock['stock_concentration'] = new_stock_concentration
                # Recalculate volume_ul with the new stock concentration
                volume_ul = (desired_conc_common * final_volume_ml * 1000) / stock_conc_common

            return volume_ul

    
    def calculate_stock_solutions(self):
        stock_preparations = []
        for comp in self.components_stock:
            if 'initial_weight' in comp and 'desired_stock_concentration' in comp:
                initial_weight = comp['initial_weight']  # Amount
                initial_weight_unit = comp['initial_weight_unit']  # Unit
                molecular_weight = comp.get('molecular_weight')  # g/mol
                desired_concentration = comp.get('adjusted_stock_concentration', comp['desired_stock_concentration'])
                stock_unit = comp['stock_unit']
                solvent = comp.get('solvent', 'Appropriate solvent')

                # Convert initial weight to grams
                initial_weight_g = initial_weight * self.conversion_factors[initial_weight_unit]

                # Calculate volume_ml based on the adjusted concentration
                if stock_unit in ['mg/mL', 'μg/mL', 'ug/mL']:
                    # For mass-based concentrations
                    if stock_unit == 'mg/mL':
                        concentration_mg_per_ml = desired_concentration
                    elif stock_unit in ['μg/mL', 'ug/mL']:
                        concentration_mg_per_ml = desired_concentration / 1000  # μg/mL to mg/mL

                    mass_mg = initial_weight_g * 1000  # Convert g to mg
                    volume_ml = mass_mg / concentration_mg_per_ml  # in mL

                elif stock_unit in ['M', 'mM', 'μM', 'uM']:
                    # For molar concentrations
                    if molecular_weight is None:
                        raise ValueError(f"Molecular weight is required for component {comp['name']}")

                    desired_concentration_M = desired_concentration * self.conversion_factors[stock_unit]

                    moles = initial_weight_g / molecular_weight  # in mol
                    volume_L = moles / desired_concentration_M  # in L
                    volume_ml = volume_L * 1000  # in mL

                else:
                    volume_ml = None

                # Adjust initial weight down if volume exceeds 15 mL
                if volume_ml and volume_ml > 15:
                    volume_ml = 15  # Set volume to 15 mL
                    if stock_unit in ['mg/mL', 'μg/mL', 'ug/mL']:
                        # Adjust initial weight accordingly
                        mass_mg = concentration_mg_per_ml * volume_ml  # mg/mL * mL
                        adjusted_initial_weight_g = mass_mg / 1000  # Convert mg to g
                    elif stock_unit in ['M', 'mM', 'μM', 'uM']:
                        moles = desired_concentration_M * (volume_ml / 1000)  # Convert mL to L
                        adjusted_initial_weight_g = moles * molecular_weight  # in g
                    else:
                        adjusted_initial_weight_g = initial_weight_g  # No change

                    # Update initial weight in component
                    comp['initial_weight'] = adjusted_initial_weight_g / self.conversion_factors[initial_weight_unit]  # Convert back to original unit
                    initial_weight_g = adjusted_initial_weight_g

                else:
                    # Use original initial weight
                    comp['initial_weight'] = initial_weight  # Keep original value

                comp['stock_volume_ml'] = volume_ml
                comp['stock_concentration'] = desired_concentration
                comp['stock_unit'] = comp['stock_unit']
                comp['solvent'] = solvent
                stock_preparations.append(comp)
        return stock_preparations


    def generate_recipe(self, recipe):
        # First, calculate stock solutions to ensure 'stock_concentration' is set
        self.calculate_stock_solutions()
        output = []
        for item in recipe:
            component_stock = self.find_component_stock(item['name'])
            if component_stock:
                try:
                    volume_ul = self.calculate_volume(component_stock, item)
                    component_output = {
                        'name': item['name'],
                        'volume_ul': volume_ul,
                    }
                    # Add note if working solution is needed
                    if 'working_solution_dilution_factor' in component_stock:
                        dilution_factor = component_stock['working_solution_dilution_factor']
                        component_output['note'] = f"Prepare working solution by diluting the stock {int(dilution_factor)}:1."
                    output.append(component_output)
                except ValueError as e:
                    output.append({
                        'name': item['name'],
                        'volume_ul': None,
                        'note': str(e)
                    })
            else:
                output.append({
                    'name': item['name'],
                    'volume_ul': None,
                    'note': 'Component not found in stock!'
                })
        return output

    def generate_word_document(self, recipe_output, filename='Media_Preparation.docx'):
        document = Document()

        # Title
        document.add_heading('Procedure to Prepare Media', 0)

        # Materials Needed
        document.add_heading('Materials Needed:', level=1)
        document.add_paragraph('- **Base Media:** HEPES-buffered DMEM/F12 (Gibco, 11330032)')
        document.add_paragraph('- **Fetal Bovine Serum (FBS):** Sigma-Aldrich, F4135')

        # Stock Solution Preparations
        stock_preparations = self.calculate_stock_solutions()
        if stock_preparations:
            document.add_heading('Stock Solution Preparations:', level=1)
            table = document.add_table(rows=1, cols=6)
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Component'
            hdr_cells[1].text = 'Initial Weight'
            hdr_cells[2].text = 'Desired Stock Concentration'
            hdr_cells[3].text = 'Solvent'
            hdr_cells[4].text = 'Volume to Add'

            for comp in stock_preparations:
                row_cells = table.add_row().cells
                row_cells[0].text = comp['name']
                adjusted_weight = comp.get('adjusted_initial_weight', comp['initial_weight'])
                weight_unit = comp.get('initial_weight_unit', 'mg' if adjusted_weight < 1000 else 'g')
                row_cells[1].text = f"{adjusted_weight:.2f} {weight_unit}"
                row_cells[2].text = f"{comp['desired_stock_concentration']} {comp['stock_unit']}"
                row_cells[3].text = comp['solvent']
                volume_ml = comp.get('stock_volume_ml', 'N/A')
                if volume_ml != 'N/A':
                    row_cells[4].text = f"{volume_ml:.2f} mL"
                else:
                    row_cells[4].text = 'N/A'
                note = ''
                if 'adjusted_initial_weight' in comp:
                    note = 'Adjusted initial weight to limit volume to 15 mL.'
                row_cells[5].text = note

            document.add_paragraph('Prepare the stock solutions as per the table above.')


        # Media Preparation Steps
        document.add_heading('Media Preparation Steps:', level=1)

        # Calculate the total volume of additives (in μL)
        total_additives_volume_ul = sum(comp['volume_ul'] for comp in recipe_output if comp['volume_ul'] is not None)
        total_additives_volume_ml = total_additives_volume_ul / 1000  # Convert μL to mL

        # Final volume and FBS volume
        final_volume_ml = self.final_volume_ml
        fbs_volume_ml = 0.10 * final_volume_ml  # FBS is 10% of final volume

        # Adjust base media volume
        base_media_volume_ml = final_volume_ml - fbs_volume_ml - total_additives_volume_ml

        # Ensure base media volume is not negative
        if base_media_volume_ml < 0:
            raise ValueError("Total volume of additives and FBS exceeds the final volume. Adjust final volume or component concentrations.")

        # Create table with columns: Step, Component, Desired Concentration, Volume to Add (μL)
        table = document.add_table(rows=1, cols=4)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Step'
        hdr_cells[1].text = 'Component'
        hdr_cells[2].text = 'Desired Concentration'
        hdr_cells[3].text = 'Volume to Add (μL)'

        step_number = 1

        # Step 1: Add Base Media
        row_cells = table.add_row().cells
        row_cells[0].text = str(step_number)
        row_cells[1].text = 'HEPES-buffered DMEM/F12'
        row_cells[2].text = '-'
        row_cells[3].text = f"{base_media_volume_ml * 1000:.2f}"  # Convert mL to μL
        step_number += 1

        # Step 2: Add FBS
        row_cells = table.add_row().cells
        row_cells[0].text = str(step_number)
        row_cells[1].text = 'Fetal Bovine Serum (FBS)'
        row_cells[2].text = '10% v/v'
        row_cells[3].text = f"{fbs_volume_ml * 1000:.2f}"  # Convert mL to μL
        step_number += 1

        # Add Components
        for comp in recipe_output:
            name = comp['name']
            volume_ul = comp['volume_ul']
            desired_concentration = ''
            # Get desired concentration from recipe data
            for item in self.recipe_data:
                if item['name'] == name:
                    if 'desired_concentration' in item:
                        desired_concentration = f"{item['desired_concentration']} {item['desired_unit']}"
                    elif 'dilution_factor' in item:
                        desired_concentration = f"1:{int(item['dilution_factor'])} dilution"
                    else:
                        desired_concentration = '-'
                    break

            row_cells = table.add_row().cells
            row_cells[0].text = str(step_number)
            row_cells[1].text = name
            row_cells[2].text = desired_concentration
            if volume_ul is not None:
                volume_str = f"{volume_ul:.2f}"
            else:
                volume_str = 'N/A'
            row_cells[3].text = volume_str
            step_number += 1

        # Final Mixing Steps
        document.add_paragraph('\n**Final Steps:**')
        document.add_paragraph('- Gently mix all components to ensure thorough mixing.')
        document.add_paragraph('- Avoid creating bubbles.')
        document.add_paragraph('- Use the media immediately or store at 4°C for up to one week.')
        document.add_paragraph('- Protect from light if light-sensitive components are included.')

         # Append Calculations as an Appendix
        document.add_page_break()
        document.add_heading('Appendix: Detailed Calculations', level=1)

        for comp in self.components_stock:
            if 'stock_concentration' in comp and 'stock_volume_ml' in comp:
                # Add a subheading for each component
                document.add_heading(comp['name'], level=2)
                p = document.add_paragraph()
                initial_weight = comp['initial_weight']
                initial_weight_unit = comp['initial_weight_unit']
                stock_concentration = comp['stock_concentration']
                stock_unit = comp['stock_unit']
                stock_volume_ml = comp['stock_volume_ml']
                solvent = comp['solvent']

                # Stock Solution Preparation Calculations
                p.add_run('Stock Solution Preparation:\n').bold = True
                p.add_run(f"- Initial Weight: {initial_weight:.2f} {initial_weight_unit}\n")
                p.add_run(f"- Solvent: {solvent}\n")
                p.add_run(f"- Desired Stock Concentration: {stock_concentration:.2f} {stock_unit}\n")
                p.add_run(f"- Volume to Add: {stock_volume_ml:.2f} mL\n")

                # Show calculation steps
                p.add_run('Calculations:\n').bold = True
                calculation_text = self.get_stock_preparation_calculation(comp)
                p.add_run(calculation_text + '\n')

                # Media Preparation Volume Calculations
                volume_ul = None
                for item in recipe_output:
                    if item['name'] == comp['name']:
                        volume_ul = item['volume_ul']
                        break

                if volume_ul is not None:
                    p.add_run('Media Preparation:\n').bold = True
                    p.add_run(f"- Volume to Add: {volume_ul:.2f} μL\n")
                    # Show calculation steps
                    p.add_run('Calculations:\n').bold = True
                    calculation_text = self.get_media_preparation_calculation(comp, volume_ul)
                    p.add_run(calculation_text + '\n')

        # Save the document
        document.save(filename)
        print(f"Word document '{filename}' has been generated successfully.")

    def get_stock_preparation_calculation(self, comp):
        # Generate the calculation text for stock solution preparation
        initial_weight = comp['initial_weight']
        initial_weight_unit = comp['initial_weight_unit']
        stock_concentration = comp['stock_concentration']
        stock_unit = comp['stock_unit']
        stock_volume_ml = comp['stock_volume_ml']
        molecular_weight = comp.get('molecular_weight')
        adjusted_concentration = comp.get('adjusted_stock_concentration')

        calculation_steps = ''

        # Convert initial weight to grams
        initial_weight_g = initial_weight * self.conversion_factors[initial_weight_unit]

        if stock_unit in ['mg/mL', 'μg/mL', 'ug/mL']:
            # Mass-based concentration
            if stock_unit == 'mg/mL':
                concentration_mg_per_ml = stock_concentration
            elif stock_unit in ['μg/mL', 'ug/mL']:
                concentration_mg_per_ml = stock_concentration / 1000  # μg/mL to mg/mL

            mass_mg = initial_weight_g * 1000  # g to mg
            calculation_steps += f"Volume (mL) = Mass (mg) / Concentration (mg/mL)\n"
            calculation_steps += f"Volume (mL) = {mass_mg:.2f} mg / {concentration_mg_per_ml:.2f} mg/mL = {stock_volume_ml:.2f} mL"

        elif stock_unit in ['M', 'mM', 'μM', 'uM']:
            # Molar concentration
            if molecular_weight is None:
                calculation_steps += "Molecular weight not provided."
                return calculation_steps

            desired_concentration_M = stock_concentration * self.conversion_factors[stock_unit]

            moles = initial_weight_g / molecular_weight  # mol
            volume_L = moles / desired_concentration_M  # L
            volume_ml_calculated = volume_L * 1000  # mL

            calculation_steps += f"Moles = Mass (g) / Molecular Weight (g/mol)\n"
            calculation_steps += f"Moles = {initial_weight_g:.6f} g / {molecular_weight:.2f} g/mol = {moles:.6f} mol\n"
            calculation_steps += f"Volume (L) = Moles / Concentration (M)\n"
            calculation_steps += f"Volume (L) = {moles:.6f} mol / {desired_concentration_M:.6e} M = {volume_L:.6f} L\n"
            calculation_steps += f"Volume (mL) = {volume_L:.6f} L * 1000 = {volume_ml_calculated:.2f} mL"

        return calculation_steps

    def get_media_preparation_calculation(self, comp, volume_ul):
        # Generate the calculation text for media preparation
        stock_concentration = comp['stock_concentration']
        stock_unit = comp['stock_unit']
        desired_concentration_info = {}
        for item in self.read_recipe('colonMedia.csv'):
            if item['name'] == comp['name']:
                desired_concentration_info = item
                break
        if not desired_concentration_info:
            return "Desired concentration not found in recipe."

        final_volume_ml = self.final_volume_ml
        desired_concentration = desired_concentration_info.get('desired_concentration')
        desired_unit = desired_concentration_info.get('desired_unit')

        # Convert concentrations to common units
        stock_conc_common = stock_concentration * self.conversion_factors[stock_unit]
        desired_conc_common = desired_concentration * self.conversion_factors[desired_unit]

        calculation_steps = ''
        calculation_steps += f"Volume (μL) = (Desired Conc × Final Volume (mL) × 1000) / Stock Conc\n"
        calculation_steps += f"Volume (μL) = ({desired_concentration} {desired_unit} × {final_volume_ml} mL × 1000) / {stock_concentration} {stock_unit}\n"
        calculation_steps += f"Volume (μL) = ({desired_conc_common:.6e} × {final_volume_ml} × 1000) / {stock_conc_common:.6e}\n"
        calculation_steps += f"Volume (μL) = {volume_ul:.2f} μL"

        return calculation_steps