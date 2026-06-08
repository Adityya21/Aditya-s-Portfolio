import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move the HTML section
start_exp = html.find('<section class="section journey-section" id="experience">')
end_exp = html.find('<section class="section" id="skills">')

if start_exp != -1 and end_exp != -1:
    exp_section = html[start_exp:end_exp]
    html = html[:start_exp] + html[end_exp:]
    
    insert_idx = html.find('<section class="section" id="contact">')
    if insert_idx != -1:
        html = html[:insert_idx] + exp_section + html[insert_idx:]
        print("Moved successfully.")
    else:
        print("Contact not found.")
else:
    print("Start or end not found.", start_exp, end_exp)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
