from django import template  

register = template.Library()
@register.filter(name='row_split')
def row_split(list, row_size):
  chunk=[]
  i=0
  for data in list:
    chunk.append(data)
    i+=1
    if i==row_size:
      yield chunk
      chunk=[]
  yield chunk