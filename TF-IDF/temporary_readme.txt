===========================
        HOW TO RUN
===========================
1.) สั่งรัน python wordParser.py จะได้ภาษาไทยแบ่ง ngram ออกโฟลเดอร์ 'split_out/'

2.) สั่งรัน python tfidf.py จะได้ค่าความสำคัญของคำแต่ละคำ(ngram) ในแต่ละไฟล์จาก split_out ในรูปแบบ TF-IDF ออกทางโฟลเดอร์  result/

===========================
         DATA FLOW
===========================

  ---[Google Search Result]--->
  ---[    LexTo    ]----> ./split/*.txt
  ---[wordParser.py]----> ./split_out/*.txt 
  ---[   tfidf.py  ]----> ./result/*.txt 