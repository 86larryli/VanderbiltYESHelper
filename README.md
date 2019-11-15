# VanderbiltYESHelper
This is a program designed to host Vanderbilt Student's enrollment process.<br>
Selenium and Direct GET/POST are used.<br>
! This program is desigend for Vanderbilt YES Enrollment November 2019. !<br>
! The Effectiveness of the program may be subject to Vanderbilt YES system updates !<br>

**Option One: Using Selenium + Webdriver**<br>
- See VanderbiltYES.py for details.

**Option Two: Using Direct GET/POST (Recommended)**<br>
- *Actions below requires cookies.*
1. Send GET Request to https://acad.app.vanderbilt.edu/more/StudentClass!queueEnroll.action?selectedTermCode={TermCode}&enrollmentRequestItems%5B4%5D.classNumber={ClassNumber}&enrollmentRequestItems%5B4%5D.waitList={True/False}
2. A jobId will be returned from server.
3. Send GET Request to https://acad.app.vanderbilt.edu/more/StudentClass!checkStatus.action?jobId={JobID}
4. The result of the enrollment action will be returned.
- *Repeat the above steps for every course that you wish to enroll.*
