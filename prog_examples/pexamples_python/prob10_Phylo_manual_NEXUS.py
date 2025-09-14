import re

def parse_nexus_tree(file_path):
    """Parses a NEXUS TREES block and returns a root Node object."""
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Parse the TRANSLATE block
    translate_block_match = re.search(r'BEGIN\s+TREES;.*?TRANSLATE(.*?)END;', content, re.DOTALL)
    if not translate_block_match:
        return None

    translate_str = translate_block_match.group(1)
    translation_table = {}
    for line in translate_str.split(','):
        match = re.search(r'(\d+)\s+([A-Za-z0-9_]+)', line)
        if match:
            translation_table[match.group(1)] = match.group(2)

    # 2. Extract the TREE string
    tree_str_match = re.search(r'TREE\s+.*?=\s+(.*?);', content, re.DOTALL)
    if not tree_str_match:
        return None
    newick_str = tree_str_match.group(1).strip()

    # 3. Recursively parse the Newick string
    def parse_newick_recursive(newick):
        if not newick:
            return None, ''

        # Match a tip or an internal node with a branch length
        tip_match = re.match(r'([A-Za-z0-9_]+):(\d+\.?\d*)', newick)
        if tip_match:
            node_id, length = tip_match.groups()
            name = translation_table.get(node_id, node_id)
            return Node(name=name, branch_length=float(length)), newick[tip_match.end():]

        # Match a clade
        if newick[0] == '(':
            newick = newick[1:]
            parent_node = Node(branch_length=0.0)
            while True:
                child, remaining = parse_newick_recursive(newick)
                parent_node.children.append(child)
                child.parent = parent_node
                newick = remaining
                if newick[0] == ',':
                    newick = newick[1:]
                elif newick[0] == ')':
                    newick = newick[1:]
                    break
            
            # Match internal branch length
            length_match = re.match(r':(\d+\.?\d*)', newick)
            if length_match:
                parent_node.branch_length = float(length_match.group(1))
                newick = newick[length_match.end():]

            return parent_node, newick
        
        return None, ''

    root, _ = parse_newick_recursive(newick_str)
    return root

# Example usage with a dummy NEXUS file
# You would need to save this content into a file named 'dummy_tree.nex'
nexus_content = """
#NEXUS
BEGIN TAXA;
DIMENSIONS NTAX=3;
TAXLABELS Human Chimp Gorilla;
END;

BEGIN TREES;
TRANSLATE
1 Human,
2 Chimp,
3 Gorilla;
TREE tree_1 = ((1:0.1,2:0.2):0.05,3:0.3);
END;
"""
with open('dummy_tree.nex', 'w') as f:
    f.write(nexus_content)

# Parse the tree from the file
root_node = parse_nexus_tree('dummy_tree.nex')

if root_node:
    print("Tree loaded successfully into a custom Node object structure.")
    print(f"Root node has {len(root_node.children)} children.")
    for child in root_node.children:
        if child.name:
            print(f"Child name: {child.name}, Branch length: {child.branch_length}")
        else:
            print(f"Internal node with branch length: {child.branch_length}")
