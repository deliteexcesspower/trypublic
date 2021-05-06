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

## php demo

### php heredoc

```
$sgtemp = <<<uu937floyo0rezu
    SELECT *
    FROM qqperson
    WHERE 1
uu937floyo0rezu
;
print($sgtemp);
```

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

### simple cat contents of a file

```

  $sgdirr   =   getcwd();
  print( $sgdirr ."\n\n" );
  //pass

  $vtemp    =   shell_exec('ls -al && pwd && cat README.txt');
  $dumper   =   var_export( $vtemp , true );
  print( $dumper ."\n\n" );
  //pass

```


### simple installed programs

```

  //$mycmd = 'type 7zip';         // NULL (not-installed ??)
  //$mycmd = 'python --version';    // NULL
  //pass

  $mycmd = 'type ruby';                                 // YES_WORKY
  $mycmd = 'type python';                               // YES_WORKY
  $mycmd = 'type perl';                                 // YES_WORKY
  $mycmd = 'perl --version';                            // YES_WORKY
  $mycmd = "echo alphabetical | perl -pe 's^abe^eba^'"; // YES_WORKY
  $mycmd = "python -c 'print(1212)'";                   // YES_WORKY
  //pass

  $vtemp    =   shell_exec($mycmd);
  $dumper   =   var_export( $vtemp , true );
  print( $dumper ."\n\n" );
  //pass

```