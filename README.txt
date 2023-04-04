1.Для того щоб запустити цей додаток вам потрібно встановити FLASK
2. Також зверніть увагу на "UPLOAD_FOLDER = " тут ви повинні прописати повний
шлях до папки куди б вам повинно було зберігатись дані про скачування.
Як на мене простіше б було створити базу даних використовуючи MySQL.
Наприклад:
class  DowloadingReport(db.Model):
    __tablename__ = 'DowloadingReport'
    Dowloading_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    duration = db.Column(db.String(50), nullable=False)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)

3. До "ALLOWED_EXTENSIONS" додати те розширення, яке б тільки можна було скачувати
4. Для запуску цього коду ви можете використати будь який текстовий редактор, я використовував PyCharm.
