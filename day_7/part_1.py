'''



'''

from anytree import Node, RenderTree

TEST_FILE = 'day_7_part_1_test.txt'
MY_FILE = 'day_7_part_1_input.txt'


def read_tree_specs(filename):
    with open(filename) as myFile:
        specs = [line.split() for line in myFile]
    return specs


def create_tree_from_specs(specs):
    nodes_dict = {}
    for spec in specs:
        # Create a node for each name we see
        # and populate our hash table with name to node pairs

        n = Node(spec[0], weight=int(spec[1].replace("(", "").replace(")", "")))
        nodes_dict[spec[0]] = n

    for spec in specs:
        if len(spec) <= 2:
            continue
        else:
            # If there was info in the spec regarding children
            # let's add it now.
            children = []
            for child in range(3,len(spec)):
                # Create a list of the children for this parent node
                children.append(nodes_dict[spec[child].replace(",", "")])
            nodes_dict[spec[0]].children = children
    return nodes_dict


def find_unbalanced_subtree(nodes_dict):
    root = nodes_dict['fwft'].root
    weight = 0
    weight = check_sub_tree_weights(root, weight)

    return weight


def check_sub_tree_weights(node, weight):
    if node.children == ():
        weight = node.weight
    else:
        for n in node.children:
            weight += check_sub_tree_weights(n, weight)
        weight += node.weight

    node.subtree_weight = weight
    return weight


if __name__ == '__main__':
    specs = read_tree_specs(TEST_FILE)
    nodes_dict = create_tree_from_specs(specs)

    find_unbalanced_subtree(nodes_dict)