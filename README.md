# DRF Schema Generation Bug

Discussion: https://github.com/encode/django-rest-framework/discussions/9297

Video overview of bug: https://www.loom.com/share/fa04fd8423f94964810dd936864320f0?sid=bb9aaf8d-e6ea-49c4-b255-3665d533d16c

## Steps to reproduce the bug

1. Install the dependencies

```bash
pip install -r requirements.txt
```

2. Generate the schema, see DRF schema documentation: https://www.django-rest-framework.org/api-guide/schemas/

```bash
./manage.py generateschema --file openapi-schema.yml
```

3. Notice the generated schema contains the following color default:

```yaml
default: !!python/object/apply:core.models.Color
- Red
```

## Workaround

1. Override the color field in `TeamSerializer` to be:

```python
color = serializers.ChoiceField(choices=Team.Color.choices, default=Team.Color.RED.value)
```

2. Notice the generated schema contains the following color default:

```yaml
default: Red
```

## Notes

- The `!!python/object/apply` text is generated to PyYaml, see https://pyyaml.org/wiki/PyYAMLDocumentation#objects
- Bug happens with `models.IntegerChoices` and `models.TextChoices`
