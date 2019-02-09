<!---
### <beg-file_info>
### document_metadata:
###   - caption: "dconfig-type"
###     dmid: "uu224tangi8yunk"
###     date: created="2019-02-08T19:52:14"
###     last: lastmod="2019-02-08T19:52:14"
###     tags: myformats,tymac,dconfig,datatype
###     author: created="__author__"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * defining the dconfig composite variable type
###     seealso: |
###         * __seealso__
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
--->

## Overview

* dconfig is the name of a primitive variable type
* it would be cool if this were native to all mainstream high-level programming languages
* it is not native to all mainstream programming languages
* therefore it is defined here

## Definition

* dconfig is a composite variable type whose root is
    * called `dictionary` in python nomenclature
    * called `associative array` in php nomenclature
    * called `object` in javascript nomenclature
    * called `hash` in perl nomenclature

* dconfig keys are of type `string`

* dconfig values are of type
    * string (with optional naming convention `_string`)
    * list (with optional naming convention `_list`)
    * dictionary (with optional naming convention `_info`)
    * table (with optional naming convention `_table`)

