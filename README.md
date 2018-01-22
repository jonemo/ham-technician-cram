ham-technician-cram
===================

The exam for a Technician level Amateur Radio license in the USA consists of 35 multiple choice questions drawn from a pool of approximately 430 questions.
The [ARRL website](http://www.arrl.org/getting-licensed) has all the details about the what and how of amateur radio licensing in the USA.

In order to quickly prepare myself for the exam (taking it was a bit of a snap decision for me), I wrote a simple tool to quiz me on the entire question pool.
This is by no means polished or even usable, but maybe it saves someone else the half hour of data manipulation and Python cowboying I invested into this.

**Note that the question pool gets updated every four year, I worked with the data valid from 2014 to 2018.**

## Data Preparation

How `quespool.json` was made

1. My data source is the [Question Pools section of the NCVEC website](http://ncvec.org/page.php?id=362).
2. Since the link to the `.txt` version of the file is dead, I used the `.doc` and saved it as `raw.txt` to use as the starting point.
3. `python raw_to_json.py > quespool.json`

## Shuffled question pool

Present yourself with all question in the question pool, in shuffled order, and have all the question IDs you got wrong written to `quespool-wrong.txt`:

```
$ python quespool-quiz.py
Question T1E03 (1/425):
---
Who must designate the station control operator?
---
A: The station licensee
B: The FCC
C: The frequency coordinator
D: The ITU
---
? a
correct
===

Question T7C12 (2/425):
---
Which of the following is a common use of coaxial cable?
---
A: Carrying dc power from a vehicle battery to a mobile radio
B: Carrying RF signals between a radio and antenna
C: Securing masts, tubing, and other cylindrical objects on towers
D: Connecting data signals from a TNC to a computer
---
? a
wrong (B)
===

... and so on
```
