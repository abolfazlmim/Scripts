from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
def ssimple_table():
    dcc= SimpleDocTemplate("simple_table.pdf", pagesize=letter)
    flowtables=[]
    data=[
        ['col_{}'.format(i) for i in range(1,6)],
        [str(x) for x in range(1,6)],
        ['a','b','c','d','e'],
    ]
    tbl=Table(data)
    flowtables.append(tbl)
    doc.build(flowtables)
    if __name__ == '__main__':
        simple_table()

    