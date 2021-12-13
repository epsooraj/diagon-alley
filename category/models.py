from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    category_type = models.CharField(
        max_length=50, default='main')  # main, sub
    main = models.ForeignKey('self', on_delete=models.CASCADE,
                             null=True, blank=True, related_name='sub_categories')

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'category'
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
