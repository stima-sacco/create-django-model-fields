import os

f = open('fields.txt', 'r')

for line in f:
    ln = line.replace('\n', '')
    property = ln.split(' - ')

    field_name = property[0]
    field_type = property[1]

    if field_type == 'String':
        field = field_name + ' = models.CharField(max_length=100, default="", blank=True)'
    elif field_type == 'int':
        field = field_name + ' = models.IntegerField(default=0)'
    elif field_type == 'Bool':
        field = field_name + ' = models.BooleanField(default=False)'
    elif field_type == 'Decimal':
        field = field_name + ' = models.DecimalField(max_digits=15, decimal_places=2, default=0)'
    print(field)

f.close()