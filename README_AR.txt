مشروع بطاقة Mohammed Ahmed القابلة للتعديل
============================================

الملفات:
- index.html : محتوى البطاقة والنصوص والروابط.
- style.css  : الألوان والتصميم والمقاس.
- qr.png     : رمز QR الذي يفتح رابط السيرة الذاتية الحالي.

بيانات البطاقة الحالية:
الاسم: Mohammed Ahmed
البريد: mohammed.eisaahmed39@gmail.com
الهاتف: +966540790537
LinkedIn: https://www.linkedin.com/in/mohammed-ahmed-392004297/
العنوان: Saudi Arabia - Riyadh
CV: https://drive.google.com/file/d/1Ou9Af8_RvUKV_WsWgHUTPuZL6GeMx4V9/view?usp=drive_link

كيفية التعديل:
1) افتح index.html في VS Code أو Notepad.
2) غيّر الاسم أو البريد أو الهاتف أو LinkedIn أو العنوان أو رابط CV.
3) افتح style.css لتغيير الألوان أو حجم الخط أو توزيع العناصر.
4) إذا غيّرت رابط CV، يجب إنشاء QR جديد للرابط الجديد (التعليمات أدناه).

إنشاء QR جديد:
ثبّت المكتبة:
    pip install "qrcode[pil]"

ثم نفّذ:
    python generate_qr.py

ألصق رابط CV الجديد عندما يطلبه البرنامج، وسيتم تحديث qr.png.

معاينة:
افتح index.html مباشرة في المتصفح.

الطباعة:
افتح الصفحة في Chrome ثم Ctrl+P:
- Paper size: 90 x 50 mm أو Custom
- Margins: None
- Scale: 100%
- فعّل Background graphics
يمكن أيضاً حفظها PDF من نافذة الطباعة.

مهم:
تأكد أن Google Drive يسمح بعرض الملف لأي شخص لديه الرابط (Anyone with the link - Viewer).
اختبر QR من هاتفك قبل الطباعة.
