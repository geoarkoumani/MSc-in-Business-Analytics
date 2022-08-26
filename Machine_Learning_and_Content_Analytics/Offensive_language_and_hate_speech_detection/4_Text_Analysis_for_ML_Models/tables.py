def display(table):
    from IPython.display import display, HTML
    display(HTML(table))

def read(tname):
    with open(tname, "r", encoding='utf-8') as f:
        return f.read()

import os
BASE_TEMPLATE_DIR = "table_templates"
CONF_MATRIX_TABLE = read(os.path.join(BASE_TEMPLATE_DIR, "conf_matrix.html"))
SCORES_TABLE = read(os.path.join(BASE_TEMPLATE_DIR, "scores_table.html"))
