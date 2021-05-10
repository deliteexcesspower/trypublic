# java_private_method
<!---
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu636coconutaytranslate"
###     date: created="2021-05-10 01:30:39"
###     last: lastmod="2021-05-10 01:30:39"
###     tags:       __tags__
###     people:
###         - __people__
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
###     namespace:
###         - __namespace__
###     desc: |
###         ## Overview
###         * __desc__
###     seealso: |
###         ## See also
###         * __seealso__
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
--->

## java private method rationale
<!--- dmid="uu550blawcx03xlink" --->

* i am writing some code and i do not have a function name finalized for `foobar_method`
* i need to call foobar_method all over the place in other sourcecode files
* i need a way to not have to search and replace all over the place if i rename foobar_method to something more comprehensible
* i will make it illegal to call foobar_method outside the originating class (sourcecode file)
* that way, no one will call the method until it has a legitimate "public released name"
