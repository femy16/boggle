# def get_stems(word):
# #   print(word[:1])
# #   print(word[:2])
# #   print(word[:3])
# #   print(word[:4])
# #   print(word[:5])
#     output=[]
#     i=1
#     while i<=len(word):
        
#         output.append(word[:i])
        
#         i+=1
#     print(output)   
 
# get_stems("hello")

def get_stems(word):
    return [word[:i] for i in range(1, len(word))]


def get_stems_for_word_list(wl):
    stems = []
    for word in wl:    
        stems_for_word = get_stems(word)
        stems += stems_for_word
    return set(stems)


