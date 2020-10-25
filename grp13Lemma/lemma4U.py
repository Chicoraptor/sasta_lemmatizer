import pickle
class Lemma4U:

    def penn_to_ud(self, tag):
        """Converting the tags of Penn Tree bank to universal UD tags."""

        if tag in ["NN", "NNS"]:
            return "NOUN"
        elif tag in ["NNP", "NNPS"]:
            return "PROPN"
        elif "JJ" in tag or tag == "AFX":
            return "ADJ"
        elif tag in ["#", "$", "SYM"]:
            return "SYM"
        elif tag in "\",-LRB--RRB-.:\'\'" or tag == "HYPH":
            return "PUNCT"
        elif tag == "CC":
            return "CCONJ"
        elif tag == "CD":
            return "NUM"
        elif tag in ["EX", "PRP", "WP"]:
            return "PRON"
        elif tag in ["FW", "LS", "NIL"]:
            return "X"
        elif tag in ["IN", "RP"]:
            return "ADP"
        elif tag in ["DT", "PDT", "PRP$", "WDT", "WP$"]:
            return "DET"
        elif tag in ["POS", "TO"]:
            return "PART"
        elif "RB" in tag or tag == "WBR":
            return "ADV"
        elif tag == "UH":
            return "INTJ"
        elif "VB" in tag or tag == "MD":
            return "VERB"
        else:
            return "X"

    def lemmatize(self, word, pos):
        final_corpus = {}
        with open("final.pkl", 'rb') as f:
            final_corpus.update(pickle.load(f))
        if word in final_corpus:
            if pos in final_corpus[word]:
                return final_corpus[word][pos]
        return word

    def plu_to_sing(self,word):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstwxyz"
        word = str(word).lower()
        if len(word) < 2:
            return word
        if word[-1] == "s":
            if len(word) > 3:
                if word[-3:] == "ves":
                    return word.replace('ves', 'f')
                if word[-3:] == "ies":
                    return word.replace("ies", 'y')
                if word[-2:] == "es":
                    if word[-3:] == "ses" and word[-4] in vowels:
                        return word[:-1]
                    if word[-4:] == "zzes":
                        return word.replace('zzes', 'z')
                    return word[:-2]
                if word[-2:] == "ys":
                    return word.replace('ys', 'y')
                return word[:-1]
        return word