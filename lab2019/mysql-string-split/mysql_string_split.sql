/*
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu000stringops_trophy"
###     date: created="2019-05-30 15:42:57"
###     last: lastmod="2019-05-30 15:42:57"
###     tags: __tags__
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
###     desc: |
###         * mysql string split
###         * complete demo with create table and data insert
###         * demonstrate use of string split function inside mysql
###         * for use when you do not have convenient access to programming language with native string split support
###     seealso: |
###         * __seealso__
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
*/

/* ------------------------------------------------------------------- */
DROP FUNCTION IF EXISTS fn_str_split;
CREATE FUNCTION `fn_str_split`(
  str     VARCHAR(255) ,
  delim   VARCHAR(12) ,
  pos     INT
) RETURNS VARCHAR(255) CHARSET utf8 RETURN REPLACE (
  SUBSTRING(
    SUBSTRING_INDEX(str , delim , pos) ,
    CHAR_LENGTH(
      SUBSTRING_INDEX(str , delim , pos - 1)
    ) + 1
  ) ,
  delim ,
  ''
);

/* ------------------------------------------------------------------- */
DROP TABLE IF EXISTS `zzdemo_uu000stringops`;
CREATE TABLE `zzdemo_uu000stringops` (
    `mydecimal`       decimal(10,2)     default NULL,
    `myascii`         varchar(255)      default NULL,
    `myinteger`       int(11)           default NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

insert into zzdemo_uu000stringops
values
  ('10.100', "Answer: email single (sub-2048450_q-100)"  , '101' )
  ,('10.200', "Answer: text single (sub-2048450_q-200)"   , '102' )
  ,('10.300', "Answer: text single (sub-2048450_q-300)"   , '103' )
  ,('10.400', "Answer: text single (sub-2048450_q-400)"   , '104' )
;

/* ------------------------------------------------------------------- */
SELECT
  "x" as `x`
  ,mydecimal
  ,myascii
  ,myinteger
  ,fn_str_split(myascii,'_q-',1) as mysplit_str01
  ,fn_str_split(fn_str_split(myascii,'_q-',2),')',1) as mysplit_str02
FROM
  zzdemo_uu000stringops
HAVING
  mysplit_str02 > 200
;



