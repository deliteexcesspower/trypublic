/**
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu639fading_able"
###     date: created="2019-06-11 12:16:01"
###     last: lastmod="2019-06-11 12:16:01"
###     tags: mysql,data,pivot,query,
###     desc: |
###         * single row to multiple rows based on delimited column
###         * not pretty
###     seealso: |
###         * https://stackoverflow.com/questions/2938427/converting-delimited-string-to-multiple-values-in-mysql
###         * https://stackoverflow.com/a/2938522/42223
###         * http://code.openark.org/blog/mysql/unwalking-a-string-with-group_concat
### <end-file_info>
**/

/**  -------------------------------------------------------------------
tabledef
**/

DROP TABLE IF EXISTS `zzdemo_uu112pingasrcdata`;
CREATE TABLE `zzdemo_uu112pingasrcdata` (
  `rowid`         varchar(64)             NOT NULL,
  `fld005`        varchar(255)    DEFAULT NULL,
  PRIMARY KEY (`rowid`)
) ENGINE=InnoDB;

/**  -------------------------------------------------------------------
datarows insert
**/

INSERT IGNORE INTO
      zzdemo_uu112pingasrcdata
VALUES
      ( 'uu761glemtestun', '@@foo/alpha/bravo/charlie/delta/echo/foxy')
      ;

/**  -------------------------------------------------------------------
** show the "BEFORE" picture
SELECT
  mytable.*
FROM
  zzdemo_uu112pingasrcdata as mytable
  ;
**/

/**  -------------------------------------------------------------------
** inspect select show how SUBSTRING_INDEX works
** SUBSTRING_INDEX actually returns a SUBSTRING and not an INTEGER like you might have guessed from the name
** NOTE that using zero is useless and returns nothing

** myascii            ;; mytoken00 ;; mytoken01 ;; mytoken02   ;; mytoken03         ;; mytoken04
** @@foo/alpha/bravo/ ;;           ;; @@foo     ;; @@foo/alpha ;; @@foo/alpha/bravo ;; @@foo/alpha/bravo/

SELECT
  fld005 as myascii
  ,SUBSTRING_INDEX(fld005,'/',0) as mytoken00_zero_does_nothing
  ,SUBSTRING_INDEX(fld005,'/',1) as mytoken01
  ,SUBSTRING_INDEX(fld005,'/',2) as mytoken02
  ,SUBSTRING_INDEX(fld005,'/',3) as mytoken03
  ,SUBSTRING_INDEX(fld005,'/',4) as mytoken04
FROM
  zzdemo_uu112pingasrcdata
  ;
**/

/**  -------------------------------------------------------------------
** inspect select show how SUBSTRING_INDEX works for split_like_functionality
** ANNOYANCE -- this approach does not work properly unless you ensure at least one trailing delimter
**      thats why we do CONCAT(fld005,'/') instead of just fld005
**      @@foo/alpha/bravo/charlie     <-- produces bad results
**      @@foo/alpha/bravo/charlie/    <-- produces good results
**      @@foo/alpha/bravo/charlie//// <-- produces good results
** href="C:/sm/docs/mydaydirs/2019/week25/workup/mysql-trybits/capture-uu926strazufruy.png"
** href="../../image/capture-uu926strazufruy.png"

SELECT
  fld005 as myascii
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',1),'/',-1)  as mytoken01
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',2),'/',-1)  as mytoken02
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',3),'/',-1)  as mytoken03
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',4),'/',-1)  as mytoken04
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',5),'/',-1)  as mytoken05
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',6),'/',-1)  as mytoken06
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',7),'/',-1)  as mytoken07
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',8),'/',-1)  as mytoken08
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',9),'/',-1)  as mytoken09
  ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',10),'/',-1) as mytoken10
FROM
  zzdemo_uu112pingasrcdata
  ;
**/

/**  -------------------------------------------------------------------
** demo convert individual tokens into rows
** here we use UNION with temporary table (subquery) which is not pretty
** we assume there is a maximum of ten items
** we skip token01 @@foo because it is superfluous

SELECT
  tta.*
FROM
(
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',2),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',3),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',4),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',5),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',6),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',7),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',8),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',9),'/',-1)  as txtvalu
    FROM zzdemo_uu112pingasrcdata
UNION
    SELECT
      rowid                                                              as txtname
      ,SUBSTRING_INDEX(SUBSTRING_INDEX(CONCAT(fld005,'/'),'/',10),'/',-1) as txtvalu
    FROM zzdemo_uu112pingasrcdata
) as tta
WHERE 1
  AND (txtvalu is not null)
  AND (txtvalu <> '')
;;;

**/