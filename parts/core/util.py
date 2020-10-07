# Handle all utility class for the project
# TODO improve documentation on this area


def max_length_field(objects, field):
    return objects._meta.get_field('field').max_length


def null_value_field(objects, field):
    return objects._meta.get_field('field').null
