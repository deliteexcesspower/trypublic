<!---
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu701charter_concrete"
###     date: created="2019-12-05 12:45:39"
###     last: lastmod="2019-12-05 12:45:39"
###     tags: __tags__
###     author:     created="__author__"
###     filetype:   "__filetype__"
###     lastupdate: "__lastupdate__"
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

## Partition array of lines into three segments, based on embedded content boundary

* **GOAL:** Partition an array of lines into segments, based on the position of a content boundary.
* The content boundary consists of two lines that contain some unique string that does not appear in any other line.
* In order to demonstrate how this is supposed to work, here are some "Before and After" images.

### Content boundary begins at line zero

<img
  alt="drawing-002aa"
  height="400px"
  src="https://raw.githubusercontent.com/dreftymac/trypublic/master/lab2019/partition-content-boundary/before_and_after_002aa.PNG"
  />

### Content boundary ends at the last line

<img
  alt="drawing-003aa"
  height="400px"
  src="https://raw.githubusercontent.com/dreftymac/trypublic/master/lab2019/partition-content-boundary/before_and_after_003aa.PNG"
  />

### Content boundary begins at line zero and ends at the last line

<img
  alt="drawing-004aa"
  height="400px"
  src="https://raw.githubusercontent.com/dreftymac/trypublic/master/lab2019/partition-content-boundary/before_and_after_004aa.PNG"
  />

### Content boundary begins and ends somewhere between line zero and the last line

<img
  alt="drawing-005aa"
  height="400px"
  src="https://raw.githubusercontent.com/dreftymac/trypublic/master/lab2019/partition-content-boundary/before_and_after_005aa.PNG"
  />

