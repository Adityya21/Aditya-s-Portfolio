with open('index.html', 'r', encoding='utf-8') as f: lines = f.readlines()
for i, line in enumerate(lines):
    if 'id="about"' in line or 'id="experience"' in line or 'id="skills"' in line or 'id="projects"' in line or 'id="education"' in line or 'id="contact"' in line:
        print(i, line.strip())
