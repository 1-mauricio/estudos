# busca sequencial
def busca_sequencial(seq, x):
    '''(list, float) -> bool'''
    for i in range(len(seq) - 1):
        if seq[i] == x:
            return True
    return False