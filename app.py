from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
import re

app = Flask(__name__)
db = TinyDB('database.json')

# Пример данных в базе, всё уже включено в database.json
# db.insert({
#     "name": "MyForm",
#     "user_name": "text",
#     "order_date": "date"
# })
#
# db.insert({
#     "name": "OrderForm",
#     "user_name": "text",
#     "lead_email": "email"
# })
# db.insert({
#     "name": "PhoneForm",
#     "user_name": "text",
#     "phone": "phone"
# })


def validate_fields(data, template):
    for field, value in data.items():
        if field in template:
            field_type = template[field]
            if field_type == 'email':
                if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                    return False  # Возвращаем False, если email не валиден
            elif field_type == 'phone':
                if not re.match(r"\+\d{11}", value):
                    return False  # Возвращаем False, если телефон не валиден
            elif field_type == 'date':
                if not re.match(r"\d{4}-\d{2}-\d{2}|[0-3][0-9]\.[0-1][0-9]\.\d{4}", value):
                    return False  # Возвращаем False, если дата не валидна
    return True


def find_matching_template(data, templates):
    for template in templates:
        template_fields = {key: value for key, value in template.items() if key != 'name'}
        if all(field in data and validate_fields({field: data[field]}, template_fields) for field in template_fields):
            return template['name']
    return None


def infer_field_types(data):
    field_types = {}
    for field, value in data.items():
        if '@' in value:
            field_types[field] = 'email'
        elif value.startswith('+7'):
            field_types[field] = 'phone'
        elif '.' in value:
            field_types[field] = 'date'
        else:
            field_types[field] = 'text'
    return field_types


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()
    matching_template = find_matching_template(data, db.all())

    if matching_template:
        return matching_template
    else:
        field_types = infer_field_types(data)
        return jsonify(field_types)


if __name__ == '__main__':
    app.run(debug=True)
