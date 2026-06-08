import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move the HTML section
start_exp = html.find('<section class="section journey-section" id="experience">')
end_exp = html.find('<section class="section section-compact" id="skills">')

if start_exp != -1 and end_exp != -1:
    exp_section = html[start_exp:end_exp]
    html = html[:start_exp] + html[end_exp:]
    
    insert_idx = html.find('<section class="section" id="contact">')
    if insert_idx != -1:
        html = html[:insert_idx] + exp_section + html[insert_idx:]

# 2. Update JS array
old_array = "const sections = ['hero', 'about', 'experience', 'skills', 'projects', 'education', 'contact'];"
new_array = "const sections = ['hero', 'about', 'skills', 'projects', 'education', 'experience', 'contact'];"
html = html.replace(old_array, new_array)

# 3. Update Navbar
old_nav = '''                <a href="#experience" class="nav-link">Extra Curriculars</a>
                <a href="#skills" class="nav-link">Skills</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#education" class="nav-link">Education</a>'''
new_nav = '''                <a href="#skills" class="nav-link">Skills</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#education" class="nav-link">Education</a>
                <a href="#experience" class="nav-link">Extra Curriculars</a>'''
html = html.replace(old_nav, new_nav)

# 4. Update checkpoints
old_checkpoints = '''            <div class="checkpoint" data-section="experience">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Extra Curriculars</span>
            </div>
            <div class="checkpoint" data-section="skills">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Skills</span>
            </div>
            <div class="checkpoint" data-section="projects">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Projects</span>
            </div>
            <div class="checkpoint" data-section="education">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Education</span>
            </div>'''
new_checkpoints = '''            <div class="checkpoint" data-section="skills">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Skills</span>
            </div>
            <div class="checkpoint" data-section="projects">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Projects</span>
            </div>
            <div class="checkpoint" data-section="education">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Education</span>
            </div>
            <div class="checkpoint" data-section="experience">
                <div class="checkpoint-dot"></div>
                <span class="checkpoint-label">Extra Curriculars</span>
            </div>'''
html = html.replace(old_checkpoints, new_checkpoints)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Moved Extra Curriculars below Education successfully.")
