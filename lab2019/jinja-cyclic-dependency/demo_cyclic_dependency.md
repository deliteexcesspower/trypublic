<!---
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu819footpath_reset"
###     date: created="2019-10-22 14:11:02"
###     last: lastmod="2019-10-22 14:11:02"
###     tags: jinja,variable,demo
###     desc: |
###         ## Overview
###         * demonstrating cyclic dependency in jinja
###     seealso: |
###         ## See also
###         * href="https://en.wikipedia.org/wiki/Circular_dependency"
###         * regain://31967064
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
--->

## Demonstrate circular dependency

```

    ## YAML-based jinja template with cyclic dependency
    var0: "{{var1}}"
    var1: "<xmp>( {{var0}} )</xmp>"

```
