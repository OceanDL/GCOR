#!/usr/bin/python
from owlready2 import *
from parse import Parser
from nltk.tree import Tree
from rdflib.graph import Graph
import xml.etree.ElementTree as ET
import types
import inspect

#data structures
__tree = ET.parse("C:\\Users\\Ocean\\PycharmProjects\\GCOR\\ontology\\HouseholdTasks.owl.xml")
__root = __tree.getroot()
__idiom_dict = {"clean as a whistle":"一尘不染", "clean house":"通吃", "cleaned someone's clock":"淘汰出局", "and":"和", "or":"或", "am":"", "I":"我"}
#tags
__tag_for_individuals = "{http://www.w3.org/2002/07/owl#}NamedIndividual"
__tag_for_type = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}type"
__tag_for_comment = "{http://www.w3.org/2000/01/rdf-schema#}comment"
#keys
__key_for_type_info = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
__key_for_individual_info = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about" 

#		finds the class that phrase belongs to
#		instance name is last element in the list
#
#needs: only searching in source language words should be implemented
def find_class_of(phrase):
	new_phrase = phrase.replace(" ", "_")
	#iterate through dictionary and check if phrase is in there
	for child in __root.iter(__tag_for_individuals):
		if(child.attrib[__key_for_individual_info].split("#")[-1] == new_phrase):
			for class_info in child.iter(__tag_for_type):
				return class_info.attrib[__key_for_type_info].split("#")[-1]

	return None

def find_in_cache(phrase):
	try:
		value = __idiom_dict[phrase]
	except KeyError:
		return None
	return value


	

def child_node_iterator(class_name):
	for child in __root.iter(__tag_for_individuals):
		for class_info in child.iter(__tag_for_type):
			if class_info.attrib[__key_for_type_info].split("#")[-1] == class_name:
				for class_comment in child.iter(__tag_for_comment):
					yield child, class_comment


#		search node's dictionary for target language word
def find_target_language_translation(class_name, language):
	for child, class_comment in child_node_iterator(class_name):
		if class_comment.text == language:
			return child.attrib[__key_for_individual_info].split("#")[-1]
	return None

#		starts at root of the of the parse tree and checks if the
#		phrase at each node is in the idiom cache or dictionary
def find_best_translation(parse_tree, translation):

	for root in parse_tree:
		if(isinstance(root, str)):
			translation.append(root)
			return
		phrase = " ".join(root.leaves())
		class_of = find_class_of(phrase)
		if find_in_cache(phrase) != None:
			translation.append(__idiom_dict[phrase]) 
		elif class_of != None:
			translation.append(find_target_language_translation(class_of, "mandarin"))
		else:
			find_best_translation(root, translation)

	return




if __name__ == '__main__':
	p = Parser()
	parse_tree = p.parse("I am cleaning the bathroom")

	translation = list()
	find_best_translation(parse_tree, translation)

	print(translation)