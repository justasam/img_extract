from docx import Document

# enter file path here (TODO: args)
FILE_PATH = ''

doc = Document(FILE_PATH)

images = []


def get_shape_blip(shape):
    return shape._inline.graphic.graphicData.pic.blipFill.blip


doc_part = doc.part
i = 0
for shape in doc.inline_shapes:
    img_part = doc_part.related_parts[get_shape_blip(shape).embed]
    image_type = img_part.content_type.split('/')[1]
    fname = 'images/image %s.%s' % (i, image_type)
    print('Writing %s' % fname)
    with open(fname, 'wb') as f:
        f.write(img_part._blob)
        f.close()
    i += 1
    print('Done writing %s' % fname)
