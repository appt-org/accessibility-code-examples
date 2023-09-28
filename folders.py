# Python script to split multi-platform markdown files into folders per platform

import os
import re

# Match ## "Platform Name" followed by content until next ## or end of file
h1_pattern = "# ([\w ]+).*?(?=##)"
h2_pattern = "## ([\w ]{2,})(.*?)(?=##|\Z)"

directory = os.getcwd()
files = os.listdir(directory)

for file in files:
  file_name, file_extension = os.path.splitext(file)
  if file_extension == ".md":
    folder = os.path.join(directory, file_name)
    if not os.path.exists(folder):
      os.mkdir(folder)
    
    content = open(file, "r").read()

    # Parse content
    match = re.match(h1_pattern, content, re.M|re.S)
    if match:
      # Extract description
      description = match[0].strip() + "\r\n"

      # Extract samples
      samples = re.findall(h2_pattern, content, re.M|re.S)
      for sample in samples:
        platform = sample[0].strip()
        identifier = platform.lower().replace(" ", "-")
        
        if identifier != "wcag":
          text = sample[1].strip() + "\r\n"
          sample_file_name = identifier + ".md"

          # WRITE platform.md
          sample_file = os.path.join(folder, sample_file_name)
          with open(sample_file, "w") as f:
            f.write(text)
      
      # Write README.md
      readme_file = os.path.join(folder, "README.md")
      with open(readme_file, "w") as f:
        f.write(description)
