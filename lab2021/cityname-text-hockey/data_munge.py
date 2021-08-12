# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu674cradlingaycustodian"
###     date: created="2021-05-30 19:26:23"
###     last: lastmod="2021-05-30 19:26:23"
###     tags:       python,munge,codegen,city,world,places
###     people:
###         - __people__
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
###     namespace:
###         - nams: __namespace__
###     desc: |
###         ## Overview
###         * __desc__
###     linktop:
###         -
###     seealso: |
###         ## See also
###         * __seealso__
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
'''

## -------------------------------------------------------------------
## begin_

## <xrbeg id="uu129swasp1622427003aa" d="python.init">##
if(True):
  import os,sys
  pass
  import codecs
  import pprint
  import re
  import yaml
  import jmespath
  pass
  # import codecs
  # import textwrap
## <xrend>##uu129swasp1622427003aa

## -------------------------------------------------------------------
## begin_

## <xrbeg id="uu129swasp1622427005aa" d="nameismain">##
if(__name__ == '__main__'):

  ## <xrbeg id="uu002slelv1622430" d="data_munge -- query data from helpful_format_saltlake">##
  if(True):
    sg711href     =   './cityname_hershey.yaml'
    vg74paggroot  =   yaml.safe_load(codecs.open(sg711href, 'rb', encoding='utf8').read())
    vg55query     =   '''droot|cityname_seent_table|[?len_space   > `0`]|[*]'''
    vg55query     =   '''droot|cityname_seent_table|[?len_nonasc  > `0`]|[*]'''
    vg55query     =   '''droot|cityname_seent_table|[?len_nonasc  == `0` && len_space  == `0`]|[*]'''
    vg22outtable  =   jmespath.compile(vg55query).search(vg74paggroot)
    pass
    # vg7586kostoutt  =   re.findall(r'[\W]+',row['str_name'])
    # print(vg7586kostoutt)
    # vg22outtable    =   [ row for row in vg22outtable if(vg7586kostoutt) ]
    pprint.pprint(vg22outtable)
    pass
  ## <xrend>##uu002slelv1622430

  ## <xrbeg id="uu143tinkz1622428" d="file_munge -- convert raw to helpful_format_saltlake">##
  if(False):
    sg711href = './city-name-raw.txt'
    mytext = codecs.open(sg711href, 'rb', encoding='utf8').read()
    mylines = [vxx for vxx in mytext.splitlines() if (vxx.strip())]
    ag6964trigoutt = []
    pass
    for thisline in mylines:
      ddtemp = dict()
      ddtemp['line']        =   thisline
      ddtemp['len_name']    =   '{vxx:03d}'.format(vxx=thisline.__len__())
      ddtemp['len_space']   =   '{vxx:03d}'.format(vxx=re.findall(r'[\x20]+',thisline).__len__())
      ddtemp['len_nonasc']  =   '{vxx:03d}'.format(vxx=re.findall(r'[^\x00-\x7F]+',thisline).__len__())
      pass
      # sg98cranoutt = ''' {{  cityname: {line} , city_len: '{len}' , city_spa: '{has_space}' }}'''.format(**ddtemp)
      # dd99cranoutt = yaml.safe_load(sg98cranoutt)
      # print(sg98cranoutt)
      # ag6964trigoutt.append(sg98cranoutt)
      ag6964trigoutt.append(ddtemp)
    pass
    # pprint.pprint(ag6964trigoutt)
    vg2520skufoutt = yaml.safe_load('''
      droot: {}
      troot: {}
      ''')
    vg2520skufoutt['droot']['cityname_seent_table'] = ag6964trigoutt
    print(yaml.safe_dump(vg2520skufoutt))
    # print(vg2520skufoutt)
  ## <xrend>##uu143tinkz1622428

  pass
## <xrend>##uu129swasp1622427005aa

