<!---
### <beg-file_info>
### document_metadata:
###   - caption: "caption"
###     dmid: "uu753conflict_travel"
###     date: created="2020-01-18 19:23:28"
###     last: lastmod="2020-01-18 19:23:28"
###     tags: namingconvention,diceware,taguri,
###     desc: |
###         ## Overview
###         * naming convention devised by dreftymac.org
###     seealso: |
###         ## See also
###         * similar concept w3w ;; uu933zipperwhip1581813432 ;; https://duckduckgo.com/?q=what3words&ia=web
###         * wikipedia w3w       ;; uu933zipperwhip1581813433 ;; https://en.wikipedia.org/wiki/What3words
###     seeinstead: |
###         * __seeinstead__
### <end-file_info>
--->

## northware ID naming convention

* create IDs that are:
    * easy for humans to recognize (low-effort recognition, medium to high-effort memorization, depending on size)
    * easy for humans to copy-paste and cross-reference with standard "autocomplete" functionality
    * not obnoxiously long nor obnoxiously distracting to look at
    * capable of being extracted out of any arbitrary text and used in automated processing
    * usable as an alternative to hexadecimal UUID and GUID formats

### Sample northware ID

<!---##xreg id="uu622brect" d="example" ##--->
```
uu400spotlessbee1579404245

[uu400]         ;; part01 ;; low-frequency high-entropy easily-typed tinyid ngram prefix
[spotlessbee]   ;; part02 ;; human-readable human-recognizable diceword ngram
[1579404245]    ;; part03 ;; optional entropy suffix with datetime component

```
<!---##/xreg uu622brect ##--->

* part01:
    * here we use a non-common letter sequence of two or more characters followed by 3 semi-random digits
    * regex specification `/uu[\d]+/`
    * consistently using the same non-common letter sequence makes the ID format easily searchable, easier to type with autocomplete and more amenable to automated processing
    * the trick is choosing a letter sequence that is easy to type, but does not occur commonly (e.g. uu qqu zqp zp zq zpz)
        * NOTE: the letter sequence is less important than the finger-digits used, (this comes into play when considering QWERTY vs DVORAK for example)

* part02:
    * for a human to memorize this ID, they can easily remember `spotlessbee` and do a substring search on that to find it again
    * even if recall is not important, the substring `spotlessbee` is quickly recognizable and can serve as a mnemonic

* part03:
    * entropy suffix further ensures the ID can be made globally unique if desired
    * used here to store a timestamp based on ID creation time
    * this can be anything you want, but using a consistent convention helps

### Comparison: northware ID compared to UUIDS

*  The following two strings are valid UUIDs

```
    ba209999-0c6c-11d2-97cf-00c04f8eea45
    ba209999-0c6c-11d2-97cf-00c04f8aea45
```

* UUIDs have the following issues:
    * what would the user experience be if you had to retype one or both UUIDs
        * with autocomplete assistance?
        * without autocomplete assistance?
    * how easy is it to recognize that they are different UUIDs just by glancing at them?
    * how easy is it to remember or recognize the UUIDs just by glancing at them?



