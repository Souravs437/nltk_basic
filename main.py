import nltk
from nltk.corpus import stopwords

stop = stopwords.words('english')

txt = '''
Hi Hello How, my name is Sourav Kumar

'''


def preprocess(doc):
    doc = ' '.join([i for i in doc.split() if i not in stop])
    tagged = nltk.word_tokenize(doc)
    tagged = nltk.pos_tag(tagged)
    nameden = nltk.ne_chunk(tagged, binary=False)
    name = ''
    for chunk in nameden:
        if type(chunk) == nltk.tree.Tree:
            if chunk.label() == 'PERSON':

                name += ' '.join([c[0] for c in chunk])
    return name


# def extract_names(doc):
#     names = []
#     tokens = preprocess(doc)
#     print()
#     for sent in tokens:
#         for chunk in nltk.ne_chunk(sent, binary= False):
#             print(chunk)
#             if type(chunk) == nltk.tree.Tree:
#                 if chunk.label() == 'PERSON':
#                     names.append(' '.join([c[0] for c in chunk]))
#     print(names)


# def ie_preprocess(document):
#     document = ' '.join([i for i in document.split() if i not in stop])
#     sentences = nltk.sent_tokenize(document)
#     sentences = [nltk.word_tokenize(sent) for sent in sentences]
#     sentences = [nltk.pos_tag(sent) for sent in sentences]
#     return sentences


def extract_names(document):
    names = []
    sentences = preprocess(document)
    print(sentences)

if __name__ == '__main__':
    extract_names(txt)
