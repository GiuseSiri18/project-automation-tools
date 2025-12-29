import os
import sys

def create_project_structure(project_name):
    """
    Creates a standard folder structure for a new software project.
    Standardizes how the team starts new work.
    """
    base_path = f"./{project_name}"
    
    # Lista delle cartelle standard che un team dovrebbe avere
    folders = [
        "docs",           # Documentazione
        "src",            # Codice sorgente
        "tests",          # Test automatici
        "scripts",        # Script di utilità
        "design"          # Mockup e design
    ]

    # Crea le cartelle
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"✅ Created: {path}")

    # Crea un file README base
    with open(f"{base_path}/README.md", "w") as f:
        f.write(f"# {project_name}\n\nProject created automatically.")
        print(f"📄 Created: README.md")

if __name__ == "__main__":
    # Esempio: python setup_project.py "NuovoProgetto"
    if len(sys.argv) > 1:
        create_project_structure(sys.argv[1])
    else:
        print("❌ Error: Please provide a project name.")