# auto_boolean_formatter
input some poorly formatted boolean rules (written in SAS) and this program will automatically format it correctly.
Output is in Lisp format.

Example:
input text:
(OR, "clean", "dirty", (SENT, (OR, "room"), (OR, "clean")), (AND, (OR, "housekeeping", "cleaning"), (OR, "great job")))

![alt text](https://github.com/andrewhogan93/auto_boolean_formatter/blob/master/example_images/use_case_1.png?raw=true)

Hit the auto format button, and copy and paste the results

![alt text](https://github.com/andrewhogan93/auto_boolean_formatter/blob/master/example_images/use_case_2.png?raw=true)
