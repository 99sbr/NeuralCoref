import json

class anaphoraDetection(object):

    def corefResolution(self,input_text,model):
        data = model.continuous_coref(utterances=input_text)
        result= model.get_resolved_utterances()
        return result

class mostRepresentative(object):
    def getMostRepresentative(self,input_text,model):
        data = model.continuous_coref(utterances=input_text)
        result = model.get_most_representative()
        result = dict((str(k), str(v)) for k, v in result.items())
        return result


