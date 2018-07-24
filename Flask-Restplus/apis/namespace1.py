from __future__ import unicode_literals
from __future__ import print_function
from flask_restplus import Namespace, Resource, fields
from core.model import anaphoraDetection , mostRepresentative
from neuralcoref import Coref
import  spacy



neuralcoref_test_instance = None


api = Namespace('Coreference', description='Coref related operations')

coref_api_model_payload = api.model('NeuralCorefPayload',
                                    {
                                        "input_text": fields.String(required=True, description='Input sentence')
                                    })

coref_api_model_response = api.model('NeuralCorefResponse',
                                     {
                                         "Response": fields.String(required=True, description='Resolved sentence')
                                     })


@api.route('/initialize')
class InitializeLatestModel(Resource):
    @api.doc("Initialize Model")
    def get(self):
        global neuralcoref_test_instance
        neuralcoref_test_instance = Coref()
        return 'Success', 200


@api.route('/isInitialized')
class IsInitialized(Resource):
    """" Check if model is initialized and ready"""

    def get(self):
        global neuralcoref_test_instance
        if neuralcoref_test_instance is None:
            return "Not Initialized"
        else:
            return "Initialized", 200


@api.route('/neuralcoref')
class coreference(Resource):
    @api.doc('Coreference Resolution')
    @api.expect(coref_api_model_payload)
    def post(self):
        global neuralcoref_test_instance
        if neuralcoref_test_instance is None:
            return {'Response': 'Model not initialized'}
        else:
            a_detect = anaphoraDetection()
            result = a_detect.corefResolution(self.api.payload['input_text'], neuralcoref_test_instance)
            return result,200


@api.route('/representatives')
class most_Representative(Resource):
    @api.doc('Get Most Representative')
    @api.expect(coref_api_model_payload)
    def post(self):
        global  neuralcoref_test_instance
        if neuralcoref_test_instance is None:
            return {'Response':'Model not Initialized'}
        else:
            m_response = mostRepresentative()
            result = m_response.getMostRepresentative(self.api.payload['input_text'],neuralcoref_test_instance)
            return result,200