SEO checker utils
========================================================

## Install
### Install pipenv
`brew install pipenv`

### Install dependencies
`pipenv install`

### Run with local Python
`pipenv run pytest -c pytest.ini`

### Куда положить файлы с данными для тестирования
В директорию test_data, рядом с example.xlsx

### Укажи название файла для проверки в *.ini файле конфигурации
Например, `FILE_NAME=old_and_new_urls.xlsx`