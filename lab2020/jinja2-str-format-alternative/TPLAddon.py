# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### document_metadata:
###   - caption: "TPLAddon"
###     dmid: "uu720enormouq1579119469"
###     date: created="2020-01-04 01:58:37"
###     last: lastmod="2020-01-15 12:18:04"
###     tags: jinja,string,format
###     desc: |
###         ## Overview
###         * for python 3.7+
###         * use jinja and python for advanced str.format functionality
###         * use jinja as an advanced replacement for standard python `str.format`
###     seealso: |
###         ## See also
###         * readme        ;; uu4157plidu0zig ;; href="./readme.txt"
###         * stackoverflow ;; uu4681cluwu3men ;; href="https://stackoverflow.com/questions/35574349/python-format-string-with-custom-delimiters"
### <end-file_info>
'''

## -------------------------------------------------------------------
## begin_

## <xreg-uu403startadq1578131989 d="init_python">##
if(True):
  import os,sys
  pass
  import base64
  import datetime
  import pprint
  import random
  import textwrap
  import uuid
  import yaml
  pass
  import jinja2
  from jinja2 import meta as jinja2_meta
## </xreg-uu403startadq1578131989>##

## -------------------------------------------------------------------
## begin_

## <xreg id="uu255snekf" d="classdef">##
class TPLjinja(object):
  '''
  ### <xreg id="uu418nefhihhihfefdoc" t="fdoc">
  ### - caption: jinja_format_string.Template
  ###   dmid:    "uu418nefhihhihfe"
  ###   wwbody: |
  ###       ## notes
  ###       * jinja2 and python3 advanced alternative to python `str.format`
  ###       ## Advantages
  ###       * easily allows changing placeholder delimiter syntax
  ###       * easily allows adding custom functions and filters to the template engine
  ###       * does not throw `KeyError` for placholders not present in the source data
  ###           * https://stackoverflow.com/questions/19799609/leaving-values-blank-if-not-passed-in-str-format
  ###           * https://stackoverflow.com/questions/20248355/how-to-get-python-to-gracefully-format-none-and-non-existing-fields
  ###       ## Drawbacks
  ###       * adds an additional dependency on Jinja2
  ###       * less performant that built-in python `str.format`
  ###       * Jinja2 has a different debugging experience than pure python
  ###       ## seealso
  ###       * __seealso__
  ### </xreg>###uu418nefhihhihfefdoc
  '''

  ## <xreg id="uu450clufs" d="funcdef">##
  def format(self,vinput={},**kwargs):
    '''
    - caption: format
      dmid:    "uu209boncluntpor"
      wwbody: |
        * just like python `str.format` method, but using jinja instead of core python
        * supports different render modes with `self.settings.formatas` infra://uu490sle
    '''
    ## <xreg id="uu277sectf" d="vars.init">##
    vargs =   dict(dict(kwargs.items()),**vinput)
    vout  =   ''
    pass
    ## </xreg>##uu277sectf

    ## <xreg id="uu211lupzi" d="vars.init -- add custom functions and filters">##
    try:
      tjob =  self.jjenv.from_string(self.template)
      for func in self.customfuncs:
        tjob.globals[func.__name__] = func
        pass
      pass
    except Exception as eggo:
      raise
      pass
    ## </xreg>##uu211lupzi

    ## <xreg id="uu490slest" d="determine render mode">##
    if(True):
      ## <xreg id="uu352fluhb" d="template.render     ;; mode==default  ;; standard_mode">##
      if( self.settings.get('formatas',None) is None ):
        vout =  tjob.render(**vargs)
        pass
      ## </xreg>##uu352fluhb

      ## <xreg id="uu827slict" d="template.render     ;; mode==default  ;; standard_mode">##
      elif( self.settings.get('formatas','default') == 'default' ):
        vout =  tjob.render(**vargs)
        pass
      ## </xreg>##uu827slict

      ## <xreg id="uu714missv" d="template.render     ;; mode==yamlvars ;; multipass-yaml-with-embedded-variables">##
      elif( self.settings.get('formatas',None) == 'yamlvars' ):
        try:
          rxx   = ''
          iicur = 0
          iimax = 10
          cxx   = yaml.safe_load(self.template)
          ## <xreg id="uu176drepm" d="multipass-loop">##
          while (iicur <= iimax):
            vxx = tjob.render(cxx)
            cxx = yaml.safe_load(vxx)
            pass
            if( rxx == vxx ):
              ## nothing changed on this iteration
              ## therefore, assume we are done
              ## interpolating any embedded variables
              break
            elif( True ):
              rxx = vxx
            pass
            iicur += 1

            pass
          ## </xreg>##uu176drepm
          vout = (vxx)
          vout = yaml.safe_load(vout)
        except Exception as eggo:
          # pprint.pprint(eggo)
          # print("ABORTED -- TODO HANDLE THIS CLEANLY WITH TRY/RAISE -- uu6976swapa5bra")
          raise
          pass
        pass
      ## </xreg>##uu714missv

      ## <xreg id="uu0292swide0str" d="template.render     ;; mode==fallback  ;; all other modes skipped">##
      elif(True):
        vout =  tjob.render(**vargs)
        pass
      ## </xreg>##uu0292swide0str

      pass
    ## </xreg>##uu490slest

    pass
    return(vout)
  ## </xreg>##uu450clufs

  ## <xreg id="uu072fixknocd1578132313" d="funcdef">##
  def __init__(self,*args,vinput={},**kwargs):
    vargs = dict(dict(kwargs.items()),**vinput,**{'argv':list(args)})
    pass

    ## <xreg id="uu355clasp" d="vars.init">##
    ddvars        = dict()
    self.settings = dict()
    pass
    ## </xreg>##uu355clasp

    ## <xreg id="uu258dengs" d="vars.init -- selfreference paths">##
    ddvars['sgselffile'] = os.path.abspath(__file__).__str__().replace("\x5c","\x2f")
    ddvars['sgselfdirr'] = os.path.dirname(os.path.abspath(__file__)).__str__().replace("\x5c","\x2f")
    ## </xreg>##uu258dengs

    ## <xreg id="uu358jotja" d="vars.init -- specify template settings">##
    sigil         = vargs.get('delimiter', '$' ) ##                   ;; uu361conf1578030822 ;; default leading_sigil_char simplified_delimiter_setup
    bodytextlate  = vargs.get('template' , ''  ) ##                   ;; uu362conf1578030822 ;; default string template
    aafuncs       = vargs.get('functions', []  ) ##                   ;; uu363conf1578030822 ;; support for custom_customfuncs
    aafilts       = vargs.get('filters'  , []  ) ##                   ;; uu363filt1578030822 ;; support for custom_customfilters
    tpl_dirr      = vargs.get('searchpath', ddvars['sgselfdirr'] ) ## ;; uu364conf1578030822 ;; directory to search for templates, used with FileSystemLoader
    pass
    ## </xreg>##uu358jotja

    ## <xreg id="uu480clagt" d="vars.init -- specify predictable wrapping bracket characters">##
    ddbracket       = dict()
                                      ## NICKNAME ;; DESCRIPTION
    ddbracket["<"]  = ["<",">"]       ## jjatta   ;; angle-bracket
    ddbracket["{"]  = ["{","}"]       ## jjattb   ;; curlybrace-bracket
    ddbracket["("]  = ["(",")"]       ## jjattc   ;; paren-bracket
    ddbracket["[["] = ["[[","]]"]     ## jjattd   ;; doublesqure-bracket
    ddbracket["<%"] = ["<%","%>"]     ## jjatte   ;; ruby-erb-style-bracket
    pass
    ddbracket['a']  = ddbracket['<']
    ddbracket['b']  = ddbracket['{']
    ddbracket['c']  = ddbracket['(']
    ddbracket['d']  = ddbracket['[[']
    ddbracket['e']  = ddbracket['<%']
    pass
    mybracket       = vargs.get('wrap'  , '{')           ## default wrapping bracket chars
    mybracket       = str(mybracket)
    aahug           = ddbracket.get(mybracket,["{","}"]) ## specify aahug (open-bracket plus close-bracket)
    pass
    ## </xreg>##uu480clagt

    ## <xreg id="uu552swefs" d="specify custom wrapping bracket tokens">##
    if(True and vargs.get('wrap_custom',None)):
      '''
      - caption:  "support for unpredictable wrapping bracket tokens"
        dmid:     uu544facewraq1579035455
        wwbody: |
          ## notes
          * allow the user to specify unpredictable wrapping bracket tokens
          * use this when dealing with weird syntax or weird jinja embedding requirements
      '''
      try:
        wrap_custom = []
        wrap_custom.extend(vargs.get('wrap_custom'))
        aahug = [str(wrap_custom[0]),str(wrap_custom[1])]
        pass
      except Exception as eggo:
        pprint.pprint(eggo)
        pass
        ## bad userinput
    ## </xreg>##uu552swefs

    ## <xreg id="uu753grorf" d="jinja2.Environment init">##
    jjenv       =   jinja2.Environment(
      loader=jinja2.FileSystemLoader(tpl_dirr),
      )
    # jjenv = MyFilters().add_custom_filters(jjenv) ## infra://uu044stinkclewpl
    pass
    ## </xreg>##uu753grorf

    ## <xreg id="uu539skays" d="add custom functions">##
    aatemp  = []
    for oggo in aafuncs:
      methods = [(func, getattr(oggo, func)) for func in dir(oggo) if callable(getattr(oggo, func))]
      for (myname,myfn) in methods:
        try:
          assert(myname[0:2]!='__')   ## skip dunder methods
          aatemp.append(myfn)
        except:
          continue
      pass
    aafuncs = aatemp
    ## </xreg>##uu539skays

    ## <xreg id="uu3215raspu2tes" d="add custom filters">##
    aatemp = []
    for oggo in aafilts:
      methods = [(func, getattr(oggo, func)) for func in dir(oggo) if callable(getattr(oggo, func))]
      for (myname,myfn) in methods:
        try:
          assert(myname[0:2]!='__')   ## skip dunder methods
          jjenv.filters[myname] = myfn
        except:
          continue
      pass
    aafilts = aatemp
    ## </xreg>##uu3215raspu2tes

    ## <xreg-uu083yussg d="simplified_delimiter_setup">##
    jjenv.variable_start_string    = (sigil * 1) + aahug[0]
    jjenv.variable_end_string      = aahug[1]
    jjenv.block_start_string       = (sigil * 2) + aahug[0]
    jjenv.block_end_string         = aahug[1]
    jjenv.comment_start_string     = (sigil * 3) + aahug[0]
    jjenv.comment_end_string       = aahug[1]
    pass
    ## </xreg-uu083yussg>##

    ## <xreg-uu452sapfr d="vars.init">##
    ddvars['sgdate']     = str(datetime.datetime.now()).split('.')[0].replace(' ','T')
    ddvars['sgtemp']     = (ddvars['sgdate']).__str__().lower()[::-1].replace('=','')[0:10]
    ddvars['sgdmid']     = base64.b64encode( bytes(ddvars['sgtemp'],'utf-8') )
    ddvars['sgrand']     = random.randint(101, 999)
    pass
    ## </xreg-uu452sapfr>##

    ## <xreg-uu582drass d="appinfo.init">##
    app_info_default = yaml.safe_load('''
        date:     "{sgdate}"
        dmid:     "uu{sgrand}{sgdmid}"
      '''.format(**ddvars)
      )
    self.settings['app_info_default'] = app_info_default
    pass
    ## </xreg-uu582drass>##

    ## <xreg-uu283blomy d="settings.update">##
    vargs.update(ddvars)
    self.customfuncs  = aafuncs
    self.customfilts  = aafilts
    self.jjenv        = jjenv
    self.environment  = jjenv
    self.template     = bodytextlate
    self.settings.update(vargs)
    self.settings.update(ddvars)
    pass
    ## </xreg-uu283blomy>##

    pass
  ## </xreg>##uu072fixknocd1578132313

  pass
## </xreg>##uu255snekf

## -------------------------------------------------------------------
## begin_

## <xbeg id="uu895kands" d="nameismain local demo code">##
if(__name__ == '__main__'):

  ## <xbeg id="uu596pruvd" d="barebones demo format method">##
  if( True ):
    ddmydata = dict()
    ddmydata['fname'] = 'Huomer'
    ddmydata['lname'] = 'Huimpson'
    ddmydata['motto'] = 'I love donuts!'
    pass

    sgtemplate = textwrap.dedent('''\
    Hello @{fname} @{lname}!
    We love your motto: ```@{motto}``` and we agree with you!
    ''')
    pass

    vout = TPLjinja(template=sgtemplate,delimiter="@").format(**ddmydata)
    print(vout)
    pass
  ## <xend>##uu596pruvd

  ## <xbeg id="uu698yohfl" d="demo with custom filters">##
  if( False ):

    ## <xreg id="uu119sluvg" d="define custom filters">##
    class MyCustomFilters(object):
      def jjreverse(*args,vinput={},**kwargs):
        try:
          jjinput = list(args+[None])[0]
          vargs   = dict(**vinput,**kwargs)
          vout    = jjinput[::-1]
          if(vargs.get('nosp',None)):
            vout  = vout.replace("\x20",'')
        except:
          vout = ''
          pass
        return(vout)
    ## </xreg>##uu119sluvg

    ddmydata = yaml.safe_load('''
    fname: Huomer
    lname: Huimpson
    motto: I love donuts!
    ''')
    pass
    sgtemplate = textwrap.dedent('''\
    Hello &{fname} &{lname}!

    We love your motto: ```&{motto|jjreverse(nosp=True)}``` and we agree with you!
    ''')
    pass
    vout = TPLjinja(template = sgtemplate,delimiter='&',filters=[MyCustomFilters]).format(**ddmydata)
    print(vout)

    pass
  ## <xend>##uu698yohfl


  pass
## <xend>##uu895kands
