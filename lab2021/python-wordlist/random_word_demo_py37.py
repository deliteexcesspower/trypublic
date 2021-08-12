# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### document_metadata:
###   - caption: "random_word_demo_py37"
###     dmid: "uu733compactoraytrimming"
###     date: created="2021-08-12 07:38:01"
###     last: lastmod="2021-08-12 07:38:01"
###     namespace:
###         - nams: python/random
###         - nams: programming/wordlist
###     desc: |
###         ## Overview
###         * demo getting a random word with py37
###         * does not require loading an external dictionary or wordlist
###         * this is a 'novelty programming' example, not really practical
###             * limited wordlist length about 500 words
###             * uncommon wordlist skewed toward geeky programming jargon
###     seealso: |
###         ## See also
###         * capt="stacko question" ;; href="https://stackoverflow.com/questions/18834636/random-word-generator-python" ;; tags="__tags01__" ;; id="dmid://uu169stonk1628779x03xlink"
### <end-file_info>
'''

## -------------------------------------------------------------------
## begin_

## <xrbeg id="uu439mospf1628779003aa"   d="python.init">##
if(True):
  import sys
  import re
  import pprint
  import random
  pass
## <xrend>##uu439mospf1628779003aa

# requires python py310
# pprint.pprint(sys.stdlib_module_names)
# exit();

## <xrbeg id="uu669smist1628779"        d="wordlist.init">##
if(True):
  aa33listimpp = '''
  datetime sys pprint os time
  codecs random glob warnings
  token pipes re
  '''.split()
  pass
  vg33modules   = map(__import__, aa33listimpp)
  sg33doctext   = " ".join([vxx.__doc__ for vxx in vg33modules])
  pass
  rgx33word4min = r'[a-zA-Z0-9]{4,}'  ## regex to find words of 4chars or more
  aa33listword  = [str(vxx).lower() for vxx in re.findall(rgx33word4min,sg33doctext) ]
  aa33listword  = set(aa33listword)
  aa33listword  = sorted(aa33listword)
  pass

  pprint.pprint(random.choice(aa33listword))
  pprint.pprint(aa33listword)
  pprint.pprint(aa33listword.__len__())
  pass
## <xrend>##uu669smist1628779
