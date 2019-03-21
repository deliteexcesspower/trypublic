# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### document_metadata:
###   - caption: "demo_composite_validation_001a"
###     dmid: "uu182upon_reproach"
###     date: created="2019-03-21 09:21:04"
###     last: lastmod="2019-03-21 09:21:04"
###     tags: __tags__
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * demonstrate the use of composite validation in python
###         * DEPENDENCY -- jmespath query language package
###         * DEPENDENCY -- cerberus validation package
###     seealso: |
###         * __seealso__
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
'''

## --------------------------------------
## begin_:

if('init_python'):
  import os
  import sys
  pass
  import cerberus
  import codecs
  import yaml
  import textwrap
  import jmespath
  import pprint
  pass
##endif

if(True and "sample documents"):
  aadocuments = []
  aadocuments.append(yaml.safe_load('''
      person_fname:       homer
      person_lname:       himpson
      person_age:         1
      prize_caption:      free beer for life
      prize_email:        prizes@abcbooze.com
      prize_category:     alchohol
    '''))
  aadocuments.append(yaml.safe_load('''
      person_fname:       jomer
      person_lname:       jimpson
    '''))
  aadocuments.append(yaml.safe_load('''
      person_fname:       helen
      person_lname:       himpson
      person_age:         16
      prize_caption:      free ammo for life
      prize_email:        prizes@zzzguns.com
      prize_category:     firearms
    '''))
  aadocuments.append(yaml.safe_load('''
    person_fname:         maggie
    person_lname:         himpson
    person_age:           3
    prize_caption:        free puppy
    prize_email:          prizes@123pets.com
    prize_category:       pets
    parent_name:          homer himpson
    '''))
  pass
##endif

if(True and "sample validation schemas"):
  aavalidation_rules = yaml.safe_load('''
    - rule_caption:     check-required-fields
      rule_vpath:       "@"
      validation_schema:
        person_fname:
          type: string
          required: true

    - rule_caption:     check-age-range
      rule_vpath:       '@|@.person_age|{"person_age":@}'
      validation_schema:
        person_age:
          "min": 2
          "max": 120

    - rule_caption:     check-underage-minor
      rule_vpath:       '@|@.person_age|{"person_age":@}'
      validation_schema:
        person_age:
          "min": 2
          "max": 120

    - rule_caption:     check-for-allergies
      rule_vpath:       "@|@.person_allergies"
      validation_schema:
        person_allergies:
          required:   True
          type:       string
    ''')
  pass
##endif




