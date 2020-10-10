punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a","so" ,"to", "if", "is", "it", "of", "for","and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you","you'd","you've","you'll", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some","not", "in","The", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
frequencies = {}
words = file_contents.split()
for word in words:
    word = word.lower()
        
    if word not in uninteresting_words:
        if word.isalpha() == False:
            for punct in punctuations:
                if punct in word:
                    word = word[:word.find(punct)]
                        
        if word not in frequencies:
            frequencies[word] = 0
        frequencies[word] += 1
