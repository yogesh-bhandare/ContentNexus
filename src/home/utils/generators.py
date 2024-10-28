import random
import string
from django.utils.text import slugify

# Generate random characters 
def generate_random_string(size=10):
    chars = string.ascii_lowercase + string.digits
    random_chars = [random.choice(chars) for _ in range(0, size)]
    return "".join(random_chars)

# This func return unique slug if the slug already exists in the db
def unique_sulgify(instance, _slug=None, size=5, slug_field="slug", title_field="title", invalid_slug="create"):
    # getting the title so that we can use it to make new slug
    to_slug_field = getattr(instance, title_field)
    slug = slugify(to_slug_field)
    if _slug is not None:
        slug = slugify(_slug)
    if slug == invalid_slug:
        random_str = generate_random_string(size=size)
        slug = f"{invalid_slug}-{random_str}"
    # querying in db to check for slug
    lookup = {}
    lookup[f"{slug_field}__iexact"] = slug
    # preventing redudent calling of models from generators and products models using class
    ModelClass = instance.__class__
    qs_exists = ModelClass.objects.filter(**lookup).exists()
    # generate random string and append at the back of title string
    if qs_exists:
        random_str = generate_random_string(size=size)
        new_slug = slugify(f"{to_slug_field} {random_str}")
        return unique_sulgify(instance, _slug=new_slug, size=size, slug_field=slug_field, title_field=title_field)

    return slug
