import json

class anaphoraDetection(object):

    def corefResolution(self,input_text,model):
        data = model(input_text)
        result = data._.coref_resolved
        return result

class mostRepresentative(object):
    def getMostRepresentative(self,input_text,model):
        data = model(input_text)
        result = dict(data._.coref_clusters)
        result = dict((str(k), str(v)) for k, v in result.items())
        return result


