from flask import flash


def flash_errors(form, category="warning"):
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)
