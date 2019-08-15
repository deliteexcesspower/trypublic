<!---
### <beg-file_info>
### document_metadata:
###   - caption: "public_snippet_demo"
###     dmid: "uu294frustrate_bronchial"
###     date: created="2019-08-15 14:59:59"
###     last: lastmod="2019-08-15 14:59:59"
###     tags: php,drupal,d7,devel
###     desc: |
###         ## Overview
###         * snippets for use with drupal d7 devel admin/devel/php
###     seealso: |
###         ## See also
###         * regain://uu529grako8smun
### <end-file_info>
--->

## Overview

* these are snippets of php code you can run using https://mydrupalsite.com/devel/php
* this depends on installed and enabled devel module

## shell_exec demo

### simple ls -al

```

  $sgdirr   =   getcwd();
  print( $sgdirr ."\n\n" );
  //pass

  $vtemp    =   shell_exec('ls -al && pwd');
  $dumper   =   var_export( $vtemp , true );
  print( $dumper ."\n\n" );
  //pass

```