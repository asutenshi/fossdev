# FOSSDEV Project: Автоматизация жизненного цикла и публикация пакета

Данный репозиторий является учебным монорепозиторием для курса
**"Культура разработки ПО с открытым исходным кодом"**.

Ветка: `feature/makeutil-pypi-release`

## 1. Описание решения

Цель работы — продемонстрировать "By-design" подход. Решение включает:

1. **Изоляцию окружения** — автоматическое создание `venv`, чтобы зависимости
   устанавливались в окружение проекта, а не в системный интерпретатор.
2. **Контроль качества (QA)** — проверку типов (`mypy`), стилей (`flake8`)
   и запуск тестов (`pytest`).
3. **Дистрибуцию** — сборку артефактов (`.whl`, `.tar.gz`) и деплой на TestPyPI.

### Архитектура: иерархические Makefile

- **Корневой Makefile** — точка входа для всего монорепозитория.
- **Локальный Makefile** (`makeutil/python-hw/Makefile`) — специфичная логика
  для данного модуля, подключает `make/venv.mk` и `make/qa.mk`.

---

## 2. Проект на TestPyPI

**[РЕАЛЬНАЯ_ССЫЛКА_НА_TEST_PYPI]**

### Установка пакета

```bash
pip install --index-url https://test.pypi.org/simple/ your-package-name
```

---

## 3. Последовательность действий (ручной способ)

```bash
# 1. Создать виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Проверка типов
mypy src/

# 4. Проверка стилей
flake8 src/

# 5. Запуск тестов
pytest

# 6. Сборка пакета
python setup.py sdist bdist_wheel

# 7. Публикация на TestPyPI
twine upload --repository testpypi dist/*
```

---

## 4. Автоматизация через Makefile

| Таргет         | Описание                                      |
|----------------|-----------------------------------------------|
| `make venv`    | Создаёт виртуальное окружение `.venv`         |
| `make install` | Устанавливает зависимости из `requirements.txt`|
| `make lint`    | Проверка типов (`mypy`) и стилей (`flake8`)   |
| `make test`    | Запускает тесты через `pytest`                |
| `make build`   | Собирает `.whl` и `.tar.gz` артефакты         |
| `make release` | Публикует пакет на TestPyPI через `twine`     |
| `make all`     | Полный цикл: venv → install → lint → test → build |
