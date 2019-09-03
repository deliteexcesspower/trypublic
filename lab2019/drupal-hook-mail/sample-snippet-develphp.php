<?php
### <beg-block>
### - caption: devel/php sample snippet
###   dmid:    "uu318snistwivfes"
###   date:    "2019-08-27 11:50:34"
###   wwbody: |
###     * this snippet of code can be pasted directly into devel/php to see how it runs
### <end-block>

## <xreg-uu872criz d="drupal_send_email_programmatically">##
function myfakemodulename_mail($key, &$message, $params) {
  ## <xreg-uu504flon001aa d="init">##
  $ddtemporary = [];
  $ddtemporary = array_merge( $ddtemporary , $params );
  ##;;
  ## </xreg-uu504flon001aa>##

  ## <xreg-uu647teyj d="email_key">##
  if( False ){/** noop **/}
  elseif( $key =='email_default' ){
    $message['subject']                 = vsprintf("%s refid://%s",[
      $ddtemporary['tmp_subj'],
      $ddtemporary['tmp_tsid'],
    ]);
    // $message['headers']['Content-Type'] = 'text/html; charset=UTF-8;';
    $message['body'][] = vsprintf("
      Thank you for your online %s parking permit purchase.

      Your request is being processed and your permit will be %s in the next 72 hours.

      Below is information about your purchase:

      Amount:             %s
      Payment Type:       %s

      Please contact Transportation Services if you have any questions.

      Transportation Services
      transportation@example.org
      541-346-5444
      ",[
        $ddtemporary['tmp_sttype'],
        $ddtemporary['tmp_ship'],
        $ddtemporary['tmp_cash'],
        $ddtemporary['tmp_paym'],
      ]);
  }
  ## </xreg-uu647teyj>##
}
function myfakemodulename_sendnow() {
  if ( True ) {
    $params   =   [];
    $params['tmp_tsid']    =   REQUEST_TIME . (string)rand(1000,9999);
    $params['tmp_subj']    =   "Confirmation of your parking permit purchase";
    $params['tmp_ship']    =   "mailed to the address you provided"; //available for pick up at the Transportation Services office
    $params['tmp_sttype']  =   "faculty/staff";  // "student";
    $params['tmp_cash']    =   "$60.00";         //available for pick up at the Transportation Services office
    $params['tmp_paym']    =   "credit card";    //[credit card] [payroll deduction] [student billing]
    //pass
    $from     =   'transportation@example.org';
    $vresult  =   drupal_mail('myfakemodulename', 'email_default', 'nobody@example.org', language_default(), $params, $from);
    //pass
    $vresult  =   ((@$vresult['result']) ? 'True ' : 'False ') . REQUEST_TIME . (string)rand(1000,9999);
    $dumper   =   var_export( $vresult , true );
    drupal_set_message($dumper);
  }
}
myfakemodulename_sendnow();
## </xreg-uu872criz>##
