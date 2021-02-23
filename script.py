###############################################
# Generate redoc static html from openapi 3.0.0 
#  Created using Python 3.8.5
# - python3 docGenerator.py {fast} Generates the html, 
#   fast can be used if you already ran it once (setup the necessary repositories)
# - python3 docGenerator.py clean  #clears files generated
#
# Results folder contains the resulting html.
# The rest of the created folders and files are only necessary to rerun the script faster next time
#
#
###############################################


import os
import subprocess
import sys

setup = True

docsWithSnippetFile = "docsWithSnippet.json"
snippetFolder = "snippetRep"
redocFolder = "redocRep"
apiFile = "example.yaml"

def cleanUp():
    try:
        subprocess.run(f"rm -r {docsWithSnippetFile} {snippetFolder} {redocFolder}", shell=True)
    except:
        print("could not clean some files or already cleaned before")
    
def addSnippets():
    docsWithSnippet = open(docsWithSnippetFile, "w")
    if setup: subprocess.run(f"mkdir {snippetFolder}", shell=True)
    if setup: subprocess.run(f"cd {snippetFolder} && npm install snippet-enricher-cli", shell=True)
    #subprocess.run(f"./{snippetFolder}/node_modules/.bin/snippet-enricher-cli --input={apiFile}", shell=True)
    subprocess.run(f"npx snippet-enricher-cli --input={apiFile}", shell=True, stdout=docsWithSnippet)
    return docsWithSnippet

def redocCompile():
        
    if setup: subprocess.run(f"mkdir {redocFolder}", shell=True)
    if setup: subprocess.run(f"cd {redocFolder} && npm install redoc-cli", shell=True)
    subprocess.run(f"npx redoc-cli bundle {docsWithSnippetFile}", shell=True)

def main():
    global setup
    if len(sys.argv) > 1:
        if sys.argv[1] == 'clean':
            cleanUp()
            return
        elif sys.argv[1] == 'fast':
            setup = False

        
    addSnippets()
    redocCompile()

if __name__ == "__main__":
    main()



