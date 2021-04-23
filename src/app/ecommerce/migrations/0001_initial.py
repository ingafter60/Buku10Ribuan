# Generated by Django 3.1.4 on 2021-04-13 06:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Admin'), (2, 'Staff'), (3, 'Merchant'), (4, 'Customer')], default=1, max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url_slug', models.CharField(max_length=255)),
                ('thumbnail', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_price', models.CharField(max_length=255)),
                ('coupon_code', models.CharField(max_length=255)),
                ('discount_amt', models.CharField(max_length=255)),
                ('product_status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(default='', upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('auth_user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(default='', upload_to='')),
                ('company_name', models.CharField(max_length=255)),
                ('gst_details', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('auth_user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review_image', models.FileField(upload_to='')),
                ('rating', models.CharField(default='5', max_length=255)),
                ('review', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url_slug', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('product_max_price', models.CharField(max_length=255)),
                ('product_discount_price', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('product_long_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('in_stock_total', models.IntegerField(default=1)),
                ('is_active', models.IntegerField(default=1)),
                ('added_by_merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.merchantuser')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVarient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url_slug', models.CharField(max_length=255)),
                ('thumbnail', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categories')),
            ],
        ),
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(default='', upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('auth_user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVarientItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products')),
                ('product_varient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.productvarient')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_product_count', models.IntegerField(default=1)),
                ('transaction_type', models.CharField(choices=[(1, 'BUY'), (2, 'SELL')], max_length=255)),
                ('transaction_description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='subcategories_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.subcategories'),
        ),
        migrations.CreateModel(
            name='ProductReviewVoting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.productreviews')),
                ('user_id_voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customeruser')),
            ],
        ),
        migrations.AddField(
            model_name='productreviews',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products'),
        ),
        migrations.AddField(
            model_name='productreviews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customeruser'),
        ),
        migrations.CreateModel(
            name='ProductQuestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=255)),
                ('media_content', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDeliveryStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
                ('status_message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customerorders')),
            ],
        ),
        migrations.AddField(
            model_name='customerorders',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ecommerce.products'),
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(default='', upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('auth_user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
