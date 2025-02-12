# Power BI Report Find and Replace Tool

This Python script leverages the underlying JSON structure of Power BI report layout files to programmatically modify text within various visual elements, such as card titles, tooltips, and other components, across different reports and pages. 

## Motivations

During my time as an Applied Data Fellow at AAAS, I recognized a challenge in maintaining our Power BI reports. Our main reporting tool, Power BI, does not have a built-in find-and-replace function for bulk updates within report layouts. This meant that any changes to text within visuals or report components required manual edits, a time-consuming and error-prone process. This issue became especially apparent when we received requests to update dashboards with multiple similar text elements, prompting the search for a more efficient find-and-replace tool. I developed this script to address this gap and streamline our reporting workflow. My goal was to create a tool that would automate these tedious tasks and reduce the risk of human error. I also wanted to develop a **generalized and reusable** solution that could be adapted to various reports and evolving data needs, ensuring long-term maintainability and scalability.

## How the Code Works

This script works by directly manipulating the underlying JSON structure of Power BI report layout files. Here's a breakdown of the key steps:

1. **File Loading**: The `load-file` function reads the JSON layout file from the specified path, ensuring proper handling of the UTF-16 LE encoding typically used by Power BI.
2. **String Replacement**: The  `replace_string` function is the core of the script. It iterates through each page(section) and visual container within the loaded layout. For each visual, it performs a string replacement on the visual's configuration (`config`) using Python's built-in `replace` method. This function also allows for targeting specific pages for replacements, providing flexibility. To make this process generalized and reusable, stakeholders can easily modify the target strings and page names within the `replace_string` calls to adapt the script to their specific reports and update requirements.
3. **Ordered Replacements**: The `main` function demonstrates how to perform replacements in a specific order. This is crucial for scenarios like updating fiscal years, where the sequence of replacements matters to avoid unintended consequences (e.g., "FY 2024" becoming "FY 2026" before "FY 2025 is updated).
4. **File Saving**: The `save_file ` function writes the modified JSON layout back to the file, preserving the file structure and using indentation for readability.
5. **Main Function**: The `main` function orchestrates the entire process. It defines the file paths, specifies the find and replace strings, and calls the relevant functions to load, process, and save multiple reports.

## Example Usage

The provided code demonstrates how to replace specific strings in two different reports. You can adapt it to your own reports by modifying the file paths, page names, and the strings to be replaced. 

## How to Use

1. **Access the Layout File:** Rename your `.pbix` file to `.zip`. Extract the contents. The `layout.json` file is typically located under `Report/Layout`.
2. **Modify the Script:** Update the `base_path`, `referrer_path`, `appropriations_path`, `page_names`, `old_string`, and `new_string` variables in the Python script to match your report and replacements.
3. **Run the Script:** Execute the Python script.
4.  **Rebuild the PBIX**:
   * Delete the `securityBindings.json` file (if present) from the extracted folder structure.  This file can sometimes cause issues when rebuilding the PBIX.
    * Zip the *entire extracted folder structure* (including the `Report` folder and its contents).
    * Rename the zip file back to a `.pbix` extension.

## Important Considerations

* **Backup**: It's highly recommended to create backups of your Power BI report layout files before running this script. This will allow you to revert to the original state if any issues occur.
* **Testing**: Test the script on a copy of your report files first to ensure the replacements are performed as expected.
* **PBIX Structure**:
  * Power BI reports are zipped archives. Modifying `layout.json` requires extracting it, making changes, and rebuilding the `.pbix`.  Zip the *entire extracted folder structure*.
  * It's often necessary to delete the `securityBindings.json` file before re-zipping to prevent potential inconsistencies and corruption issues in the rebuilt PBIX file.  This file manages data connections and permissions. Sometimes, when you modify the layout and rebuild the PBIX, this file can become out of sync, leading to errors or unexpected behavior in Power BI. Deleting it forces Power BI to regenerate the file, often resolving conflicts.


