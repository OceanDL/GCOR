# GCOR
Machine Translation project using non-language objects 

# Setup
To get the Tensorflow external libraries download Anaconda Navigator and set up a new enviornment with the tensorflow package there. Also pip install the GIPHY Python SDK.

# First-time installation of Stanford CoreNLP
```
mkdir lib && cd lib

wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip

unzip stanford-corenlp-full-2018-10-05.zip
```
# Stanford Server Start-up
First navigate to lib directory, then run the following command:
```
cd stanford-corenlp-full-2018-10-05 && java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```