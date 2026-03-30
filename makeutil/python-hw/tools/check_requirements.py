import ast
import os

def find_imports(path):
    imports = set()
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file)) as f:
                    try:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for n in node.names:
                                    imports.add(n.name.split('.')[0])
                            elif isinstance(node, ast.ImportFrom):
                                if node.module:
                                    imports.add(node.module.split('.')[0])
                    except Exception:
                        pass
    return imports

def read_requirements(filename):
    reqs = set()
    with open(filename) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                reqs.add(line.split('==')[0].split('>=')[0].strip())
    return reqs

if __name__ == "__main__":
    imports = find_imports('src')
    reqs = read_requirements('requirements.txt')
    missing = imports - reqs
    extra = reqs - imports
    if missing:
        print("Missing in requirements.txt:", ', '.join(missing))
    if extra:
        print("Not used in code:", ', '.join(extra))
    if not missing and not extra:
        print("All requirements match imports.")
