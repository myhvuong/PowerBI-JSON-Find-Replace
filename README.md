# Power BI Report Find and Replace Tool

This Python script leverages the underlying JSON structure of Power BI report layout files to programmatically modify text within various visual elements, such as card titles, tooltips, and other components, across different reports and pages. 

## Motivations

During my time as an Applied Data Fellow at AAAS, I recognized a challenge in maintaining our Power BI reports. Our main reporting tool, Power BI, does not have a built-in find-and-replace function for bulk updates within report layouts. This meant that any changes to text within visuals or report components required manual edits, a time-consuming and error-prone process. This was particularly problematic when dealing with multiple reports or frequent updates. I developed this script to address this gap and streamline our reporting workflow. My goal was to create a tool that would automate these tedious tasks and reduce the risk of human error. I also wanted to develop a **generalized and reusable** solution that could be adapted to various reports and evovling data needs. 


