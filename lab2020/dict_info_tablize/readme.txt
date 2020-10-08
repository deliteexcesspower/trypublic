<!---
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu355xunroundvoguiyx"
###     date: created="2020-10-08T11:50:04"
###     last: lastmod="2020-10-08T11:50:04"
###     tags:       python,json,azure,functionapp,reallysimpledata
###     people:
###         - __people__
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
###     namespace:
###         - json/featurespecific
###     desc: |
###         ## Overview
###         * convert json simple_info format into simple_table format (dictionary to aod_table)
###     seealso: |
###         ## See also
###         * __seealso__
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
--->

## Overview
<!--- dmid="uu201slisklink" --->

* json dictionary (simple_info) to json aod_table (simple_table)
* convert BEFORE into AFTER

### BEFORE

* add a sequential token to every name-value pair that needs converted to table format
* in this example it is a trailing underscore followed by an integer `_1` , `_2` . etcetera

```
  {
    "fname_1": "Huomer",
    "fname_2": "Kuomer",
    "fname_3": "Juomer",
    "lname_1": "Huimpson",
    "lname_2": "Kuimpson",
    "lname_3": "Juimpson",
  }
```

### AFTER

```
  [
    {
      "lname": "Huimpson",
      "fname": "Huomer"
    },
    {
      "fname": "Kuomer",
      "lname": "Kuimpson"
    },
    {
      "fname": "Juomer",
      "lname": "Juimpson"
    }
  ]
```

## Issues
<!--- dmid="uu202slisklink" --->

* how to handle non-contiguous sequence
    * (eg) fname_2,fname_3,fname_5,fname_7
    * no exception, just process items in order
* how to handle duplicated sequence
    * (eg) fname_2,fname_3,fname_5,fname_7,fname_3
    * omit duplicated elements and just pick the first one that gets processed


