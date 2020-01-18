<!---
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu306affluent_tint"
###     date: created="2020-01-18 15:34:10"
###     last: lastmod="2020-01-18 15:34:10"
###     tags: __tags__
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
###     desc: |
###         ## Overview
###         * pseudocode_demo_001aa
###     seealso: |
###         ## See also
###         * __seealso__
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
--->

## multi-return-vs-multi-function

### one-of-several ways to do it variant1 <!--- dmid://uu665waterelq1579390643 --->

* we have a single function that returns structured-output
* PRO ;; return a single structured variable that can be consumed as JSON
* CON ;; caller needs to know that it is going to get a structured variable

```
def output_star_ranking():
  vout = []
  vout.append('zero-star')
  vout.append('one-star')
  vout.append('two-star')
  vout.append('three-star')
  vout.append('four-star')
  vout.append('five-star')
  return(vout)
```

### one-of-several ways to do it variant2 <!--- dmid://uu665waterelq1579390645 --->

* we have multiple functions that each return a single variant of the structured-output
* PRO ;; arguably easier to think about a non-structured 'single-value-return' ... less to remember
* CON ;; not easily represented as JSON
* CON ;; syntax arguably more cumbersome because we have to use `getattr` or `myobject.send`
    * seealso https://stackoverflow.com/questions/771036/php-equivalent-of-send-and-getattr

```
def output_star_ranking_zero():
  vout = []
  vout.append('zero-star')
  return(vout)

def output_star_ranking_one():
  vout = []
  vout.append('one-star')
  return(vout)

def output_star_ranking_two():
  vout = []
  vout.append('two-star')
  return(vout)

def output_star_ranking_three():
  vout = []
  vout.append('three-star')
  return(vout)

def output_star_ranking_four():
  vout = []
  vout.append('four-star')
  return(vout)

def output_star_ranking_five():
  vout = []
  vout.append('five-star')
  return(vout)

```

### different calling styles

```
## variant1
chosen    = 0
myresult  = output_star_ranking()
print(myresult[chosen])

## variant2
chosen    =   0
callstr   =   'output_star_ranking' + 'zero'
myresult  =   myprogram.call(callstr)
print(myresult)

```

