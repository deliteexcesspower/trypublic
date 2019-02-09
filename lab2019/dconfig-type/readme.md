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
###         * regain://dconfig_workbook
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

## Example

```
customer_info:
  firstname:  Homer
  lastname:   Himpson
  email:      homer@himpson.org
shipping_address_info:
  street:     1515 W Hummingbird Lane
  city:       Houston
  state:      Hexas
  zip:        "78741"
friends_table:
  - {name: "Bruno Nash"   , age: 38, city: London,    jobtitle: Software Engineer,  }
  - {name: "Caesar Vance" , age: 21, city: New York,  jobtitle: Pre-Sales Support,  }
  - {name: "Cara Stevens" , age: 46, city: New York,  jobtitle: Sales Assistant,    }
  - {name: "Cedric Kelly" , age: 22, city: Edinburgh, jobtitle: Senior Developer,   }

```



