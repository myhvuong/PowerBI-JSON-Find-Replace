import json
import os


def load_file(filepath):
    with open(filepath, "r", encoding = "utf-16 le") as f:
        layout = json.load(f)
    return layout


def save_file(layout, filepath):
    """ Save the JSON layout to a file with indentation for readability."""
    with open(filepath, 'w', encoding='utf-16 le') as outfile:
        json.dump(layout, outfile, indent = 4)
       
    print('String updated!')
   
def replace_string(layout, old_string, new_string, page_names = None):
    """
    Replace occurrences of old_string with new_string within specified pages of the layout.
    
    Args:        
        layout (dict): The JSON object containing the layout data.        
        old_string (str): The string to be replaced.        
        new_string (str): The new string that will replace the old string.        
        page_names (set or list, optional): A set or list of page names to limit the replacements to.            
            If not specified, the function will apply replacements to all pages.
    
    This function modifies the layout in place, meaning changes are directly applied to the passed `layout` object.
    """
   
    # check each report page
    for section in layout['sections']:
   
        # if page_names is specified, skip pages that don't match
        if page_names and section.get('displayName') not in page_names:
            continue
       
        # check each visual in a page
        for visual_container in section['visualContainers']:
            visual_container['config'] = visual_container['config'].replace(
                old_string, new_string)
           
def main():
    base_path = r"C:\Users\myhvuong"


    referrer_path = os.path.join(base_path, "Referrer Report_PowerBI_AE - Training", "Report", "Layout")
    appropriations_path = os.path.join(base_path, "Appropriations Dashboard - Training", "Report", "Layout")
   
    # Load and process the Referrer Report
    referrer_layout = load_file(referrer_path)
    page_names = {"2024 Referrer Codes", "2023 Referrer Codes"}
   
    for i in range(1,4):
        replace_string(referrer_layout, old_string = f'DL {i} ', new_string = f'Email {i} ', page_names = page_names)
   
    save_file(referrer_layout, referrer_path)
   
   
    # Load and process the Appropriations Dashboard
    appropriations_layout = load_file(appropriations_path)
   
    # Perform replacements in chronological order to avoid conflicts
    # FY 2024 should not become FY 2025 before FY 2025 becomes FY 2026
    # otherwise, both would end up as FY 2026
    replace_string(appropriations_layout, old_string = 'FY 2025', new_string = 'FY 2026', page_names = None)
    replace_string(appropriations_layout, old_string = 'FY 2024', new_string = 'FY 2025', page_names = None)
   
    save_file(appropriations_layout, appropriations_path)
   
if __name__ == '__main__':
    main()

