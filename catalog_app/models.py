from django.contrib.auth.models import User # Required to assign User as a borrower
from django.db import models
import uuid  # Required for unique book instances
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    book_image = models.ImageField(default='default.jpg', upload_to='book_pics')
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.author}"

class Magazine(models.Model):
    name = models.CharField(max_length=200, null=True)
    collection = models.ForeignKey('Collection', on_delete=models.SET_NULL, null=True)
    magazine_image = models.ImageField(default='default.jpg', upload_to='magazine_pics')
    issue = models.CharField(max_length=200)
    issue_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.collection} - {self.magazine_image} - {self.issue} - {self.issue_date}"

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Collection(models.Model):
    magazine_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.magazine_name}"