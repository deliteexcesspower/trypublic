# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### document_metadata:
###   - caption: "demo_composite_validation_001a"
###     dmid: "uu182upon_reproach"
###     date: created="2019-03-21 09:21:04"
###     last: lastmod="2019-03-21 09:21:04"
###     tags: validation,json,jmespath,python,jsonschema
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
###     desc: |
###         ## Overview
###         * demonstrate the use of composite validation in python
###         * DEPENDENCY -- jmespath query language package
###         * DEPENDENCY -- cerberus validation package
###         ##
###     seealso: |
###         * href="smartpath://mytrybits/p/trypython/lab2014/cerberus/baredemo_jmespath_mixin_conditional.py"
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
'''

'''
## email validation regex

* regain://tryqualtrics/uu098dottedaymoisten
* `(^[^@]+@[^@\.]+[\.][^\.]+)`

'''

## --------------------------------------
## begin_

## <xrbeg id="uu065fendb" d="python.init">##
if(True):
  import os,sys
  pass
  import cerberus
  import codecs
  import itertools
  import jmespath
  import pprint
  import textwrap
  import yaml
  pass
## <xrend>##uu065fendb

## --------------------------------------
## begin_

## <xreg id="uu149pawloclassdef" d="classdef">##
class tinyhelper_validate_houston(object):

  ## <xrbeg id="uu885steppdef" d="funcdef">##
  def proc_apply_validation(self,vinput={},**kwargs):
    '''
    ### <beg-fdoc-uu885steppfdoc>
    ### - caption: __caption__
    ###   dmid:    "uu885stepp001aa"
    ###   wwbody: |
    ###     ## notes
    ###     ## DEPENDENCIES
    ###     * import jmespath
    ###     * import cerberus
    ###     * import itertools
    ###     ## seealso
    ###     * __seealso__
    ###   args: |
    ###     * ddinput['dataroot']    ;; (required) ;; py variable  ;; source document requiring validation
    ###     * ddinput['rules_table'] ;; (required) ;; py aod_table ;; cerberus validation rules_table
    ### <end-fdoc-uu885steppfdoc>
    '''

    ## <xrbeg id="uu885stepp001a" d="vars.init">##
    vargs = dict(dict(kwargs.items()),**vinput)
    ddeml = {'err':False,'data':None,'msg':'','lst':[]}
    vcc   = cerberus.Validator(allow_unknown=True)
    ## <xrend> ##uu885stepp001a>##

    ## <xrbeg id="uu885stepp002a" d="main">##
    if(True):
      try:
        validationrules_table =   vargs.get('rules_table',[])
        dataroot              =   vargs.get('dataroot',{})
        ddeml['data']         =   dataroot
        # pprint.pprint(vargs);exit();
        pass
        ## <xrbeg id="uu707prenk" d="iterate validationrules_table">##
        for myruleset in validationrules_table:
          ddresult = dict()
          ddresult.update(myruleset)
          ddresult['rule_vpath_hasdata']  = ( not jmespath.compile(myruleset['rule_vpath']).search(dataroot) is None )
          ddresult['rule_vpath_dataval']  = ( jmespath.compile(myruleset['rule_vpath']).search(dataroot) )
          pass

          ## <xrbeg id="uu652zuntp" d="">##
          if( ddresult['rule_vpath_hasdata'] ):
            vcc.schema  =   myruleset['validation_schema']
            ddresult['validation_result'] = vcc.validate(dataroot)
            ddresult['validation_errors'] = vcc.errors
          elif(True):
            ddresult['validation_result'] = None
          pass
          # pprint.pprint(ddresult)
          pass
          ## <xrend>##uu652zuntp

          ## <xrbeg id="uu333yipts" d="proc_validate -- apply any custom validation_text">##
          mylist11valikeys = ddresult.get('validation_errors',{}).keys()
          if( mylist11valikeys.__len__() > 0 ):
            ddeml['err']    = True
            mylist13frosso  = [ ddresult.get('validation_text',{}).get(thiskey,['* validation error: {thiskey} either missing or invalid'.format(thiskey=thiskey)]) for thiskey in mylist11valikeys if(thiskey) ]
            mylist13frosso  = itertools.chain.from_iterable(mylist13frosso)
            ddeml['lst'].extend(mylist13frosso)
            ddeml['msg']    = ddeml['lst'][-1]
          pass
          ## <xrend>##uu333yipts
          pass
        ## <xrend>##uu707prenk
        vout = ddeml
        pass
      except Exception as msg:
        ddeml['err']    = True
        ddeml['msg']    = 'failed args.init err://uu885stepp009er -- {msg}'.format(msg=msg,)
        ddeml['lst'].append( ddeml['msg'] )
        pass
        ## return None to indicate abnormal execution
        vout = None
        raise
      pass
    ## <xrend> ##uu885stepp002a>##

    return(vout)
    #pass
  ## <xrend>##uu885steppdef

  ## <xrbeg id="uu149pawloinit" d="funcdef">##
  def __init__(self,vinput={},**kwargs):
    '''
    ### <beg-fdoc-uu149pawlofdoc>
    ### - caption: __caption__
    ###   dmid:    "uu149pawlo001aa"
    ###   wwbody: |
    ###     ## notes
    ###     ## DEPENDENCIES
    ###     * import jmespath
    ###     * import cerberus
    ###     * import itertools
    ###     ## seealso
    ###     * __seealso__
    ### <end-fdoc-uu149pawlofdoc>
    '''

    ## <xrbeg id="uu149pawlo01a" d="func.init">##
    vargs = dict(dict(kwargs.items()),**vinput)
    ddvars = dict()
    pass
    ## <xrend> ##-uu149pawlo01a>##

    ## <xrbeg id="uu149pawlo02a" d="settings.init">##
    ddvars['sgselffile'] = os.path.abspath(__file__).__str__().replace("\x5c","\x2f")
    ddvars['sgselfdirr'] = os.path.dirname(os.path.abspath(__file__)).__str__().replace("\x5c","\x2f")
    pass
    ## <xrend> ##-uu149pawlo02a>##

    vargs.update(ddvars)
    self.settings = dict()
    self.settings.update(vargs)
    pass
  ## <xrend>##uu149pawloinit

  pass
## </xreg>##uu149pawloclassdef

## --------------------------------------
## begin_

## <xrbeg id="uu888priwv" d="sample documents to validate">##
if(True):
  aadocuments = []
  aadocuments.append(yaml.safe_load('''
      person_fname:         cuomer
      person_lname:         cuimpson
      person_age:           34
      person_email:         invalidemailformat.com
    '''))
  aadocuments.append(yaml.safe_load('''
      person_fname:         duomer
      person_lname:         duimpson
      person_age:           1
      prize_caption:        free beer for life
      prize_email:          prizes@abcbooze.com
      prize_category:       alchohol
      fave_oddnumber:       3
    '''))
  aadocuments.append(yaml.safe_load('''
      person_fname:         muomer
      person_lname:         muimpson
      person_age:           30
      prize_caption:        free beer for life
      prize_email:          invalidemailformat.com
      prize_category:       alchohol
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
  aadocuments.append(yaml.safe_load('''
      ## fieldnames misspelled
      ## age is missing
      person_firstname:     fuomer
      person_lastname:      fuimpson
    '''))
  aadocuments.append(yaml.safe_load('''
      ## missing age
      person_fname:         jomer
      person_lname:         jimpson
      fave_oddnumber:       3
    '''))
  aadocuments.append(yaml.safe_load('''
      ## cannot give firearms to a minor
      person_fname:         helen
      person_lname:         himpson
      person_age:           16
      prize_caption:        free ammo for life
      prize_email:          prizes@zzzguns.com
      prize_category:       firearms
    '''))
  aadocuments.append(yaml.safe_load('''
      person_fname:         kuomer
      person_lname:         kuimpson
      person_age:           17
      fave_oddnumber:       4
      person_allergies:     gluten
    '''))
  pass
## <xrend>##uu888priwv

## --------------------------------------
## begin_

## <xrbeg id="uu852snuwp" d="sample validation schema">##
if(True):
  ## <xrbeg id="uu161stinb" d="funcdef">##
  def validator_oddity(field, value, error):
      if( not (value % 2) == 1 ):
          error(field, "Must be an odd number")
      pass
  ## <xrend>##uu161stinb

  validationrules_table = yaml.safe_load('''
    - rule_caption:     check-wellformed-fields
      rule_vpath:       "@"
      ## you can include optional validation_text.
      ## formatas list, one message per list element.
      ## put the list under a dict key that corresponds to the validation_schema key
      validation_text:
        person_email:
          - 'Email address must be correctly formatted.'
      validation_schema:
        person_email:
          required: false
          type:     string
          regex:    '(^[^@]+@[^@\.]+[\.][^\.]+)'

    - rule_caption:     check-required-fields
      rule_vpath:       "@"
      validation_schema:
        person_fname:
          type: string
          required: true
        person_lname:
          type: string
          required: true
        person_age:
          type: ['string','integer']
          required: true

    # NO__WORKY -- check_with requires a callable, but here we are
    # in YAML which makes it a scalar, so cerberus check_with fails
    # - rule_caption:     check-fave_oddnumber
    #   rule_vpath:       '@|@.fave_oddnumber|{"fave_oddnumber":@}'
    #   validation_schema:
    #     fave_oddnumber:
    #       check_with: validator_oddity

    - rule_caption:     check-age-range
      rule_vpath:       '@|@.person_age|{"person_age":@}'
      validation_schema:
        person_age:
          "min": 2
          "max": 120

    - rule_caption:     check-underage-minor
      ## this rule_vpath means that this validation element
      ## is not triggred unles person_age exists and is less than 18
      rule_vpath:       '[@]|[? @.person_age < `18`]'
      validation_schema:
        prize_category:
          type: string
          allowed: ['pets','toys','candy']
        prize_email:
          type:     string
          regex:    '(^[^@]+@[^@\.]+[\.][^\.]+)'

    ## counterintuitive -- formerly this had "required"
    ##    rule_vpath evaluates to true iff person_allergies exists
    ##    so why declare `required: true` here at all?
    ##    changed it to evaluate for `forbidden` (opposite of `allowed`)
    - rule_caption:     check-for-allergies
      rule_vpath:       "@|@.person_allergies"
      validation_text:
        person_allergies:
          - If present, the person_allergies field must not contain `gluten` or `air`
      validation_schema:
        person_allergies:
          type:       string
          forbidden:  ['gluten','air']
    ''')
  pass
## <xrend>##uu852snuwp

## --------------------------------------
## begin_
ogghelper = tinyhelper_validate_houston()
pass

## <xrbeg id="uu199fefgi" d="iterate validate multiple documents">##
if(False):
  vcc = cerberus.Validator(allow_unknown=True)
  docslice = aadocuments[0:]
  pass

  for dataroot in docslice:

    print("## -------------------------------------------------------------------")
    print("## -------------------------------------------------------------------")
    print("## {person_fname} {person_lname}".format(**dataroot))
    pass

    for myruleset in validationrules_table:
      print("~~~~")
      ddresult        = dict()
      ddresult.update(myruleset)
      ddresult['rule_vpath_hasdata']  = ( not jmespath.compile(myruleset['rule_vpath']).search(dataroot) is None )
      ddresult['rule_vpath_dataval']  = ( jmespath.compile(myruleset['rule_vpath']).search(dataroot) )
      pass
      if( ddresult['rule_vpath_hasdata'] ):
        vcc.schema  =   myruleset['validation_schema']
        ddresult['validation_result'] = vcc.validate(dataroot)
        ddresult['validation_errors'] = vcc.errors
      elif(True):
        ddresult['validation_result'] = None
      pprint.pprint(ddresult)
    pass

  pass
## <xrend>##uu199fefgi

## <xrbeg id="uu699ziksp" d="validate single document">##
if(True):
  ## <xrbeg id="uu707prenk"     d="proc_apply_validation">##
  mydocument  = aadocuments[-1]
  vresult0909 = ogghelper.proc_apply_validation(
      dataroot=mydocument,
      rules_table=validationrules_table,
      )
  pass
  ## <xrend>##uu707prenk

  ## <xrbeg id="uu510cladr"     d="">##
  pprint.pprint(vresult0909)
  pass
  ## <xrend>##uu510cladr

  pass
## <xrend>##uu699ziksp

