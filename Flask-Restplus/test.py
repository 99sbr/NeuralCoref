from neuralcoref import Coref

coref = Coref()
clusters = coref.one_shot_coref(utterances=u"She loves him.", context=u"My sister has a dog.")
mentions = coref.get_mentions()
utterances = coref.get_utterances()
resolved_utterance_text = coref.get_resolved_utterances()
most_representative = coref.get_most_representative()

print(clusters)
print(mentions)
print(utterances)
print(resolved_utterance_text)
print(most_representative)

