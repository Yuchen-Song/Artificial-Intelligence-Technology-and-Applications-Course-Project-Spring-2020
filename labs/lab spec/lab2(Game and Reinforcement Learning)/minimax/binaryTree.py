import matplotlib.pyplot as plt
class BiNode(object):
    """class BiNode provide interface to set up a BiTree Node and to interact"""
    def __init__(self, element=None, left=None, right=None):
        """set up a node """
        self.element = element
        self.left = left
        self.right = right

    def get_element(self):
        """return node.element"""
        return self.element

    def dict_form(self):
        """return node as dict form"""
        dict_set = {
            "element": self.element,
            "left": self.left,
            "right": self.right,
        }
        return dict_set

    def __str__(self):
        """when print a node , print it's element"""
        return str(self.element)


class node_plot():
    """It stores some functions related to the image output of binary tree"""
    def __init__(self, label='BinaryTree'):
        self.label = label
    def draw_init(self):
        """Create a canvas"""
        fig = plt.figure(self.label, figsize=(16,12))
        ax = fig.add_subplot(111)
        return ax
    def get_coord(self, coord_prt, depth_le, depth, child_type="left"):
        """Return the coordinate of the point we want"""
        if child_type == "left":
            x_child = coord_prt[0] - 1 / (2 ** (depth_le + 1))
        elif child_type == "right":
            x_child = coord_prt[0] + 1 / (2 ** (depth_le + 1))
        else:
            raise Exception("illegal child type")
        y_child = coord_prt[1] - 1 / depth
        return x_child, y_child
    def plot_node(self, ax, node_text, center_point, parent_point):
        """Plot node"""
        ax.annotate(node_text, xy=parent_point, xycoords='axes fraction', xytext=center_point,
                    textcoords='axes fraction', va="bottom", ha="center", size=18,
                    bbox=dict(boxstyle='round,pad=1', fc='yellow', ec='k', lw=2, alpha=0.5),
                    arrowprops=dict(facecolor = "r", headlength = 10, headwidth = 10, width = 10))
    def show(self):
        """Show the piture"""
        plt.show()


class BiTree:
    """class BiTree provide interface to set up a BiTree and to interact"""
    def __init__(self, tree_node=None):
        """set up BiTree from BiNode and empty BiTree when nothing is passed"""
        self.root = tree_node
        self.depth = 0

    def get_depth(self):
        """method of getting depth of BiTree"""
        if self.root is None:
            return 0
        else:
            node_queue = list()
            node_queue.append(self.root)
            depth = 0
            while len(node_queue):
                q_len = len(node_queue)
                while q_len:
                    q_node = node_queue.pop(0)
                    q_len = q_len - 1
                    if q_node.left is not None:
                        node_queue.append(q_node.left)
                    if q_node.right is not None:
                        node_queue.append(q_node.right)
                depth = depth + 1
            return depth

    def add_node_in_order(self, element):
        """add a node to existent BiTree in order"""
        node = BiNode(element)

        if self.root is None:
            self.root = node
        else:
            node_queue = list()
            node_queue.append(self.root)
            while len(node_queue):
                q_node = node_queue.pop(0)
                if q_node.left is None:
                    q_node.left = node
                    break
                elif q_node.right is None:
                    q_node.right = node
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)


    def set_up_in_order(self, elements_list):
        """set up BiTree from lists of elements in order """
        for elements in elements_list:
            self.add_node_in_order(elements)


    def view_in_graph(self):
        """use matplotlib.pypplot to help view the BiTree """
        if self.root is None:
            print("An Empty Tree, Nothing to plot")
        else:
            depth = self.get_depth()
            node_plots = node_plot()
            ax = node_plots.draw_init()
            coord0 = (1/2, 1 - 1/(2*depth))
            node_queue = list()
            coord_queue = list()
            node_plots.plot_node(ax, str(self.root.get_element()), coord0, coord0)
            node_queue.append(self.root)
            coord_queue.append(coord0)
            cur_level = 0
            while len(node_queue):
                q_len = len(node_queue)
                while q_len:
                    q_node = node_queue.pop(0)
                    coord_prt = coord_queue.pop(0)
                    q_len = q_len - 1
                    if q_node.left is not None:
                        xc, yc = node_plots.get_coord(coord_prt, cur_level + 1, depth, "left")
                        element = str(q_node.left.get_element())
                        node_plots.plot_node(ax, element, (xc, yc), coord_prt)
                        node_queue.append(q_node.left)
                        coord_queue.append((xc, yc))
                    if q_node.right is not None:
                        xc, yc = node_plots.get_coord(coord_prt, cur_level + 1, depth, "right")
                        element = str(q_node.right.get_element())
                        node_plots.plot_node(ax, element, (xc, yc), coord_prt)
                        node_queue.append(q_node.right)
                        coord_queue.append((xc, yc))
                cur_level += 1
            node_plots.show()


    def fill(self, max_first=False):
        node = self.root
        self._minimax(node, max_first==bool(self.depth%2))


    def _minimax(self, node, max_turn):
        if node is None:
            return None
        elif node.left is None and node.right is None:
            return node.element
        else:
            l = self._minimax(node.left, not max_turn)
            r = self._minimax(node.right, not max_turn)
            if max_turn == True:
                node.element = max(l, r)
            else:
                node.element = min(l, r)
            return node.element


    def build_by_list(self, list_, depth):
        self.depth = depth
        before = 2**depth
        for i in range(1, before):
            self.add_node_in_order(0)
        for i in range(before):
            self.add_node_in_order(list_[i])