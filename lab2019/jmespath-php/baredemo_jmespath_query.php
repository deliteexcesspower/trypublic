<?php
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu444lagging_mayday"
###     date: created="2019-10-15 11:25:16"
###     last: lastmod="2019-10-15 11:25:16"
###     tags: jmespath,php,basicops
###     author:     created="dreftymac"
###     desc: |
###         ## Overview
###         * demonstrate basic jmespath with php
###     seealso: |
###         ## See also
###         * project link    ;; https://github.com/jmespath/jmespath.php
###         * project link    ;; https://packagist.org/packages/mtdowling/jmespath.php
###         * project link    ;; http://jmespath.org/examples.html
###         * pipe-expression ;; href="http://jmespath.org/specification.html#pipe-expressions"
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>


// ------------------------------------------------------------------------
// begin_ init_php

require_once(dirname(__FILE__) . "/../../../tryphp/lab2015/jmespath/vendor/autoload.php");

// -------------------------------------------------------------------
// begin_ class

## <xreg-uu084hadte d="classdef">##
class tinyhelper_jmespath_demo {

  ## <xreg-uu720giskc d="funcdef">##
  function sampledata_person_table(){
    $vout = '
      {"_":"x"
        ,"app_info":  {"noop":"x"
            ,"id": "uu404plimpiruko"
        }
        ,"person_table": [
          {
             "fname":   "Huomer",
             "lname":   "Huimpson",
             "age":     33,
             "motto":   "I love donuts!"
          },
          {
             "fname":   "Juomer",
             "lname":   "Juimpson",
             "age":     16,
             "motto":   "I love pizza!"
          },
          {
             "fname":   "Kuomer",
             "lname":   "Kuimpson",
             "age":     35,
             "motto":   "I love seafood!"
          },
          {
             "fname":   "Puomer",
             "lname":   "Puimpson",
             "age":     38,
             "motto":   "I love pumpkins!"
          },
          {
             "fname":   "Allison",
             "lname":   "Abernathy",
             "age":     38,
             "motto":   "I love abs!"
          },
          {
             "fname":   "Luomer",
             "lname":   "Luimpson",
             "age":     36,
             "motto":   "I love pecan pie!"
          }
        ]
      }
    ';
    $vout = json_decode( $vout, true );
    return($vout);
  }
  ## </xreg-uu720giskc>##

  ## <xreg-uu691hiwst d="funcdef">##
  function sampledata_lunch_orders(){
    $vout = '
      {"_":"x"
        ,"order_table": [
          {
             "menuitem":    "pizza",
             "size":        "large",
             "toppings":    ["cheese","sausage","mushroom"],
             "server":      "Cuanderson"
          },
          {
             "menuitem":    "soup",
             "size":        "cup",
             "toppings":    "",
             "server":      "Huimpson"
          },
          {
             "menuitem":   "salad",
             "size":       "small",
             "toppings":    ["ranch-dressing","olives"],
             "server":      "Cuanderson"
          }
        ]
      }
    ';
    $vout = json_decode( $vout, true );
    return($vout);
  }
  ## </xreg-uu691hiwst>##

  ## <xreg-uu769skisk d="funcdef">##
  function __construct($ddinput=Array()) {
    // init vars
    $this->settings     = Array();
    //pass

    $ddvars = [];
    $ddvars['sgselfdirr'] = str_replace("\x5c", '/', dirname(__FILE__));
    //pass

    $this->settings = array_merge($this->settings,$ddvars);
    $this->settings = array_merge($this->settings,$ddinput);
    //pass

    //endfunc
  }
  ## </xreg-uu769skisk>##

  // endclass
}
## </xreg-uu084hadte>##

// ------------------------------------------------------------------------
// begin_: inline nameismain run -- href="http://stackoverflow.com/questions/2413991"
$nameismain = !debug_backtrace();
if( $nameismain ) {
  $oggdemo = new tinyhelper_jmespath_demo();
  //pass

  ## <xreg-uu269roycl d="jmespath functions demo">##
  if( False ){

    ## <xreg-uu374brisp d="vars.init -- dataroot">##
    $dataroot = json_decode('
      {"noop":"x"
        ,"fruit_list": ["apple","banana","cherry","date","elderberry"]
        ,"food_table": [{},{},{}
            , {"name":"apple"      , "type":"fruit"}
            , {"name":"banana"     , "type":"fruit"}
            , {"name":"cherry"     , "type":"fruit"}
            , {"name":"date"       , "type":"fruit"}
            , {"name":"elderberry" , "type":"fruit"}
            , {"name":"flounder"   , "type":"meat"}
            , {"name":"garlic"     , "type":"vegetable"}
            , {"name":"ham"        , "type":"meat"}
          ]
        }
      '
      ,true);
    ## </xreg-uu374brisp>##

    ## <xreg-uu374brisp d="vars.init -- expression">##
    $expression = '@ != null';                // ;; // evaluates to true
    $expression = 'to_string(null)';          // ;; // 'null'
    $expression = 'to_number(`-12`)';          // ;; // -12
    $expression = 'to_string(`-12`)';          // ;; // '-12'
    $expression = 'to_string(``)';            // ;; // ''
    $expression = 'to_string(`1`) && true';  // ;; // NULL
    $expression = '(true == true)';           // ;; // true
    $expression = '(false == false)';         // ;; // true
    $expression = 'contains(`foobar`, `foo`)';            // ;; // evaluates to true
    $expression = 'contains(@|fruit_list|[0], `foo`)';    // ;; // evaluates to false
    $expression = 'contains(@|fruit_list|[0], `ppl`)';    // ;; // evaluates to true
    $expression = 'contains(@|fruit_list|[*], `ppl`)';    // ;; // evaluates to false (list context NO__WORKY with substring)
    $expression = 'contains(@|fruit_list|[*], `apple`)';  // ;; // evaluates to true  (list context YES_WORKY with matching list element)
    $expression = '@|fruit_list|[?contains(@,`rr`)]';     // ;; // returns elements containing substring
    $expression = '@|food_table|[?(@.type == null)]|[*]';                       // ;; // filter-expression (test for null)
    $expression = '@|food_table|[?(@.type != null)]|[*]';                       // ;; // filter-expression (test for non-null)
    $expression = '@|food_table|[0]|keys(@)';                                   // ;; // keys (empty list)
    $expression = '@|food_table|[-1]|keys(@)';                                  // ;; // keys (non-empty list) (indexing on negative integer)
    $expression = '@|food_table|[*].keys(@)';                                   // ;; // keys (non-empty list)
    $expression = '@|food_table|[*].values(@)|[?length(@) != `0`]';             // ;; // values (non-empty list)
    $expression = '@|food_table|[? contains(@.type,`e`)]';                      // ;; // NOTE: this throws an error because we did not filter out the nulls (Argument 0 of contains must be one of the following types: string, array) (seealso: https://stackoverflow.com/a/55307847/42223)
    $expression = '@|food_table|[?(@.type != to_string(`meat`))]';              // ;; // filter-expression (return list_of_dict, includes-empty-element)
    $expression = '@|food_table|[?(@.type == to_string(`meat`))]|[*].name';     // ;; // filter-expression (return list, ignores-empty-element)
    $expression = '@|food_table|[?(@.type!=null)]|[?contains(@.type,`e`)]';     // ;; // filter-expression only those types containing substring 'e'
    ## </xreg-uu374brisp>##

    ## <xreg-uu617pibdr d="output.render">##
    $jpquery  = $expression;
    $vout     = JmesPath\search($jpquery, $dataroot);
    //pass
    $vout = var_export($vout, true);
    print( $vout );
    //pass
    ## </xreg-uu617pibdr>##
  }
  ## </xreg-uu269roycl>##

  ## <xreg-uu745plunk001aa d="jmespath-expression-demo -- sampledata_person_table">##
  if( True ){

    ## <xreg-uu894spufd d="vars.init">##
    $mydelim = '@@';
    ## </xreg-uu894spufd>##

    ## <xreg-uu319stapt d="vars.init -- demo queries">##
    $expression = '@|person_table|[? (@.age<`36`) ].age|sort(@)';                     // ;; // projection by age and sorted
    $expression = '@.person_table|[*].{"Name":join(``,[@.fname,@.lname])}';           // ;; // concat fname and lname
    $expression = '@|person_table|[*].{"Name":join(`::`,[@.fname,@.lname])}';         // ;; // concat fname and lname
    $expression = "@|person_table|[*].{\"Name\":join(`$mydelim`,[@.fname,@.lname])}"; // ;; // concat fname and lname
    $expression = '@|person_table|[0]|(fname != ``)&&(fname != null)';                // ;; // evaluates to true
    $expression = '@.person_table';                           // ;; // returns person_table
    $expression = '@|person_table|[0:2]|[*].fname';           // ;; // list_of_fname (return only two elements)
    $expression = '@.person_table[0:2].fname';                // ;; // list_of_fname (return only two elements)
    $expression = '@';                                        // ;; // entire jpdata data_object
    $expression = '@.[*]';                                    // ;; // entire jpdata data_object (as a list)
    $expression = '@|@|@';                                    // ;; // entire jpdata data_object (redundant pipe-expression)
    $expression = '@.person_table[*].fname';                  // ;; // list_of_fname (sub-expression dot notation)
    $expression = '@.person_table[0].fname';                  // ;; // scalar_value (sub-expression dot notation)
    $expression = '@|person_table|[*].fname';                 // ;; // list_of_fname (pipe-expression)
    $expression = '@|person_table|[*].fname|sort(@)';         // ;; // list_of_fname sorted (pipe-expression)
    $expression = '(@|person_table|[0].fname == `Huomer`)';   // ;; // evaluates to true
    $expression = '(@|person_table|[0].fname != `Juomer`)';   // ;; // evaluates to true
    $expression = '@|person_table|[0]|values(@)';             // ;; // list_of_values
    $expression = '@|person_table|[0]';                       // ;; // dictionary (aka object // aka associative-array)
    $expression = '@|person_table|[0].fname|length(@)';       // ;; // int 6
    $expression = '@|person_table|[4].fname|length(@)';       // ;; // int 7
    $expression = '@|person_table|[0]|values(@)|length(@)';   // ;; // int 4
    $expression = '@|person_table|[0]|@.fname|type(@)';           // ;; // 'string'
    $expression = '@|person_table|[0]|length(@.fname)|type(@)';   // ;; // 'number'
    $expression = '@|person_table|[0]|(@.noexisto)|type(@)';      // ;; // 'null'
    $expression = '@|person_table|[0]|type(@)';                   // ;; // 'object'
    $expression = '@|person_table|[0]|keys(@)|type(@)';           // ;; // 'array'
    $expression = '@|person_table|[*]|type(@)';                   // ;; // 'array'
    ## </xreg-uu319stapt>##

    ## <xreg-uu617pibdr d="output.render">##
    $jpdata   = $oggdemo->sampledata_person_table();
    $jpquery  = $expression;
    $vout     = JmesPath\search($jpquery, $jpdata);
    //pass
    $vout = var_export($vout, true);
    print( $vout );
    //pass
    ## </xreg-uu617pibdr>##

    //endif
  }
  ## </xreg-uu745plunk001aa>##

}
//;;

