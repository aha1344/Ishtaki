# Generated by Django 4.1.7 on 2024-03-30 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0003_remove_report_impact_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='corruption_type',
            field=models.CharField(choices=[('فساد سياسي', 'فساد سياسي'), ('  تأثيرات سلبية على استقلالية القضاء', ' تأثيرات سلبية على استقلالية القضاء'), ('فساد قانوني', 'فساد قانوني'), ('احتكار', 'احتكار'), ('تقصير أو اهمال في توفير السلامة', 'تقصير أو اهمال في توفير السلامة '), ('فساد بيئي.', 'فساد بيئي.'), ('فساد مالي', 'فساد مالي'), (' تجاوز السلطة', ' تجاوز السلطة'), ('فساد اداري', 'فساد اداري'), ('فساد عقاري', 'فساد عقاري'), ('انتهاكات حقوق انسان', 'انتهاكات حقوق انسان'), ('تغطية', 'تغطية'), ('فساد تعييني', 'فساد تعييني'), ('فساد في العقود ', 'فساد في العقود '), ('تقييد حرية التعبير', 'تقييد حرية التعبير'), ('اهمال', 'اهمال'), ('اختلاس الأموال العامة', 'اختلاس الأموال العامة'), ('جريمة', 'جريمة'), ('سوء ادارة', 'سوء ادارة'), ('عدم الشفافية', 'عدم الشفافية'), ('فساد سلوكي / فساد أخلاقي', 'فساد سلوكي / فساد أخلاقي'), (' تلاعب بالصفقات', 'لاعب بالصفقات'), ('تهديدات عنيفة', 'تهديدات عنيفة'), ('بيروقراطية', 'بيروقراطية'), ('انحياز واستغلال الموقف', 'انحياز واستغلال الموقف'), ('تزوير واستعمال مزور', 'تزوير واستعمال مزور'), ('اتهامات بالاختلاس وغسيل الأموال', 'اتهامات بالاختلاس وغسيل الأموال'), ('احتكار', 'احتكار'), ('قمع ', ' قمع'), (' زيادة الأسعار بصورة غير مبررة', ' زيادة الأسعار بصورة غير مبررة'), (' سرقة ', ' سرقة'), ('التهريب', ' التهريب'), (' الفساد  المرتبط بالأحزاب السياسية والمسؤولين', ' الفساد المرتبط بالأحزاب السياسية والمسؤولين'), (' تقصير', ' تقصير'), ('تشويه الحقائق', 'تشويه الحقائق')], max_length=100),
        ),
    ]
